from os import getenv

from dotenv import load_dotenv

load_dotenv()
que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN", "6254171749:AAFn9tbZaVK4nTuhAbYX6mVqzVPYpJ-YdNk")
BOT_USERNAME = getenv("BOT_USERNAME", "nilaymusicbot")
admins = {}
API_ID = int(getenv("API_ID", "18052289"))
API_HASH = getenv("API_HASH", "552525f45a3066fee54ca7852235c19c")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1924693109").split()))
