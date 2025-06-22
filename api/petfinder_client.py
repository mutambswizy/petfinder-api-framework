import requests
from .auth import Auth

class PetfinderClient:
    # Base URL for all Petfinder API endpoints
    BASE_URL = "https://api.petfinder.com/v2"

    def __init__(self):
        # Initialize client with OAuth token
        token = Auth.get_access_token()
        self.headers = {"Authorization": f"Bearer {token}"}

    def get_animal_types(self):
        # Fetch available animal types (dog, cat, etc.)
        return requests.get(f"{self.BASE_URL}/types", headers=self.headers)

    def get_dog_breeds(self):
        # Fetch list of all dog breeds
        return requests.get(f"{self.BASE_URL}/types/dog/breeds", headers=self.headers)

    def search_golden_retrievers(self):
        # Search specifically for Golden Retriever dogs
        params = {"type": "dog", "breed": "Golden Retriever"}
        return requests.get(f"{self.BASE_URL}/animals", headers=self.headers, params=params)