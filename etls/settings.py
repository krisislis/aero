import dotenv

SETTINGS = {}
SETTINGS.update(dotenv.dotenv_values('.env'))
