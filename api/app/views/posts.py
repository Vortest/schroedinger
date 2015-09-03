from app import app
from app.models.post import Post
import json
from flask_restful import reqparse, abort, Api, Resource
from app import api
from flask import Flask, request

@api.resource("/posts")
class AllPosts(Resource):
    def get(self):
        posts = Post.objects.get()
        return posts.to_json()

    def post(self):
        json = request.get_json(force=True)
        post = Post.from_json(json)
        post.save()

@api.resource("/post/<string:post_id>")
class SinglePost(Resource):
    def get(self,post_id):
        post = Post.objects.get_or_404(id=post_id)
        return post.to_json()


# @app.route('/posts')
# def get_all_posts():
#     posts = Post.objects.first_or_404()
#     return posts.to_json()
#
# @app.route('/post/<post_id>')
# def get_post(post_id):
#     # text = "Hello, World! {}".format(post_id)
#     post = Post.objects.get_or_404(id=post_id)
#     return post
