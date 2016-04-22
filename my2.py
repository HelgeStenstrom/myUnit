#! /usr/bin/env python3
# -*- coding: utf-8 -*.

# Från Kent Beck


import time


class TestCase:
    def __init__(self, name):
        self.name = name
        self.start = None

    def run(self):
        self.setUp()
        self.start = time.time()
        method = getattr(self, self.name)
        method()

    def fail(self, msg=None):
        raise AssertionError(msg)

    def assertFaster(self, maxTime):
        elapsed  = time.time() - self.start
        if elapsed > maxTime:
            raise TimeoutError

    def assertTrue(self, bool):
        if not bool:
            raise AssertionError


# class WasRun(TestCase):
#     def q__init__(self, name):
#         TestCase.__init__(self, name)


#     def testMethod(self):
#         self.wasRun = True
#         self.log += "testMethod "

#     def setUp(self):
#         self.wasRun = False
#         self.log = "setUp "


