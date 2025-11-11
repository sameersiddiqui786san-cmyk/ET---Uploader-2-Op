#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "22325981"))
API_HASH = environ.get("API_HASH", "ef55d51182a725ba11fc1e3ed385c5e4")
BOT_TOKEN = environ.get("BOT_TOKEN", "8480820390:AAEiInOhk_epGB7JCn7nAbwx2EVi7qNFMFw")

OWNER = int(environ.get("OWNER", "8408897715"))
CREDIT = environ.get("CREDIT", "🔰𝙴𝚌𝚘𝚞𝚛𝚜𝚎 𝚃𝚛𝚞𝚜𝚝𝚎𝚍🤝")
cookies_file_path = os.getenv("cookies_file_path", "youtube_cookies.txt")

TOTAL_USER = os.environ.get('TOTAL_USERS', '5680454765').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '5680454765').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))






