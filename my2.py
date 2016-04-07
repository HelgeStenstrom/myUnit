#! /usr/bin/env python3

# Från Kent Beck

class TestCase:
	pass

class WasRun(TestCase):
    def __init__(self, name):
    	self.wasRun = False
    	self.name = name

    def testMethod(self):
    	self.wasRun = True

    def run(self):
    	method = getattr(self, self.name)
    	method()
    	


# =====  Unit tests start here ==========

test = WasRun("testMethod")
print(test.wasRun)
test.run()
print(test.wasRun)

