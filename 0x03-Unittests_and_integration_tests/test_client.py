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
    @patch('utils.get_json')
    def test_org(self, mock_get_json, org):
        """Tests org method from GithubOrgClient."""
        GithubOrgClient(org).org()
        mock_get_json.assert_called_once()

    @patch('client.GithubOrgClient.org')
    def test_public_repos_url(self, mock_org):
        """Tests public_repos method from GithubOrgClient."""
        payload = {'repos_url': 12345}
        mock_org.return_value = payload
        client = GithubOrgClient('abc')
        self.assertEqual(client._public_repos_url, payload['repos_url'])

    @patch('utils.get_json')
    def test_public_repos(self, mock_get_json):
        """Tests public_repos method from GithubOrgClient."""
        payload = {'repos_url': 12345}
        mock_get_json.return_value = payload
        client = GithubOrgClient('abc')
        with patch.object(GithubOrgClient, '_public_repos_url') as patched:
            mock_get_json.assert_called_once()


class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Test suit for GithubOrgClient class"""

    def test_public_repos(self):
        """Tests public_repos method from GithubOrgClient."""
        pass

    def test_public_repos_with_license(self):
        """Tests public_repos_with_license method from GithubOrgClient."""
