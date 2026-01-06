import json
import uuid
from api_methods.api_client import ApiClient
from utilities.logging import Logger
from utilities.randomizer import get_random_int
from utilities.yaml_actions import YamlActions

log = Logger(__name__).get_logger()

def test_check_bytes_generator():
    log.info("Starting test_check_bytes_generator")
    endpoint = YamlActions("test_data/resources.yaml").get_yaml_value_by_key("get_bytes_generator")
    random_bytes_number = get_random_int(1, 10)
    response_content = ApiClient().get(f"{endpoint}{random_bytes_number}")
    log.info(f"Response content: {response_content.content}")
    assert isinstance(response_content.content, bytes), f"Responce content is not Bytes type. Actual type is {type(response_content.content)}"

def test_check_uuid4():
    log.info("Starting test_check_uuid4")
    getuuid_endpoint = YamlActions("test_data/resources.yaml").get_yaml_value_by_key("get_uuid")
    response_content = ApiClient().get(getuuid_endpoint).content.decode('utf-8')
    log.info(f"Response content: {response_content}")
    uuid_from_service = json.loads(response_content)["uuid"]
    assert uuid.UUID(uuid_from_service).version == 4, "UUID is not a version 4 or not a valid UUID"