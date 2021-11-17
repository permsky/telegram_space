import os
import time

import telegram
from dotenv import load_dotenv


if __name__ == '__main__':
    load_dotenv()
    token = os.getenv('TELEGRAM_TOKEN')
    delay = os.getenv('POST_DELAY')
    bot = telegram.Bot(token=token)
    chat_id = '@CuriousAstro'
    message_text = 'Добро пожаловать!'
    bot.send_message(chat_id=chat_id, text=message_text)
    directory = 'apod_images'
    images = os.listdir(directory)
    while True:
        for image_number, image_path in enumerate(images):
            image_path = f'{directory}/{image_path}'
            with open(image_path, 'rb') as photo:
                bot.send_photo(chat_id=chat_id, photo=photo)
            if image_number == len(images) - 1:
                print('All images are published.')
                exit(0)
            if delay:
                time.sleep(int(delay))
            else:
                time.sleep(3600 * 24)
