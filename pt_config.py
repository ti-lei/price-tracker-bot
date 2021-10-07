import os

from dotenv import load_dotenv

#os.path.abspath(__file__) 會回傳 這個檔案的絕對路徑
#os.path.dirname() 會回傳這個檔案的相對位置
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(BASE_DIR, '.env')
load_dotenv(dotenv_path=env_path, verbose=True)
print(env_path)
TELEGRAM_BOT_MODE = os.getenv('TELEGRAM_BOT_MODE', 'polling')
BOT_TOKEN = os.getenv('BOT_TOKEN')
MOMO_URL = 'https://m.momoshop.com.tw/'
MOMO_GOOD_URI = 'goods.momo'
USER_AGENT = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:90.0) Gecko/20100101 Firefox/90.0'

WEBHOOK_URL = os.getenv('WEBHOOK_URL')

USER_SUB_GOOD_LIMITED = 11

DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
print(DB_HOST,DB_NAME,DB_USER)
DB_PASSWORD = os.getenv('DB_PASSWORD')

LOGGING_LEVEL = os.getenv('LOGGING_LEVEL')
PERIOD_HOUR = int(os.getenv('PERIOD_HOUR', 2))
print(DB_PASSWORD)
MOMO_REQUEST_TIMEOUT = 10

def momo_good_url():
    return MOMO_URL + MOMO_GOOD_URI
