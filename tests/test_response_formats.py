import json
from api_methods.api_client import ApiClient
from utilities.logging import Logger
from utilities.yaml_actions import YamlActions

log = Logger(__name__).get_logger()

def test_check_json():
    log.info("Starting test_check_json")
    getip_endpoint = YamlActions("test_data/resources.yaml").get_yaml_value_by_key("get_json")
    response_content = ApiClient().get(getip_endpoint).content.decode('utf-8')
    log.info(f"Response content:\n{response_content}")
    assert response_content.startswith("{") and response_content.endswith("}\n"), "Response content does not start with { and end with }"

def test_check_html():
    log.info("Starting test_check_html")
    with open("test_data/html_keywords.json", "r") as f:
        html_keywords = json.load(f)
    getip_endpoint = YamlActions("test_data/resources.yaml").get_yaml_value_by_key("get_html")
    response_content = ApiClient().get(getip_endpoint).content.decode('utf-8')
    log.info(f"Response content:\n{response_content}")
    assert response_content.startswith("<!DOCTYPE html>") and response_content.endswith("</html>"), "Response content does not start with <html> and end with </html>"
    for keyword in html_keywords:
            assert keyword in response_content, f"Keyword {keyword} not found in response content"

def test_check_robots():
    log.info("Starting test_check_robots")
    getip_endpoint = YamlActions("test_data/resources.yaml").get_yaml_value_by_key("get_robots")
    response_content = ApiClient().get(getip_endpoint).content.decode('utf-8')
    log.info(f"Response content:\n{response_content}")
    assert response_content.startswith("User-agent: *") and response_content.endswith("Disallow: /deny\n"), "Response content does not start with User-agent: * and end with Disallow: /"