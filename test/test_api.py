import unittest

from app import app


class TestAPI(unittest.TestCase):

    def test_get_index_end_point(self):
        with app.test_client() as client:
            response = client.get('/')
            assert response.status_code == 200

    def test_post_index_end_point(self):
        with app.test_client() as client:
            response = client.post('/', json={"word": "This"})
            assert response.status_code == 302
