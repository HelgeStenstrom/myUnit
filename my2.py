#! /usr/bin/env python3
# -*- coding: utf-8 -*.

# Från Kent Beck

class TestCase:
    def __init__(self, name):
        self.name = name

    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()

    def fail(self, msg=None):
        raise AssertionError(msg)



class WasRun(TestCase):
    def __init__(self, name):
        TestCase.__init__(self, name)


    def testMethod(self):
        self.wasRun = True
        self.log += "testMethod "

    def setUp(self):
        self.wasRun = False
        self.log = "setUp "


# =====  Unit tests start here ==========

class TestCaseTest(TestCase):
    """Testar mina test case"""

    def setUp(self):
        self.test = WasRun("testMethod")

    def testSetUp(self):
        self.test.run()
        assert("setUp testMethod " == self.test.log)

    def testRunning(self):
        self.test.run()
        assert(self.test.wasRun)

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

        



TestCaseTest("testRunning").run()
TestCaseTest("testSetUp").run()
TestCaseTest("testFailNoMsg").run()
TestCaseTest("testFailMsg").run()
print("end of program")
