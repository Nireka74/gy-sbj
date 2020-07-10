import pytest
import requests

from config.env_config import QA_BASE_URL


@pytest.fixture(scope="module")
def d():
    data = {"pwd": "aa123456", "userName": "testr0013"}
    r = requests.request("POST", QA_BASE_URL + '/login', json=data)
    print(r.text)
    return {"token": r.json()["data"]["token"]}
