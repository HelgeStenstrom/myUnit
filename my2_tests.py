#! /usr/bin/env python3
# -*- coding: utf-8 -*-   Behövs egentligen inte, men vissa editorer gillar det.

# Från Kent Beck


import my2 as unittest
import time
import sys

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

    def test_AssertFalse(self):
        "assertTrue should raise an Exception if not False"
        self.assertFalse(False)
        try:
            self.assertFalse(True)
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


    # "addSuccess(test)"
    # ...
    # "Called when the test case test succeeds"
    # ...
    # "wasSuccessful() - Returns True if all tests run so far have passed,
    # otherwise returns False"
    # ...
    # "testsRun - The total number of tests run so far."
    # ...
    # "errors - A list containing 2-tuples of TestCase instances and
    # formatted tracebacks. Each tuple represents a test which raised an
    # unexpected exception. Contains formatted
    # tracebacks instead of sys.exc_info() results."
    # ...
    # "failures - A list containing 2-tuples of TestCase instances and
    # formatted tracebacks. Each tuple represents a test where a failure was
    # explicitly signalled using the TestCase.fail*() or TestCase.assert*()
    # methods. Contains formatted tracebacks instead
    # of sys.exc_info() results."
    def test_addSuccess(self):
        class Foo(unittest.TestCase):
            def test_1(self):
                pass

        test = Foo('test_1')

        result = unittest.TestResult()

        result.startTest(test)
        result.addSuccess(test)
        result.stopTest(test)

        self.assertTrue(result.wasSuccessful())
        self.assertEqual(len(result.errors), 0)
        self.assertEqual(len(result.failures), 0)
        self.assertEqual(result.testsRun, 1)
        self.assertEqual(result.shouldStop, False)


    # "addFailure(test, err)"
    # ...
    # "Called when the test case test signals a failure. err is a tuple of
    # the form returned by sys.exc_info(): (type, value, traceback)"
    # ...
    # "wasSuccessful() - Returns True if all tests run so far have passed,
    # otherwise returns False"
    # ...
    # "testsRun - The total number of tests run so far."
    # ...
    # "errors - A list containing 2-tuples of TestCase instances and
    # formatted tracebacks. Each tuple represents a test which raised an
    # unexpected exception. Contains formatted
    # tracebacks instead of sys.exc_info() results."
    # ...
    # "failures - A list containing 2-tuples of TestCase instances and
    # formatted tracebacks. Each tuple represents a test where a failure was
    # explicitly signalled using the TestCase.fail*() or TestCase.assert*()
    # methods. Contains formatted tracebacks instead
    # of sys.exc_info() results."
    def test_addFailure(self):
        class Foo(unittest.TestCase):
            def test_1(self):
                pass

        test = Foo('test_1')
        try:
            test.fail("foo")
        except:
            exc_info_tuple = sys.exc_info()

        result = unittest.TestResult()

        result.startTest(test)
        result.addFailure(test, exc_info_tuple)
        result.stopTest(test)

        self.assertFalse(result.wasSuccessful())
        self.assertEqual(len(result.errors), 0)
        self.assertEqual(len(result.failures), 1)
        self.assertEqual(result.testsRun, 1)
        self.assertEqual(result.shouldStop, False)

        test_case, formatted_exc = result.failures[0]
        self.assertIs(test_case, test)
        self.assertIsInstance(formatted_exc, str)

    # "addError(test, err)"
    # ...
    # "Called when the test case test raises an unexpected exception err
    # is a tuple of the form returned by sys.exc_info():
    # (type, value, traceback)"
    # ...
    # "wasSuccessful() - Returns True if all tests run so far have passed,
    # otherwise returns False"
    # ...
    # "testsRun - The total number of tests run so far."
    # ...
    # "errors - A list containing 2-tuples of TestCase instances and
    # formatted tracebacks. Each tuple represents a test which raised an
    # unexpected exception. Contains formatted
    # tracebacks instead of sys.exc_info() results."
    # ...
    # "failures - A list containing 2-tuples of TestCase instances and
    # formatted tracebacks. Each tuple represents a test where a failure was
    # explicitly signalled using the TestCase.fail*() or TestCase.assert*()
    # methods. Contains formatted tracebacks instead
    # of sys.exc_info() results."
    def test_addError(self):
        class Foo(unittest.TestCase):
            def test_1(self):
                pass

        test = Foo('test_1')
        try:
            raise TypeError()
        except:
            exc_info_tuple = sys.exc_info()

        result = unittest.TestResult()

        result.startTest(test)
        result.addError(test, exc_info_tuple)
        result.stopTest(test)

        self.assertFalse(result.wasSuccessful())
        self.assertEqual(len(result.errors), 1)
        self.assertEqual(len(result.failures), 0)
        self.assertEqual(result.testsRun, 1)
        self.assertEqual(result.shouldStop, False)

        test_case, formatted_exc = result.errors[0]
        self.assertIs(test_case, test)
        self.assertIsInstance(formatted_exc, str)

    def test_addError_locals(self):
        class Foo(unittest.TestCase):
            def test_1(self):
                1/0

        test = Foo('test_1')
        result = unittest.TestResult()
        result.tb_locals = True

        unittest.result.traceback = MockTraceback
        self.addCleanup(restore_traceback)
        result.startTestRun()
        test.run(result)
        result.stopTestRun()

        self.assertEqual(len(result.errors), 1)
        test_case, formatted_exc = result.errors[0]
        self.assertEqual('A tracebacklocals', formatted_exc)


WasRun("testRunning").run()
WasRun("testSetUp").run()

TestCaseTest("testFailNoMsg").run()
TestCaseTest("testFailMsg").run()

AssertTests("test_AssertFaster_tooSlow").run()
AssertTests("test_AssertFaster_notTooSlow").run()
AssertTests("test_AssertTrue").run()
AssertTests("test_AssertFalse").run()
AssertTests("test_AssertEqual").run()


ResultTests("test_init").run()
ResultTests("test_stop").run()
ResultTests("test_startTest").run()
ResultTests("test_stopTest").run()
ResultTests("test_startTestRun_stopTestRun").run()
ResultTests("test_addSuccess").run()
ResultTests("test_addFailure").run()
ResultTests("test_addError").run()
#ResultTests("test_addError_locals").run()

print("end of program")
