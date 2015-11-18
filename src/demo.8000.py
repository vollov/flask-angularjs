# -*- coding: utf-8 -*-

from flask import Flask
app = Flask(__name__)

from utils.logger import Logger
logger = Logger().getLogger('demo.8000')  

from utils.settings import Configuration
config = Configuration('test')

@app.route('/')
def hello_world():
    logger.debug('calling hello_world()')
    return 'Hello World!'

if __name__ == '__main__':
    port = config.get('server', 'port')
    logger.info("Server started on port:" + port)
    app.run(host='0.0.0.0', port=int(port))
    
    