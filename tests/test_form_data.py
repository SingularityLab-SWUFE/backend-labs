from flask.testing import FlaskClient
import pytest


@pytest.mark.parametrize("data, response", [
    ({'name': 'John'}, 'Hello John'),
    ({'name': ''}, 'Hello Anonymous')]
)
def test_form_data(client: FlaskClient, data, response):
    resp = client.post('/data', data=data)
    assert resp.data == response.encode()


class TestFileUpload:
    def test_file_upload(self, client: FlaskClient, tmp_path):
        test_file = tmp_path / 'test.txt'
        test_file.write_text('Hello World')
        with open(test_file, 'rb') as f:
            data = {'file': f}
            resp = client.post('/upload', data=data)
            assert resp.data == b'File uploaded successfully'

    def test_no_file_upload(self, client: FlaskClient):
        data = {'file': (None, '')}
        resp = client.post('/upload', data=data)
        assert b'No file uploaded' in resp.data

    def test_large_file_upload(self, client: FlaskClient, tmp_path):
        test_file = tmp_path / "test.txt"
        with test_file.open('wb') as f:
            f.write(b'\0' * (2 * 1024 * 1024 + 1))
        with test_file.open('rb') as f:
            data = {'file': (f, 'test.txt')}
            resp = client.post('/upload', data=data)
            assert resp.data == b'File size exceeds limit of 2MB'
