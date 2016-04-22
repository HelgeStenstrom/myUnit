#! /usr/bin/env python3
# -*- coding: utf-8 -*.

# Från Kent Beck


import time


class TestCase:
    def __init__(self, name):
        self.name = name
        self.start = None

    def setUp(self):
        pass

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



