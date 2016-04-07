#! /usr/bin/env python3

# Från Kent Beck

class WasRun:
    def __init__(self, name):
    	self.wasRun = False

    def testMethod(self):
    	self.wasRun = True

    def run(self):
    	self.testMethod()
    	



# =====  Unit tests start here ==========

test = WasRun("testMethod")
print(test.wasRun)
test.run()
print(test.wasRun)

