#!/usr/bin/python3
import configuration.config_production as config
from pprint import pprint
import pytest


def test_climb():
    root = "skateboard/src/models"
    assert "skateboard/src/models" in config.climb(root)
    assert "skateboard/src" in config.climb(root)
    assert "skateboard" in config.climb(root)
    assert "" in config.climb(root)


def test_get_repo_name_none():
    pprint(config.get_repo_name("./"))
    with pytest.raises((FileNotFoundError, OSError)):
        config.get_repo_name("")
