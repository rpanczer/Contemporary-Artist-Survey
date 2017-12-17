class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = '2bfcf54577559dad34468623d82ca24c8e6da5d4ef5e5e887d79273eb7500f13'
    DATABASE_URI = 'postgres://ydjxpextmymfpr:2bfcf54577559dad34468623d82ca24c8e6da5d4ef5e5e887d79273eb7500f13@ec2-54-' \
                   '163-233-103.compute-1.amazonaws.com:5432/d7okp7kjfvra58'

class DevConfig(BaseConfig):
    DEBUG = True