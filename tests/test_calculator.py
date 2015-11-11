# -*- coding: utf-8 -*-

import sys
sys.path.append('../')

from calculator import operators
from calculator import calculate
import unittest


class OperatorsTestCase(unittest.TestCase):
    def setUp(self):
        self.add = operators["+"]["function"]
        self.sub = operators["-"]["function"]
        self.mul = operators["*"]["function"]
        self.div = operators["/"]["function"]
        self.mod = operators["%"]["function"]

    def test_add(self):
        self.assertEqual(self.add(4, 2), 6)
        self.assertAlmostEqual(self.add(4, 2.23), 6.23)

    def test_sub(self):
        self.assertEqual(self.sub(4, 6), -2)
        self.assertAlmostEqual(self.sub(4, 6.23), -2.23)

    def test_mul(self):
        self.assertEqual(self.mul(4, 6), 24)
        self.assertAlmostEqual(self.mul(4, 6.23), 24.92)

    def test_div(self):
        self.assertEqual(self.div(6, 2), 3)
        self.assertAlmostEqual(self.div(3, 2), 1.5)

    def test_mod(self):
        self.assertEqual(self.mod(8, 6), 2)
        self.assertAlmostEqual(self.mod(9.2, 8), 1.19999999)
