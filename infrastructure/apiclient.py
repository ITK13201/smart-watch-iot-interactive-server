import base64
import json
import logging
import requests
from urllib.parse import urlencode
from copy import deepcopy

from config.config import API_SERVER_BASE_URL, API_USER_USERNAME, API_USER_PASSWORD

logger = logging.getLogger(__name__)


def generate_auth_header(username: str, password: str) -> dict:
    basic_username_and_password = base64.b64encode(
        "{}:{}".format(username, password).encode("utf-8")
    )
    auth_header = {
        "Authorization": "Basic {}".format(basic_username_and_password.decode("utf-8"))
    }
    return auth_header


class ApiClient:
    def __init__(
        self, prefix_url: str, auth_user_username: str, auth_user_password: str
    ):
        self.prefix_url = prefix_url
        self.auth_header = generate_auth_header(auth_user_username, auth_user_password)

    def _create_url(self, endpoint: str, query: dict = None) -> str:
        if query:
            params = urlencode(query)
            return self.prefix_url + endpoint + "?" + params
        return self.prefix_url + endpoint

    def _create_headers(self, extra: dict = None) -> dict:
        headers = deepcopy(self.auth_header)
        if extra:
            headers.update(extra)
        return headers

    def fetch_status(self) -> requests.Response:
        url = self._create_url("api/v1/statuses")
        headers = self._create_headers()
        response = requests.get(url=url, headers=headers)
        logger.info(response.text)
        return response

    def create_status(self, query: dict) -> requests.Response:
        url = self._create_url("api/v1/statuses")
        headers = self._create_headers(
            {
                "Content-Type": "application/json",
            }
        )
        response = requests.post(url=url, headers=headers, data=json.dumps(query))
        logger.info(response.text)
        return response


apiClient = ApiClient(
    prefix_url=API_SERVER_BASE_URL,
    auth_user_username=API_USER_USERNAME,
    auth_user_password=API_USER_PASSWORD,
)
