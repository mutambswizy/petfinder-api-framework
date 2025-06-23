import pytest
import responses
import logging

from api.petfinder_client import PetfinderClient

@pytest.mark.unit
@pytest.mark.petfinder
@responses.activate
def test_mocked_animal_types(caplog):
    caplog.set_level(logging.INFO)
    
    logging.info("Setting up mock responses")
    # Mock the token endpoint
    responses.add(
        responses.POST,
        "https://api.petfinder.com/v2/oauth2/token",
        json={"access_token": "mocked_token"},
        status=200,
    )
    logging.info("Mocked OAuth token endpoint")
    
    # Mock the types endpoint
    responses.add(
        responses.GET,
        "https://api.petfinder.com/v2/types",
        json={"types": [{"name": "Dog"}, {"name": "Cat"}]},
        status=200,
    )
    logging.info("Mocked animal types endpoint")
    
    client = PetfinderClient()
    logging.info("Making request to mocked endpoint")
    resp = client.get_animal_types()
    
    logging.info(f"Response received: {resp.json()}")
    assert resp.json()["types"][0]["name"] == "Dog"