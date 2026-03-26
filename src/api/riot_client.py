import os
import requests
from dotenv import load_dotenv

load_dotenv()

class RiotClient:
    def __init__(self):
        self.api_key = os.getenv("RIOT_API_KEY")
        self.headers = {"X-Riot-Token": self.api_key}

    def get(self, url, params=None):
        res = requests.get(url, headers=self.headers, params=params)
        res.raise_for_status()
        return res.json()