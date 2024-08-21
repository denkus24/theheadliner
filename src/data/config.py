import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv('MONGO_URI')
DATABASE_NAME = os.getenv('DATABASE_NAME')
BOT_API = os.getenv('BOT_API')
ADMIN_ID = os.getenv('ADMIN_ID')

HOUR_DELAY = 2
SUPPORTABLE_LANGUAGES = ['uk', 'ru', 'en']
