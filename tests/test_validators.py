"""Tests for Validators.

Tests the Validator class methods.
"""

from klyor.utils.validators import Validator


def test_email_validation():
    """Test email validation."""
    assert Validator.is_email("test@example.com") is True
    assert Validator.is_email("invalid-email") is False


def test_ip_validation():
    """Test IP validation."""
    assert Validator.is_ip("192.168.1.1") is True
    assert Validator.is_ip("999.999.999.999") is False


def test_domain_validation():
    """Test domain validation."""
    assert Validator.is_domain("example.com") is True
    assert Validator.is_domain("invalid domain") is False


def test_url_validation():
    """Test URL validation."""
    assert Validator.is_url("https://example.com") is True
    assert Validator.is_url("invalid url") is False
