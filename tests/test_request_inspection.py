import json
import yaml
from api_methods.api_client import ApiClient
from utilities.get_ip import get_external_ip
from utilities.logging import Logger
from utilities.yaml_actions import YamlActions

log = Logger(__name__).get_logger()

def test_check_headers():
    log.info("Starting test_check_headers")
    getip_endpoint = YamlActions("test_data/resources.yaml").get_yaml_value_by_key("get_headers")
    response_content = ApiClient().get(getip_endpoint).content.decode('utf-8')
    log.info(f"Response content: {response_content}")
    with open("test_data/headers.yaml", "r") as f:
        expected_headers = yaml.safe_load(f)
    missing_headers = [header
    for header in expected_headers["Headers"]
    if header not in response_content]
    log.info(f"missing_headers: {missing_headers}")
    assert not missing_headers, f"Missing headers: {missing_headers}"

def test_check_ip():
    log.info("Starting test_check_ip")
    getip_endpoint = YamlActions("test_data/resources.yaml").get_yaml_value_by_key("get_ip")
    expected_ip = get_external_ip()
    response_content = ApiClient().get(getip_endpoint).content.decode('utf-8')
    log.info(f"Response content: {response_content}")
    ip_from_tested_service = json.loads(response_content)["origin"]
    assert expected_ip == ip_from_tested_service, (
        f"Expected {expected_ip}, got {ip_from_tested_service}"
    )
    
def test_check_useragent():
    log.info("Starting test_check_useragent")
    getip_endpoint = YamlActions("test_data/resources.yaml").get_yaml_value_by_key("get_user-agent")
    response_content = ApiClient().get(getip_endpoint).content.decode('utf-8')
    log.info(f"Response content: {response_content}")
    with open("test_data/user-agent.txt", "r") as f:
        expected_useragent = f.read()
    useragent_from_tested_service = json.loads(response_content)["user-agent"]
    assert expected_useragent == useragent_from_tested_service, (
        f"Expected {expected_useragent}, got {useragent_from_tested_service}"
    )