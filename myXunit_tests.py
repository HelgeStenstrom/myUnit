class WasRun:
    def __init__(self, name):
        self.wasRun = None

    def testMethod(self):
        self.wasRun = 1

    def run(self):
        self.testMethod()

# -----------------------------------------

def test_one():
    # -------------- first unit test ----------
    # Setup
    test = WasRun("testMethod")

    # Pre-condition test
    print(test.wasRun)

    # Exercise
    test.testMethod()

    # Assert
    print(test.wasRun)
    # -------------------------------------------


def test_two():
    # -------------- second unit test ----------
    # Setup
    test = WasRun("testMethod")

    # Pre-condition test
    print(test.wasRun)
    assert not (test.wasRun)

    # Exercise
    test.run()

    # Assert
    print(test.wasRun)
    assert test.wasRun

    # -------------------------------------------

# test_one()
test_two()

