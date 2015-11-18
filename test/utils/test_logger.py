# -*- coding: utf-8 -*-
from utils.logger import Logger
import os, unittest
        
def foo():
    logger = Logger().getLogger(__name__)
    print 'Hello foo()'
    logger.info('Hi, foo')
    
class TestLogger(unittest.TestCase):
   
    def setUp(self):
        self.logger = Logger().getLogger(__name__)
         
    def test_log(self):
        self.logger.debug("debug")
        self.logger.info("info")
        self.logger.warn("warn")
        self.logger.error("error")
        self.logger.critical("critical")
    
def test():
    foo()
    unittest.main()    
    
if __name__ == '__main__': test()