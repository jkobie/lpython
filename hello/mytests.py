#! /usr/bin/python
#
# Purpose : Print 'Hello World'
# Author  : jkobie@gmail.com
#

import unittest
from mycode import *


class MyFirstTests(unittest.TestCase):
    def test_hello(self):
        hello = Hello();
        self.assertEqual(hello.hello_world(), 'hello world')

if __name__ == '__main__':
    unittest.main()