from os import getenv

que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
admins = {}
API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH")
