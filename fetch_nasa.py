import datetime
import os
from pathlib import Path
from urllib.parse import unquote, urlsplit

import requests
from dotenv import load_dotenv

from utils import download_image


def get_photo_links(url: str, params: dict) -> list:
    """Return links on Astronomy Picture of the Day."""
    response = requests.get(url, params=params)
    response.raise_for_status()
    apod_urls = []
    for apod in response.json():
        apod_urls.append(apod['url'])
    return apod_urls


def get_extension(url: str) -> str:
    """Return file extension from url."""
    url_components = urlsplit(url)
    url_path = unquote(url_components.path)
    return os.path.splitext(url_path)[1]


def fetch_apod(url: str, params: dict, directory: str) -> None:
    """Fetch APOD into determined directory."""
    photo_links = get_photo_links(url, params)
    Path(directory).mkdir(exist_ok=True)
    for photo_number, photo_link in enumerate(photo_links):
        image_extension = get_extension(photo_link)
        if not image_extension:
            continue
        image_name = f'{directory}apod{photo_number}{image_extension}' 
        download_image(photo_link, image_name)


def fetch_epic(url: str, params: dict, directory: str) -> None:
    """Fetch EPIC into determined directory."""
    response = requests.get(url, params=params)
    response.raise_for_status()
    images = response.json()
    for image in images:
        image_name = image['image']
        image_date = datetime.datetime.fromisoformat(image['date'])
        formatted_image_date = image_date.strftime('%Y/%m/%d')
        image_url = (
            f'https://api.nasa.gov/EPIC/archive/natural/'
            f'{formatted_image_date}/png/{image_name}.png'
        )
        response = requests.get(image_url, params=params)
        response.raise_for_status()
        
        Path(directory).mkdir(exist_ok=True)
        image_name = f'{directory}{image_name}.png'
        with open(image_name, 'wb') as img:
            img.write(response.content)


def main() -> None:
    """Fetch EPIC and APOD images from NASA."""
    nasa_token = os.getenv('NASA_TOKEN')
    apod_url = 'https://api.nasa.gov/planetary/apod'
    apod_get_params = {
        'api_key': nasa_token,
        'start_date': '2021-10-07',
        'end_date': '2021-11-07',
    }
    apod_images_directory = './apod_images/'
    fetch_apod(apod_url, apod_get_params, apod_images_directory)
    epic_url = 'https://api.nasa.gov/EPIC/api/natural/images'
    epic_get_params = {'api_key': nasa_token}
    epic_images_directory = './epic_images/'
    fetch_epic(epic_url, epic_get_params, epic_images_directory)


if __name__ == '__main__':
    load_dotenv()
    main()
