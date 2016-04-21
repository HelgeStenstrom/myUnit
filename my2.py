#! /usr/bin/env python3
# -*- coding: utf-8 -*.

# Från Kent Beck


import time


class TestCase:
    def __init__(self, name):
        self.name = name

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


class WasRun(TestCase):
    def __init__(self, name):
        TestCase.__init__(self, name)


    def testMethod(self):
        self.wasRun = True
        self.log += "testMethod "

    def setUp(self):
        self.wasRun = False
        self.log = "setUp "


# # =====  Unit tests start here ==========

# class TestCaseTest(TestCase):
#     """Testar mina test case"""

#     def setUp(self):
#         self.test = WasRun("testMethod")

#     def testSetUp(self):
#         self.test.run()
#         assert("setUp testMethod " == self.test.log)

#     def testRunning(self):
#         self.test.run()
#         assert(self.test.wasRun)

#     def testFailNoMsg(self):
#         try:
#             self.fail()
#         except AssertionError:
#             pass
#         else:
#             raise AssertionError

#     def testFailMsg(self):
#         try:
#             self.fail("argument")
#         except AssertionError as e:
#             if e.args[0] != "argument":
#                 raise ValueError("fail(arg) hanterar inte argumentet rätt")
#         else:
#             raise AssertionError


#     def testAssertFaster_tooSlow(self):
#         time.sleep(0.2)
#         try:
#             self.assertFaster(0.1)
#         except TimeoutError:
#             pass
#         else:
#             self.fail("Did not catch too slow execution.")

#     def testAssertFaster_notTooSlow(self):
#         time.sleep(0)
#         try:
#             self.assertFaster(1)
#         except TimeoutError:
#             self.fail("Faulty assertion of slow running time")


# # Lista test att köra

# TestCaseTest("testRunning").run()
# TestCaseTest("testSetUp").run()
# TestCaseTest("testFailNoMsg").run()
# TestCaseTest("testFailMsg").run()
# TestCaseTest("testAssertFaster_tooSlow").run()
# TestCaseTest("testAssertFaster_notTooSlow").run()
# print("end of program")
