from flask import Flask

app = Flask(__name__)
from app import forms
from app import routes
