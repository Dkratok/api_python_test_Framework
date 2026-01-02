import json
from api_methods.api_client import ApiClient
from utilities.get_ip import get_external_ip
from utilities.logging import Logger
from utilities.yaml_actions import YamlActions

log = Logger(__name__).get_logger()

def test_dynamic_data():
    log.info("Starting test_dynamic_data")
    getip_endpoint = YamlActions("test_data/resources.yaml").get_yaml_value_by_key("get_ip")
    expected_ip = get_external_ip()
    responce_content = ApiClient().get(getip_endpoint).content.decode('utf-8')
    ip_from_tested_service = json.loads(responce_content)["origin"]
    assert expected_ip == ip_from_tested_service, (
        f"Expected {expected_ip}, got {ip_from_tested_service}"
    )