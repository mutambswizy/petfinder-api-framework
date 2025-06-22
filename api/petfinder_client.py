import requests
from .auth import Auth

class PetfinderClient:
    BASE_URL = "https://api.petfinder.com/v2"


    def __init__(self):
        token = Auth.get_access_token()
        self.headers = {"Authorization": f"Bearer {token}"}

    def get_animal_types(self):
        return requests.get(f"{self.BASE_URL}/types", headers=self.headers)

    def get_dog_breeds(self):
        return requests.get(f"{self.BASE_URL}/types/dog/breeds", headers=self.headers)

    def search_golden_retrievers(self):
        params = {"type": "dog", "breed": "Golden Retriever"}
        return requests.get(f"{self.BASE_URL}/animals", headers=self.headers, params=params)
