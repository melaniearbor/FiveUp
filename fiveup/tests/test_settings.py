import pytest
from django.core.exceptions import ImproperlyConfigured
from settings.base import get_env_variable


def test_get_env_variable():
    """
    A weird environment variable should raise an exception.
    """

    with pytest.raises(ImproperlyConfigured):
        get_env_variable("brrp")
