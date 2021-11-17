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
    images_list = os.listdir(directory)
    while True:
        for image_number, image in enumerate(images_list):
            image = f'{directory}/{image}'
            bot.send_photo(chat_id=chat_id, photo=open(image, 'rb'))
            if image_number == len(images_list) - 1:
                print('All images are published.')
                exit(0)
            if delay:
                time.sleep(int(delay))
            else:
                time.sleep(3600 * 24)
