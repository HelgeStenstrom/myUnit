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

test = WasRun("testMethod")
print(test.wasRun)
test.run()
print(test.wasRun)

