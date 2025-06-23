import pytest

from api.petfinder_client import PetfinderClient
@pytest.mark.integration
@pytest.mark.retrievers
def test_golden_retriever_search_returns_results():
    client = PetfinderClient()
    resp = client.search_golden_retrievers()
    assert resp.status_code == 200
    assert len(resp.json().get("animals", [])) > 0
