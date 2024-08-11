#!/usr/bin/python3
""" Initialization module"""


from flask import Flask
from portfolio.config import app_config


def createapp(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])


    

    return app


