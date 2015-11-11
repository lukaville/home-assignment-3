# -*- coding: utf-8 -*-

import unittest
import sys

from tests.test_calculator import CalculatorTestCase
from tests.test_calculator import OperatorsTestCase

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(CalculatorTestCase),
        unittest.makeSuite(OperatorsTestCase),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
