import json
import uuid
from api_methods.api_client import ApiClient
from utilities.logging import Logger
from utilities.yaml_actions import YamlActions
from utilities.randomizer import get_random_int

log = Logger(__name__).get_logger()

def test_check_uuid4():
    log.info("Starting test_check_uuid4")
    getuuid_endpoint = YamlActions("test_data/resources.yaml").get_yaml_value_by_key("get_uuid")
    response_content = ApiClient().get(getuuid_endpoint).content.decode('utf-8')
    log.info(f"Response content: {response_content}")
    uuid_from_service = json.loads(response_content)["uuid"]
    assert uuid.UUID(uuid_from_service).version == 4, "UUID is not a version 4 or not a valid UUID"

def test_check_bytes_generator():
    log.info("Starting test_check_bytes_generator")
    endpoint = YamlActions("test_data/resources.yaml").get_yaml_value_by_key("get_bytes_generator")
    random_bytes_number = get_random_int(1, 10)
    response_content = ApiClient().get(f"{endpoint}{random_bytes_number}")
    log.info(f"Response content: {response_content.content}")
    assert response_content.content is not None and response_content.content.startswith("b"), f"Responce content value: {response_content.content}. It is None or does not start with 'b'."
