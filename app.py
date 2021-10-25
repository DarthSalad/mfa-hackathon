import flask
from flask import Flask, redirect, request, url_for
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)

app=Flask(__name__)

if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)