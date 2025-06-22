import responses
from api.petfinder_client import PetfinderClient

@responses.activate
def test_mocked_animal_types():
    # Mock the token endpoint
    responses.add(
        responses.POST,
        "https://api.petfinder.com/v2/oauth2/token",
        json={"access_token": "mocked_token"},
        status=200,
    )
    
    # Mock the types endpoint
    responses.add(
        responses.GET,
        "https://api.petfinder.com/v2/types",
        json={"types": [{"name": "Dog"}, {"name": "Cat"}]},
        status=200,
    )
    
    client = PetfinderClient()
    resp = client.get_animal_types()
    assert resp.json()["types"][0]["name"] == "Dog"