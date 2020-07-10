import pytest
import requests

from config.env_config import QA_BASE_URL


@pytest.fixture(scope="module")
def d():
    data = {"pwd": "tjf123", "userName": "tan241094"}
    r = requests.request("POST",QA_BASE_URL + '/login', json=data)
    print(r.text)
    return {"token": r.json()["data"]["token"]}
