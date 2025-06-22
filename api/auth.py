import os
import requests
from dotenv import load_dotenv

load_dotenv()

class Auth:
    @staticmethod
    def get_access_token():
        url = "https://api.petfinder.com/v2/oauth2/token"
        data = {
            "grant_type": "client_credentials",
             "client_id": os.getenv("PETFINDER_CLIENT_ID"),
            "client_secret": os.getenv("PETFINDER_CLIENT_SECRET"),

        }
        resp = requests.post(url, data=data)
        resp.raise_for_status()
        return resp.json()["access_token"]
