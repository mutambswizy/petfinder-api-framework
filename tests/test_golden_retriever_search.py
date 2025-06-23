import pytest
import logging

from api.petfinder_client import PetfinderClient

@pytest.mark.integration
@pytest.mark.retrievers
def test_golden_retriever_search_returns_results():
    client = PetfinderClient()
    
    logging.info("Searching for Golden Retrievers via Petfinder API")
    resp = client.search_golden_retrievers()
    
    logging.info(f"Response status code: {resp.status_code}")
    assert resp.status_code == 200
    
    animals = resp.json().get("animals", [])
    logging.info(f"Number of Golden Retrievers found: {len(animals)}")
    assert len(animals) > 0