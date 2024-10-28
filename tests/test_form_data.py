from flask.testing import FlaskClient
import pytest


@pytest.mark.parametrize("data, response", [
    ({'name': 'John'}, 'Hello John'),
    ({'name': ''}, 'Hello Anonymous'),
    ({}, 'name required')]
)
def test_form_data(client: FlaskClient, data, response):
    data = {'name': 'John'}
    resp = client.post('/data', data=data)
    assert resp.data == response.encode()


class TestFileUpload:
    def create_large_file(self, file_path, size_in_bytes):
        with open(file_path, 'wb') as f:
            f.seek(size_in_bytes - 1)
            f.write(b'\0')

    def test_file_upload(self, client: FlaskClient, tmp_path):
        test_file = tmp_path / 'test.txt'
        test_file.write_text('Hello World')
        with test_file.open('rb') as f:
            data = {'file': (f, 'test.txt')}
            resp = client.post('/upload', data=data)
            assert resp.data == b'File uploaded successfully'

    def test_no_file_upload(self, client: FlaskClient):
        data = {'file': (None, '')}
        resp = client.post('/upload', data=data)
        assert b'No file uploaded' in resp.data

    def test_large_file_upload(self, client: FlaskClient, tmp_path):
        large_file_path = tmp_path / "large_file.txt"
        self.create_large_file(large_file_path, 2 * 1024 * 1024 + 1)
        with large_file_path.open('rb') as f:
            data = {'file': (f, 'test.txt')}
            resp = client.post('/upload', data=data)
            assert resp.data == b'File size exceeds limit of 2MB'
