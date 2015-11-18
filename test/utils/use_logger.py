# -*- coding: utf-8 -*-

"""
file to show how to use logger
"""
from utils.logger import Logger
import os

def foo():  
    logger = Logger().getLogger('utils.use_logger.foo')  
    print 'Hello foo()'
    logger.info('Hi, foo')
    
class Bar():
   
    def __init__(self):
        print 'Bar init()'
        self.logger = Logger().getLogger('utils.use_logger.Bar')
         
    def test_log(self):
        print 'Bar test_log()'
        self.logger.debug("debug")
        self.logger.info("info")
        self.logger.warn("warn")
        self.logger.error("error")
        self.logger.critical("critical")
    
def test():
    foo()
    bar = Bar()
    bar.test_log()    
    
if __name__ == '__main__': test()