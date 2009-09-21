from agileday.settings import *
import os.path

current_dir = os.path.dirname(__file__)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

SECRET_KEY = 'deadbeefbadc0ffee'

DATABASE_NAME = os.path.join(current_dir, 'test.db')

TEMPLATE_DIRS = (
    os.path.join(current_dir, '..', 'templates'),
    )

MEDIA_ROOT = os.path.join(current_dir, '..', 'media')

