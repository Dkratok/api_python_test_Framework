import logging
import requests
from utilities.yaml_actions import YamlActions
from utilities.logging import Logger


class ApiClient:

    log = Logger(__name__).get_logger()

    def __init__(self, default_headers: dict | None = None):
        self.config_path = "config.yaml"
        self.base_url = YamlActions(self.config_path).get_yaml_value_by_key("base_url")
        self.session = requests.Session()
        self.session.headers.update(default_headers or {})

    def get(self, endpoint: str, params: dict | None = None, headers: dict | None = None):
        url = f"{self.base_url}/{endpoint}"
        self.log.info(f"Starting GET request: {url} | headers={headers} | params={params}")
        return self.session.get(url, params=params, headers=headers)

    def post(self, endpoint: str, json: dict | None = None, data=None, headers: dict | None = None):
        url = f"{self.base_url}/{endpoint}"
        self.log.info(f"Starting POST request: {url} | headers={headers} |body={json or data}")
        return self.session.post(url, json=json, data=data, headers=headers)

    def put(self, endpoint: str, json: dict | None = None, headers: dict | None = None):
        url = f"{self.base_url}/{endpoint}"
        self.log.info(f"Starting PUT request: {url} | headers={headers} | body={json}")
        return self.session.put(url, json=json, headers=headers)

    def patch(self, endpoint: str, json: dict | None = None, headers: dict | None = None):
        url = f"{self.base_url}/{endpoint}"
        self.log.info(f"Starting PATCH request: {url} | headers={headers} | body={json}")
        return self.session.patch(url, json=json, headers=headers)

    def delete(self, endpoint: str, headers: dict | None = None):
        url = f"{self.base_url}/{endpoint}"
        self.log.info(f"Starting DELETE request: {url} | headers={headers}")
        return self.session.delete(url, headers=headers)