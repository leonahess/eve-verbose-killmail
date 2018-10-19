import unittest

# import test modules
from tests.tests_name_fetcher_attacker import TestNameFetcherAttacker
from tests.tests_name_fetcher_victim import TestNameFetcherVictim
from tests.tests_name_fetcher_final_blow import TestNameFetcherFinalBlow
from tests.tests_name_fetcher_geographic import TestNameFetcherGeographic
from tests.tests_killmail import TestKillmail

import sys


def testSuite():
    # initialize the test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # add test to the test suite
    suite.addTest(loader.loadTestsFromTestCase(TestNameFetcherAttacker))
    suite.addTest(loader.loadTestsFromTestCase(TestNameFetcherVictim))
    suite.addTest(loader.loadTestsFromTestCase(TestNameFetcherGeographic))
    suite.addTest(loader.loadTestsFromTestCase(TestNameFetcherFinalBlow))
    suite.addTest(loader.loadTestsFromTestCase(TestKillmail))

    return suite


if __name__ == "__main__":
    # initialize a runner, pass it the suite and run it
    sys.path.append('../src')
    mySuite = testSuite()
    runner = unittest.TextTestRunner(verbosity=3)
    runner.run(mySuite)
