import os
from dotenv import load_dotenv

import json

load_dotenv()

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
SERVER = os.getenv("SERVER")
SCHOOL = os.getenv("SCHOOL")
USERAGENT = os.getenv("USERAGENT")
CLIENT_HEADERS = json.loads(os.getenv("CLIENT_HEADERS"))