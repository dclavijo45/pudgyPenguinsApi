from config import SECRET_KEY, MYSQL_USER,MYSQL_PASSWORD, MYSQL_DB, MYSQL_HOST
from routes.server import server_v1
from flask import Flask, redirect
from routes.api import api_v1
from flask_cors import CORS

app = Flask(__name__, static_url_path='')

app.secret_key = SECRET_KEY

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(
    app,
    resources={
        r"/*": {
            "origins": "*",
            "methods": ["OPTIONS", "GET", "POST", "PUT", "DELETE"],
            "allow_headers": ["Authorization", "Content-Type"],
        }
    },
)

# Catch Http Errors
@app.errorhandler(404)
def notFound(e):
    return redirect("/api/v1/")

@app.errorhandler(405)
def methodNotAllowed(e):
    return redirect("/api/v1/")

# Api v1
app.add_url_rule(api_v1["api"], view_func=api_v1["api_controller"])
app.add_url_rule(api_v1["api_by_id"], view_func=api_v1["api_controller_by_id"])
app.add_url_rule(api_v1["api_paginator"], view_func=api_v1["api_controller_paginator"])

# Server
app.add_url_rule(server_v1["server"], view_func=server_v1["server_controller"])