from flask import Flask
app = Flask(__name__)

import hello_world.views    #noqa

import hello_world.views  # noqa: E902
