#!/usr/bin/env python3
"""Module for testing functions in client.py module"""
from client import GithubOrgClient
from parameterized import parameterized
import unittest
from unittest.mock import patch


class TestGithubOrgClient(unittest.TestCase):
    """Test suit for GithubOrgClient class"""

    @parameterized.expand([
        ('google'),
        ('abc'),
    ])
    def test_org(self, org):
        client = GithubOrgClient(org)
        with patch('utils.get_json') as mock_get_json:
            mock_get_json.assert_called_once()


class TestIntegrationGithubOrgClient(unittest.TestCase):
    def test_public_repos(self):
        pass

    def test_public_repos_with_license(self):
        pass
