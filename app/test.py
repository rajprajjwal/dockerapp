import unittest
import app
import ssl
from http.client import HTTPSConnection
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)

# Create HTTPS connection
c = HTTPSConnection("0.0.0.0", context=context)

class TestDockerapp(unittest.TestCase):

    def setUp(self):
        self.app = app.app.test_client()

    def test_save_value(self):
        response = self.app.post('/', data=dict(submit='save', key='2', cache_value='two'))
        assert response.status_code == 200
        assert b'2' in response.data
        assert b'two' in response.data

    def test_load_value(self):
        self.app.post('/', data=dict(submit='save', key='2', cache_value='two'))
        response = self.app.post('/', data=dict(submit='load', key='2'))
        assert response.status_code == 200
        assert b'2' in response.data
        assert b'two' in response.data

if __name__=='__main__':
    unittest.main()
