from locust import HttpUser, task

class PetfinderLoadTest(HttpUser):
    @task
    def get_golden_retrievers(self):
        self.client.get("/v2/animals?type=dog&breed=Golden%20Retriever")
