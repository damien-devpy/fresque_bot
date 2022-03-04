import json
from os import environ

import pytest
import requests


@pytest.fixture
def response():
    url = environ.get("URL")
    response = requests.get(url)
    return response.json()


@pytest.fixture
def content():
    return json.loads(
        """{
        "data": {
            "rows": [
                [327342]
            ],
            "cols": [
                {
                    "base_type": "type/BigInteger","semantic_type":"type/Quantity","settings":null,"name":"sum","display_name":"Somme de Participants Number","source":"aggregation","field_ref":["aggregation",0],"effective_type":"type/BigInteger"}],"insights":null,"results_timezone":"Etc/UTC"},
"json_query":{},"status":"completed"}"""
    )


@pytest.fixture
def wrong_content():
    return {"not_the_expected_content": ""}
