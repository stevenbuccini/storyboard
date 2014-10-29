from flask import Flask

app = Flask(__name__)

from app.views import infra
#TODO: figure out a better way to do this.
from app.views import nodes