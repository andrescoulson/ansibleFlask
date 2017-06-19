#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/projects/ormucoFlask/app")

from index import app as application
application.secret_key = '3205829846'