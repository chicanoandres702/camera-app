# app.py
import os
import json
from flask import Flask
from database import get_user_data  # <-- Add this line!

app = Flask(__name__)

@app.route('/')
def hello():
    user = get_user_data()
    return f"Hello from the camera app! User: {user['user']}"
