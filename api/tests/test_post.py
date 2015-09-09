import unittest
import requests

class TestPost(unittest.TestCase):
    def test_index(self):
        response = requests.get("http://0.0.0.0:3001/posts")
        assert response.status_code == 200

if __name__ == "main":
    unittest.main()