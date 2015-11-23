import os, logging

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = 's0%dyyy_6r1!^^dksvnt1u^hpv61-)2(szfhyfo(!b-5z($pym'

DEBUG = True
UNIX = False
PORT = 8000

if UNIX:
    RESOURCE_ROOT='/opt/www/jennyli/'
else:
    RESOURCE_ROOT='c:/opt/var/www/jennyli/'
    
if DEBUG:
    PRESERVE_CONTEXT_ON_EXCEPTION=True
else:
    PRESERVE_CONTEXT_ON_EXCEPTION=False
    
DATABASE_URL = 'mysql://root:justdoit@localhost/flaskr_test'
    
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '[ %(levelname)s ] %(asctime)s - %(message)s'
        },
    },
           
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'debug.logfile': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(RESOURCE_ROOT,'logs/debug.log'),
            'formatter': 'verbose',
        },
        'info.logfile': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(RESOURCE_ROOT,'logs/info.log'),
            'formatter': 'simple',
        },
    },
           
    'loggers': {
        'debug_logger': {
            'handlers': ['debug.logfile', 'console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'info_logger': {
            'handlers': ['info.logfile', 'console'],
            'level': 'INFO',
            'propagate': True,
        },
    },       
}

