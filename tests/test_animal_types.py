import pytest

from api.petfinder_client import PetfinderClient
@pytest.mark.integration
@pytest.mark.animal_types

def test_dog_in_animal_types():
    client = PetfinderClient()
    resp = client.get_animal_types()
    assert resp.status_code == 200
    names = [t["name"] for t in resp.json()["types"]]
    assert "Dog" in names
