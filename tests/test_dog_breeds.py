import pytest
import logging

from api.petfinder_client import PetfinderClient

@pytest.mark.integration
@pytest.mark.breeds
def test_golden_retriever_in_breeds(caplog):
    caplog.set_level(logging.INFO)
    client = PetfinderClient()
    
    logging.info("Requesting dog breeds from Petfinder API")
    resp = client.get_dog_breeds()
    
    logging.info(f"Response status code: {resp.status_code}")
    assert resp.status_code == 200
    
    names = [b["name"] for b in resp.json()["breeds"]]
    logging.info(f"Number of dog breeds retrieved: {len(names)}")
    logging.info("Checking if Golden Retriever is in the breeds list")
    assert "Golden Retriever" in names