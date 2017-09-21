class TestCase:
    def __init__(self, name):
        self.name = name

    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()

    def setUp(self):
        pass


class WasRun(TestCase):
    # Denna klass är inte ett testfall, den är indata till SUT. Men den ser ut som ett testfall.
    def __init__(self, name):
        self.wasRun = None
        super().__init__(name)

    def testMethod(self):
        self.wasRun = 1
        pass

    def setUp(self):
        self.wasSetUp = True
        self.wasRun = None


class TestCaseTest(TestCase):
    def setUp(self):
        self.test = WasRun("testMethod")

    def testRunning(self):
        self.test.run()
        assert(self.test.wasRun)

    def testSetUp(self):
        self.test.run()
        assert self.test.wasSetUp

TestCaseTest("testRunning").run()
TestCaseTest("testSetUp").run()

