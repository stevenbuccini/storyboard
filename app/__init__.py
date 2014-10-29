from flask import Flask

app = Flask(__name__)

from app.views.infra import healthcheck
#TODO: figure out a better way to do this.
from app.views.nodes import *