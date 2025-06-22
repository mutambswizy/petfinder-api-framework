from api.petfinder_client import PetfinderClient

def test_golden_retriever_in_breeds():
    client = PetfinderClient()
    resp = client.get_dog_breeds()
    assert resp.status_code == 200
    names = [b["name"] for b in resp.json()["breeds"]]
    assert "Golden Retriever" in names
