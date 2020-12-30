#!/usr/bin/env python3

from flask import Flask, request


app = Flask(__name__)

@app.route("/api/post_data/<uuid>", methods=["POST"])
def use_json(uuid):
    content = request
    # print(content.json)
    # print(f"{uuid}")
    return request.get_json()


if __name__ == "__main__":
    app.run()
