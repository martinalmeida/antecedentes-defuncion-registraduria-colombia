from dotenv import load_dotenv
import os

class ExtractConstEnv:
    def __init__(self):
        load_dotenv()
        self.env = {
            "name": os.getenv("APP_NAME"),
            "url": os.getenv("APP_URL")
        }

    def get_env(self):
        return self.env