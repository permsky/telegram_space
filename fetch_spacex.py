from pathlib import Path

import requests

from utils import download_image


def get_photo_links(url: str) -> list:
    """Return list of links on photos of SpaceX launch."""
    response = requests.get(url)
    response.raise_for_status() 
    return response.json()['links']['flickr_images']


def fetch_spacex_launch(url: str, directory: str) -> None:
    """Fetch SpaceX launch photos into determined directory."""
    photo_links = get_photo_links(url)
    Path(directory).mkdir(exist_ok=True)
    for photo_number, photo_link in enumerate(photo_links):
        image_name = f'{directory}spacex{photo_number}.jpg' 
        download_image(photo_link, image_name)
    

if __name__ == '__main__':
    spacex_launch_url = 'https://api.spacexdata.com/v3/launches/99'
    images_directory = './images/'
    fetch_spacex_launch(spacex_launch_url, images_directory)
