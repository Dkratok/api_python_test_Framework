import pytest
from utilities.logging import Logger

logger = Logger(__name__).get_logger()

@pytest.fixture(scope="session", autouse=True)
def global_setup_teardown():
    logger.info("=== Test session START ===")

    yield

    logger.info("=== Test session END ===\n")

@pytest.fixture(autouse=True)
def per_test_setup_teardown():
    logger.info("=== Test START ===")

    yield

    logger.info("=== Test END ===")