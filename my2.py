#! /usr/bin/env python3

# Från Kent Beck

class TestCase:
    def __init__(self, name):
        self.name = name

    def run(self):
    	method = getattr(self, self.name)
    	method()
 
class WasRun(TestCase):
    def __init__(self, name):
    	self.wasRun = False
    	TestCase.__init__(self, name)


    def testMethod(self):
    	self.wasRun = True

# =====  Unit tests start here ==========

class TestCaseTest(TestCase):
	"""Testar mina test case"""
	def testRunning(self):
		test = WasRun("testMethod")
		assert(not test.wasRun)
		test.run()
		assert(test.wasRun)



TestCaseTest("testRunning").run()
