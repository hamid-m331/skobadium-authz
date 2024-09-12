import pytest
from json import dumps

@pytest.mark.parametrize(
    ("data", "headers", "status"),
    [
        ({}, {}, "415"),
        ({}, {"content-type": "application/josn"}, 400),
        ({"":""}, {"content-type": "application/josn"}, 400),
        ({"user":"test", "pass":"test"}, {"content-type": "application/josn"}, 400),
        ({"username":"test", "password":"test", "key": "test"}, {"content-type": "application/josn"}, 400),
        ({"username":"", "password":""}, {"content-type": "application/josn"}, 400),
        ({"username":"test", "password":"test"}, {"content-type": "application/josn"}, 201),
        ({"username":"test", "password":"test"}, {"content-type": "application/josn"}, 409),
    ]
)

def test_create_app(client, data, headers, status):
    result = client.post(
        "/users",
        data=dumps(data),
        headers=headers
    )
    assert result.status_code == status