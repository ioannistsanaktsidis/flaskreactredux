import os

DEBUG = True

SQLALCHEMY_TRACK_MODIFICATIONS = False

SQLALCHEMY_DATABASE_URI =  \
    os.environ.get('TESTAPP_SQLALCHEMY_DATABASE_URI', 'sqlite:////tmp/test.db')
