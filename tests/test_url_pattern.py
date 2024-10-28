from flask.testing import FlaskClient
import pytest


@pytest.mark.parametrize("msg, response", [
    ('red', 'red'),
    ('green', 'green'),
    ('blue', 'blue'),
    ('grey', 'invalid color')
])
def test_url_pattern(client: FlaskClient, msg, response):
    resp = client.get(f'/check/{msg}')
    assert resp.data == response.encode()


@pytest.mark.parametrize("num1, num2", [
    (2, 3),
    (0, 0)
]
)
def test_add_in_url(client: FlaskClient, num1, num2):
    resp = client.get(f'/add/{num1}/{num2}')
    assert int(resp.data) == (num1 + num2)


@pytest.mark.parametrize("query, response", [
    ('?name=John', 'Hello John'),
    ('?name=', 'Hello Anonymous'),
    ('?fake=123', 'Invalid query parameter')
])
def test_query_string(client: FlaskClient, query: str, response: str):
    resp = client.get(f'/query{query}')
    assert resp.data == response.encode()
