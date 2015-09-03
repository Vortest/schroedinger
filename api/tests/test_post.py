import unittest
import requests

class TestPost(unittest.TestCase):
    def test_post(self):
        requests.get("http://0.0.0.0:3031/posts")

if __name__ == "main":
    unittest.main()