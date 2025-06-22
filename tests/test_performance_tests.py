import time
import pytest
from api.petfinder_client import PetfinderClient

def test_api_response_times():
    client = PetfinderClient()
    
    # Test animal types endpoint performance
    start_time = time.time()
    response = client.get_animal_types()
    duration = time.time() - start_time
    assert duration < 1.0, f"get_animal_types took too long: {duration:.2f} seconds"
    assert response.status_code == 200
    
    # Test dog breeds endpoint performance
    start_time = time.time()
    response = client.get_dog_breeds()
    duration = time.time() - start_time
    assert duration < 1.0, f"get_dog_breeds took too long: {duration:.2f} seconds"
    assert response.status_code == 200
    
    # Test search endpoint performance
    start_time = time.time()
    response = client.search_golden_retrievers()
    duration = time.time() - start_time
    assert duration < 2.0, f"search_golden_retrievers took too long: {duration:.2f} seconds"
    assert response.status_code == 200

@pytest.mark.parametrize("endpoint_method", [
    "get_animal_types",
    "get_dog_breeds",
    "search_golden_retrievers"
])
def test_endpoint_consistency(endpoint_method):
    """Test response time consistency across multiple calls"""
    client = PetfinderClient()
    method = getattr(client, endpoint_method)
    
    durations = []
    for _ in range(3):  # Make 3 calls to check consistency
        start_time = time.time()
        response = method()
        duration = time.time() - start_time
        durations.append(duration)
        assert response.status_code == 200
        time.sleep(1)  # Avoid rate limiting
    
    # Check if response times are consistent (within 50% of mean)
    mean_duration = sum(durations) / len(durations)
    for duration in durations:
        assert abs(duration - mean_duration) < (mean_duration * 0.5), \
            f"Response time variance too high for {endpoint_method}"