import unittest
from app.test_base import TestBase
from models.post import Post, Comment


class TestPost(unittest.TestCase):
    def test_post(self):
        post = Post(title="Hello World!", slug="hello-world", body="Welcome to my new shiny Tumble log powered by MongoDB, MongoEngine, and Flask" )
        post.save()
        comment = Comment(author="Joe Bloggs",body="Great post! I'm looking forward to reading your blog!")
        post.comments.append(comment)
        post.save()