#! /usr/bin/env python3
# -*- coding: utf-8 -*-   Behövs egentligen inte, men vissa editorer gillar det.

# Från Kent Beck


import my2
import time


# =====  Unit tests start here ==========

class WasRun(my2.TestCase):

    def testMethod(self):
        self.wasRun = True
        self.log += "testMethod "

    def setUp(self):
        self.test = WasRun("testMethod")
        self.wasRun = False
        self.log = "setUp "

    def testSetUp(self):
        self.test.run()
        assert("setUp testMethod " == self.test.log)

    def testRunning(self):
        self.test.run()
        assert(self.test.wasRun)


class TestCaseTest(my2.TestCase):
    """Testar mina test case"""

    def testFailNoMsg(self):
        try:
            self.fail()
        except AssertionError:
            pass
        else:
            raise AssertionError

    def testFailMsg(self):
        try:
            self.fail("argument")
        except AssertionError as e:
            if e.args[0] != "argument":
                raise ValueError("fail(arg) hanterar inte argumentet rätt")
        else:
            raise AssertionError


    def test_AssertFaster_tooSlow(self):
        time.sleep(0.2)
        try:
            self.assertFaster(0.1)
        except TimeoutError:
            pass
        else:
            self.fail("Did not catch too slow execution.")

    def test_AssertFaster_notTooSlow(self):
        time.sleep(0.01)
        try:
            self.assertFaster(0.1)
        except TimeoutError:
            self.fail("Faulty assertion of slow running time")


    def test_AssertTrue(self):
        "assertTrue should raise an Exception if not True"
        self.assertTrue(True)
        try:
            self.assertTrue(False)
        except AssertionError:
            pass
        else:
            raise AssertionError


WasRun("testRunning").run()
WasRun("testSetUp").run()

TestCaseTest("testFailNoMsg").run()
TestCaseTest("testFailMsg").run()
TestCaseTest("test_AssertFaster_tooSlow").run()
TestCaseTest("test_AssertFaster_notTooSlow").run()
TestCaseTest("test_AssertTrue").run()

print("end of program")
