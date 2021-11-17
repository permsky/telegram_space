import os
import time

import telegram
from dotenv import load_dotenv


def main() -> None:
    """Post message and images in Telegram channel wiht delay."""
    token = os.getenv('TELEGRAM_TOKEN')
    delay = os.getenv('POST_DELAY')
    bot = telegram.Bot(token=token)
    chat_id = '@CuriousAstro'
    message_text = 'Добро пожаловать!'
    bot.send_message(chat_id=chat_id, text=message_text)
    directory = 'apod_images'
    image_names = os.listdir(directory)
    while True:
        for image_number, image_path in enumerate(image_names):
            image_path = f'{directory}/{image_path}'
            with open(image_path, 'rb') as photo:
                bot.send_photo(chat_id=chat_id, photo=photo)
            if image_number == len(image_names) - 1:
                print('All images are published.')
                exit(0)
            if delay:
                time.sleep(int(delay))
            else:
                time.sleep(3600 * 24)


if __name__ == '__main__':
    load_dotenv()
    main()
