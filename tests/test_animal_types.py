import pytest
import logging

from api.petfinder_client import PetfinderClient

@pytest.mark.integration
@pytest.mark.animal_types
def test_dog_in_animal_types(caplog):
    caplog.set_level(logging.INFO)
    client = PetfinderClient()
    
    logging.info("Requesting animal types from Petfinder API")
    resp = client.get_animal_types()
    
    logging.info(f"Response status code: {resp.status_code}")
    assert resp.status_code == 200
    
    names = [t["name"] for t in resp.json()["types"]]
    logging.info(f"Retrieved animal types: {', '.join(names)}")
    assert "Dog" in names