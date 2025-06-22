import responses
from api.petfinder_client import PetfinderClient

@responses.activate
def test_mocked_animal_types():
    responses.add(
        responses.GET,
        "https://api.petfinder.com/v2/types",
        json={"types": [{"name": "Dog"}, {"name": "Cat"}]},
        status=200,
    )
    client = PetfinderClient()
    client.headers = {"Authorization": "Bearer mocked"}
    resp = client.get_animal_types()
    assert resp.json()["types"][0]["name"] == "Dog"
