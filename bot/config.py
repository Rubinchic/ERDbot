import os
from dotenv import load_dotenv

# Завантаження змінних із .env
load_dotenv()

# Змінні середовища
API_TOKEN = os.getenv('API_TOKEN')
ADMIN_CHAT_ID = os.getenv('ADMIN_CHAT_ID')

# Перевірка змінних
if not API_TOKEN:
    raise ValueError("API_TOKEN не знайдено. Перевірте файл .env")
if not ADMIN_CHAT_ID:
    raise ValueError("ADMIN_CHAT_ID не знайдено. Перевірте файл .env")
