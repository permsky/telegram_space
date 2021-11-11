import os

import telegram
from dotenv import load_dotenv


def post_message(token: str, chat_id: str, text: str) -> None:
    """Post message in Telegram channel."""
    astro_bot = telegram.Bot(token=token)
    astro_bot.send_message(chat_id=chat_id, text=text)


def post_image(token: str, chat_id: str, image: str) -> None:
    """Post photo in Telegram channel."""
    astro_bot = telegram.Bot(token=token)
    astro_bot.send_photo(chat_id=chat_id, photo=open(image, 'rb'))


if __name__ == '__main__':
    load_dotenv()
    token = os.getenv('TELEGRAM_TOKEN')
    chat_id = '@CuriousAstro'
    message_text = 'Добро пожаловать!'
    post_message(token, chat_id, message_text)
    image = 'apod_images/apod0.jpg'
    post_image(token, chat_id, image)
