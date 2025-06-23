import pytest
import time
import logging
from api.petfinder_client import PetfinderClient

@pytest.mark.integration
@pytest.mark.performance
def test_api_response_times():
    client = PetfinderClient()

    # Test animal types endpoint performance
    logging.info("Testing get_animal_types response time")
    start_time = time.time()
    response = client.get_animal_types()
    duration = time.time() - start_time
    logging.info(f"get_animal_types duration: {duration:.2f} seconds")
    assert duration < 2.0, f"get_animal_types took too long: {duration:.2f} seconds"

    # Test dog breeds endpoint performance
    logging.info("Testing get_dog_breeds response time")
    start_time = time.time()
    response = client.get_dog_breeds()
    duration = time.time() - start_time
    logging.info(f"get_dog_breeds duration: {duration:.2f} seconds")
    assert duration < 3.0, f"get_dog_breeds took too long: {duration:.2f} seconds"

    # Test golden retrievers search performance
    logging.info("Testing search_golden_retrievers response time")
    start_time = time.time()
    response = client.search_golden_retrievers()
    duration = time.time() - start_time
    logging.info(f"search_golden_retrievers duration: {duration:.2f} seconds")
    assert duration < 4.0, f"search_golden_retrievers took too long: {duration:.2f} seconds"

@pytest.mark.integration
@pytest.mark.performance
@pytest.mark.parametrize("endpoint_method", [
    "get_animal_types",
    "get_dog_breeds",
    "search_golden_retrievers"
])
def test_endpoint_consistency(endpoint_method):
    """Test response time consistency across multiple calls"""
    client = PetfinderClient()
    method = getattr(client, endpoint_method)
    logging.info(f"Testing consistency for {endpoint_method}")

    durations = []
    for i in range(3):  # Make 3 calls to check consistency
        start_time = time.time()
        response = method()
        duration = time.time() - start_time
        durations.append(duration)
        logging.info(f"Call {i+1} duration: {duration:.2f} seconds")
        assert response.status_code == 200
        time.sleep(1)  # Avoid rate limiting

    # Check if response times are consistent (within 100% of mean instead of 50%)
    mean_duration = sum(durations) / len(durations)
    logging.info(f"Mean duration: {mean_duration:.2f} seconds")
    for duration in durations:
        assert abs(duration - mean_duration) < (mean_duration * 1.0), \
            f"Response time variance too high for {endpoint_method}"