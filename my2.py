#! /usr/bin/env python3

# Från Kent Beck

class TestCase:
    def __init__(self, name):
        self.name = name

    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()


class WasRun(TestCase):
    def __init__(self, name):
        TestCase.__init__(self, name)


    def testMethod(self):
        self.wasRun = True

    def setUp(self):
        self.wasRun = False
        self.wasSetUp = True


# =====  Unit tests start here ==========

class TestCaseTest(TestCase):
    """Testar mina test case"""

    def setUp(self):
        self.test = WasRun("testMethod")

    def testSetUp(self):
        self.test.run()
        assert(self.test.wasSetUp)

    def testRunning(self):
        self.test.run()
        assert(self.test.wasRun)



TestCaseTest("testRunning").run()
TestCaseTest("testSetUp").run()

