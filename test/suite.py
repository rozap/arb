import unittest
from main import parse, load_settings



class ParametrizedTestCase(unittest.TestCase):
    """ TestCase classes that want to be parametrized should
        inherit from this class.
    """
    def __init__(self, methodName='runTest', settings=None):
        super(ParametrizedTestCase, self).__init__(methodName)
        self.settings = settings

    @staticmethod
    def parametrize(testcase_klass, settings=None):
        """ Create a suite containing all tests taken from the given
            subclass, passing them the parameter 'param'.
        """
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(testcase_klass)
        suite = unittest.TestSuite()
        for name in testnames:
            suite.addTest(testcase_klass(name, settings=settings))
        return suite


if __name__ == '__main__':
    from exchanges import *
    from watcher import TestWatcher
    from api import *
    
    args = parse()
    settings = load_settings(args.settings)


    suite = unittest.TestSuite()
    suite.addTest(ParametrizedTestCase.parametrize(TestBitstamp, settings = settings))
    suite.addTest(ParametrizedTestCase.parametrize(TestCoinbase, settings = settings))
    suite.addTest(ParametrizedTestCase.parametrize(TestWatcher, settings = settings))
    suite.addTest(ParametrizedTestCase.parametrize(TestBTCE, settings = settings))
    unittest.TextTestRunner().run(suite)