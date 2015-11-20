# -*- coding: utf-8 -*-

"""
Flask server to load setting.py
"""

from flask import Flask
#import settings_prod as app_settings
import settings as app_settings


app = Flask(__name__)
app.config.from_object(app_settings)

import logging.config
logging.config.dictConfig(app_settings.LOGGING)

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    print app.config['SECRET_KEY']
    print app.config['DEBUG']
    port = app.config['PORT']
    logger.info("Server started on port:" + str(port))
    logger.debug('Starting server ...')
    app.run(host='0.0.0.0', port=port)