#!/usr/bin/env python3
"""Module for testing functions in utils.py file."""
from parameterized import parameterized
import unittest
from unittest.mock import Mock, patch
from utils import *


class TestAccessNestedMap(unittest.TestCase):
    """Test suit for access_nested_map function."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, map, path, ret):
        """Test access_nested_map."""
        self.assertEqual(access_nested_map(map, path), ret)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b"),
    ])
    def test_access_nested_map_exception(self, map, path, err):
        """Test access_nested_map exception."""
        with self.assertRaises(KeyError, msg=f"'{err}'"):
            access_nested_map(map, path)


class TestGetJson(unittest.TestCase):
    """Test suit for get_json function."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, payload, mock_get):
        mock_json = Mock()
        mock_json.json.return_value = payload
        mock_get.return_value = mock_json
        get_json(test_url)
        mock_get.asset_called_once()
