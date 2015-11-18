# -*- coding: utf-8 -*-
from utils.settings import Configuration
import os, unittest, ConfigParser
        
class TestConfiguration(unittest.TestCase):
   
    def setUp(self):
         self.config = Configuration('test')
         
    def test_config_value(self):
        port = self.config.get('server', 'port')
        expected_port = '8000'
        self.assertEqual(port, expected_port, 'port should be ' + expected_port)
        
if __name__ == '__main__': unittest.main()