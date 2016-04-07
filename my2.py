#! /usr/bin/env python3

# Från Kent Beck

class WasRun:
    def __init__(self, name):
    	self.wasRun = False

    def testMethod(self):
    	pass
    	



# Unit tests start here
test = WasRun("testMethod")
print(test.wasRun)
test.testMethod()
print(test.wasRun)

