import requests


def download_image(url: str, image_name: str) -> None:
    """Download image from url."""
    response = requests.get(url)
    response.raise_for_status()

    with open(image_name, 'wb') as img:
        img.write(response.content)
