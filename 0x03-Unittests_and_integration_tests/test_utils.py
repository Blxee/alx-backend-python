#!/usr/bin/env python3
"""Module for testing functions in utils.py file."""
from parameterized import parameterized
import unittest
from utils import *


class TestAccessNestedMap(unittest.TestCase):
    """Test suit for access_nested_map function."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, map, path, ret):
        """Test access_nested_map"""
        self.assertEqual(access_nested_map(map, path), ret)
