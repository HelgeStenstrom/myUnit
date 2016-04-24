#! /usr/bin/env python3
# -*- coding: utf-8 -*-   Behövs egentligen inte, men vissa editorer gillar det.

# Från Kent Beck


import my2 as unittest
import time


# =====  Unit tests start here ==========

class WasRun(unittest.TestCase):

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

class TestCaseTest(unittest.TestCase):
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

class AssertTests(unittest.TestCase):
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


class ResultTests(unittest.TestCase):
    """Testar mina test case"""

    def setUp(self):
        pass

    def test_init(self):
        result = unittest.TestResult()
        self.assertTrue(result.wasSuccessful())
        self.assertEqual(len(result.errors), 0)
        self.assertEqual(len(result.failures), 0)
        self.assertEqual(result.testsRun, 0)
        self.assertEqual(result.shouldStop, False)

    # "This method can be called to signal that the set of tests being
    # run should be aborted by setting the TestResult's shouldStop
    # attribute to True."
    def test_stop(self):
        result = unittest.TestResult()

        result.stop()

        self.assertEqual(result.shouldStop, True)

    # "Called when the test case test is about to be run. The default
    # implementation simply increments the instance's testsRun counter."
    def test_startTest(self):
        class Foo(unittest.TestCase):
            def test_1(self):
                pass

        test = Foo('test_1')

        result = unittest.TestResult()

        result.startTest(test)

        self.assertTrue(result.wasSuccessful())
        self.assertEqual(len(result.errors), 0)
        self.assertEqual(len(result.failures), 0)
        self.assertEqual(result.testsRun, 1)
        self.assertEqual(result.shouldStop, False)

        result.stopTest(test)

    # "Called after the test case test has been executed, regardless of
    # the outcome. The default implementation does nothing."
    def test_stopTest(self):
        class Foo(unittest.TestCase):
            def test_1(self):
                pass

        test = Foo('test_1')

        result = unittest.TestResult()

        result.startTest(test)

        self.assertTrue(result.wasSuccessful())
        self.assertEqual(len(result.errors), 0)
        self.assertEqual(len(result.failures), 0)
        self.assertEqual(result.testsRun, 1)
        self.assertEqual(result.shouldStop, False)

        result.stopTest(test)

        # Same tests as above; make sure nothing has changed
        self.assertTrue(result.wasSuccessful())
        self.assertEqual(len(result.errors), 0)
        self.assertEqual(len(result.failures), 0)
        self.assertEqual(result.testsRun, 1)
        self.assertEqual(result.shouldStop, False)

    # "Called before and after tests are run. The default implementation does nothing."
    def test_startTestRun_stopTestRun(self):
        result = unittest.TestResult()
        result.startTestRun()
        result.stopTestRun()




    # Hur ska jag testa att det finns ett resultat efter körningen?
    # Det skapas ju efter att testSomething() har körts!


WasRun("testRunning").run()
WasRun("testSetUp").run()

TestCaseTest("testFailNoMsg").run()
TestCaseTest("testFailMsg").run()

AssertTests("test_AssertFaster_tooSlow").run()
AssertTests("test_AssertFaster_notTooSlow").run()
AssertTests("test_AssertTrue").run()
AssertTests("test_AssertEqual").run()


ResultTests("test_init").run()
ResultTests("test_stop").run()
ResultTests("test_startTest").run()
ResultTests("test_stopTest").run()
ResultTests("test_startTestRun_stopTestRun").run()

print("end of program")
