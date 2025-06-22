from locust import HttpUser, task, between

class PetfinderLoadTest(HttpUser):
    # Simulate realistic user behavior with random 1-3 second delays between requests
    wait_time = between(1, 3)
    
    # Base URL for all API requests
    host = "https://api.petfinder.com"
    
    def on_start(self):
        """Initialize user session with authentication"""
        # Get access token before starting the tests
        self.client.post("/v2/oauth2/token", 
                        data={
                            "grant_type": "client_credentials",
                            "client_id": "your_client_id",
                            "client_secret": "your_client_secret"
                        })

    @task(3)  # This task runs 3x more frequently than weight-1 tasks
    def get_golden_retrievers(self):
        # Search for Golden Retrievers with 2-second timeout
        with self.client.get(
            "/v2/animals?type=dog&breed=Golden%20Retriever",
            name="/v2/animals - Golden Retrievers"  # Custom name in Locust statistics
        ) as response:
            assert response.elapsed.total_seconds() < 2.0, "Response too slow"

    @task(2)  # This task runs 2x more frequently than weight-1 tasks
    def get_animal_types(self):
        # Get list of animal types with 1-second timeout
        with self.client.get("/v2/types", name="/v2/types") as response:
            assert response.elapsed.total_seconds() < 1.0

    @task(1)  # Baseline weight for task frequency
    def get_dog_breeds(self):
        # Get list of dog breeds with 1.5-second timeout
        with self.client.get("/v2/types/dog/breeds", name="/v2/types/dog/breeds") as response:
            assert response.elapsed.total_seconds() < 1.5