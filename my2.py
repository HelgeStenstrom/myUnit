#! /usr/bin/env python3
# -*- coding: utf-8 -*.

# Från Kent Beck


import time

class TestResult(object):

    def __init__(self):
        self.errors = []
        self.failures = []
        self.testsRun = 0
        self.shouldStop = False

    def wasSuccessful(self):
        return len(self.failures) == 0

    def stop(self):
        self.shouldStop = True

    def startTest(self, test):
        self.testsRun += 1

    def stopTest(self, test):
        pass

    def startTestRun(self):
        pass

    def stopTestRun(self):
        pass

    def addSuccess(self, test):
        pass

    def addFailure(self, test, exc_info_tuple):
        self.failures += [(test, exc_info_tuple)]


    def addError(self, test, exc_info_tuple):
        pass

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

    def assertTrue(self, maybeTrue):
        if not maybeTrue:
            raise AssertionError

    def assertFalse(self, b):
        if not b == False:
            raise AssertionError

    def assertEqual(self, a, b, msg=None):
        if a != b:
            raise AssertionError

    def assertIs(self, a, b):
        pass

    def assertIsInstance(self, a, b):
        pass
    
