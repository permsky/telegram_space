# Space Telegram

### fetch_spasex.py
Fetch SpaceX launch photos from [api.spacexdata.com](https://api.spacexdata.com/).
### fetch_nasa.py
Fetch APOD and EPIC images from [api.nasa.gov](https://api.nasa.gov/).
### telegram_bot_post.py
Script post a message and all images from determinded directory with delay to Telegram channel. Default delay is 24 hours. You can change the delay by assigning new value in seconds to ```POST_DELAY``` variable in ```.env``` file in script directory. For example, to set delay 10 seconds:

```POST_DELAY=10```

### How to install
Python3.x should be already installed.
Recommended to use virtual environment [virtualenv/venv](https://docs.python.org/3/library/venv.html) for project isolation.
For installing dependencies run:

```pip install -r requirements.txt```

Or (if there is a conflict with Python2.x):

```pip3 install -r requirements.txt```

To work with NASA and Telegram API needed tokens. You can generate API key for NASA on address [api.nasa.gov](https://api.nasa.gov/). You should save it in ```NASA_TOKEN``` variable in ```.env``` file in script directory:

```NASA_TOKEN=abcdefghjiklmnopqrstuvwxyz1234567890ABCD```

After creating new Telegram bot with ```@BotFather``` you get token for HTTP API. You should save it in ```TELEGRAM_TOKEN``` variable in ```.env``` file in script directory:

```TELEGRAM_TOKEN=0123456789:ABCDEF12345_ABCDEabcde1234567890_Ab```

### Project Goals
The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).