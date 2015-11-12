# -*- coding: utf-8 -*-

import sys
sys.path.append('../')

from calculator import operators
from calculator import calculate
import unittest
from decimal import Decimal


class CalculatorTestCase(unittest.TestCase):
    def test_calculator(self):
        self.assertEqual(calculate("+", 2, 3), 5)

    def test_unsupported_operator(self):
        with self.assertRaises(ValueError):
            calculate("$", 2, 3)

    def test_incorrect_arg_count(self):
        with self.assertRaises(ValueError):
            calculate("mod", 1, 2, 3)

    def test_floats(self):
        self.assertEqual(calculate("+", "0.1", "0.2"), Decimal("0.3"))
        self.assertEqual(calculate("/", "12", "0.1"), Decimal("120"))


class OperatorsTestCase(unittest.TestCase):
    def setUp(self):
        self.add = operators["+"]["function"]
        self.sub = operators["-"]["function"]
        self.mul = operators["*"]["function"]
        self.div = operators["/"]["function"]
        self.mod = operators["%"]["function"]

    def test_add(self):
        self.assertEqual(self.add(4, 2), Decimal(6))
        self.assertAlmostEqual(self.add(4, 2.23), Decimal(6.23))

    def test_sub(self):
        self.assertEqual(self.sub(4, 6), Decimal(-2))
        self.assertAlmostEqual(self.sub(4, 6.23), Decimal(-2.23))

    def test_mul(self):
        self.assertEqual(self.mul(4, 6), Decimal(24))
        self.assertAlmostEqual(self.mul(4, 6.23), Decimal(24.92))

    def test_div(self):
        self.assertEqual(self.div(6, 2), Decimal(3))
        self.assertAlmostEqual(self.div(3, 2), Decimal(1.5))
        with self.assertRaises(ZeroDivisionError):
            self.div(1, 0)

    def test_mod(self):
        self.assertEqual(self.mod(8, 6), Decimal(2))
        self.assertAlmostEqual(self.mod(1.5, 2), Decimal(1.5))
        self.assertNotEqual(self.mod(9.2, 8), Decimal(1.2))
