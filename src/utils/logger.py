# -*- coding: utf-8 -*-

import os,  yaml, logging
from logging import config

class Logger:
    '''System logger'''
    
    def __init__(self):
        #File config
        #logging.config.fileConfig('/opt/esm/etc/logging.conf')
        current_directory = os.path.dirname(os.path.abspath(__file__))
        etc_directory = os.path.join(current_directory, '../etc')
        log_config_file = os.path.join(etc_directory, 'logging.yaml')
        
        log_config = yaml.load(open(log_config_file, 'r'))
        log_config.setdefault('version', 1)
        logging.config.dictConfig(log_config)
        
    def getLogger(self, name):
        return logging.getLogger(name)