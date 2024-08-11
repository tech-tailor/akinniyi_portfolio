#!/usr/bin/activate
""" Configuration for the app"""
import os


class Config:
    """ Configuration for the app"""

    SECRET_KEY = "gfds3456jnvcserynn965dcv"
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = 'ogundareakinniyi8@gmail.com'
    MAIL_PASSWORD =  'oosuxqwbcmhqlufu'
    MAIL_DEFAULT_SENDER = ('portfolio', 'ogundareakinniyi8@gmail.com')



class DevelopmentConfig(Config):
    """ development onfiguration for the app"""

    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}