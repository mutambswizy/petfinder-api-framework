import pytest
import logging

def pytest_configure(config):
    """Set up logging configuration for tests"""
    logging.basicConfig(
        format='%(asctime)s [%(levelname)8s] %(message)s',
        level=logging.INFO
    )

@pytest.fixture(autouse=True)
def setup_logging(caplog):
    """Set up logging for each test"""
    caplog.set_level(logging.INFO)
    return caplog