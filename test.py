from flask import Flask, url_for

app = Flask(__name__)

with app.test_request_context():
    print(url_for("hello"))