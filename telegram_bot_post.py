import os
import time

import telegram
from dotenv import load_dotenv


def post_message(bot: telegram.Bot, chat_id: str, text: str) -> None:
    """Post message in Telegram channel."""
    bot.send_message(chat_id=chat_id, text=text)


def post_image(bot: telegram.Bot, chat_id: str, image: str) -> None:
    """Post photo in Telegram channel."""
    bot.send_photo(chat_id=chat_id, photo=open(image, 'rb'))


if __name__ == '__main__':
    load_dotenv()
    token = os.getenv('TELEGRAM_TOKEN')
    delay = os.getenv('POST_DELAY')
    bot = telegram.Bot(token=token)
    chat_id = '@CuriousAstro'
    message_text = 'Добро пожаловать!'
    post_message(bot, chat_id, message_text)
    directory = 'apod_images'
    images_list = os.listdir(directory)
    while True:
        for image_number, image in enumerate(images_list):
            image = f'{directory}/{image}'
            post_image(bot, chat_id, image)
            if image_number == len(images_list) - 1:
                print('All images are published.')
                exit(0)
            if delay:
                time.sleep(int(delay))
            else:
                time.sleep(3600 * 24)
