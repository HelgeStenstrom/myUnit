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

class ResultTests(my2.TestCase):
    """Testar mina test case"""

    def setUp(self):
        pass

    def test_init(self):
        result = my2.TestResult()
        self.assertTrue(result.wasSuccessful())
        self.assertEqual(len(result.errors), 0)
        self.assertEqual(len(result.failures), 0)
        self.assertEqual(result.testsRun, 0)
        self.assertEqual(result.shouldStop, False)
        

    # Hur ska jag testa att det finns ett resultat efter körningen?
    # Det skapas ju efter att testSomething() har körts!

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






class AssertTests(my2.TestCase):
    def test_AssertTrue(self):
        "assertTrue should raise an Exception if not True"
        self.assertTrue(True)
        try:
            self.assertTrue(False)
        except AssertionError:
            pass
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

    def test_AssertEqual(self):
        try:
            self.assertEqual(3, 4)
        except AssertionError:
            pass
        else:
            raise AssertionError

        self.assertEqual(3, 3)
        self.assertEqual('a', 'a')
        self.assertEqual(AssertTests, AssertTests)


WasRun("testRunning").run()
WasRun("testSetUp").run()

TestCaseTest("testFailNoMsg").run()
TestCaseTest("testFailMsg").run()

AssertTests("test_AssertFaster_tooSlow").run()
AssertTests("test_AssertFaster_notTooSlow").run()
AssertTests("test_AssertTrue").run()
AssertTests("test_AssertEqual").run()


ResultTests("test_init").run()

print("end of program")
