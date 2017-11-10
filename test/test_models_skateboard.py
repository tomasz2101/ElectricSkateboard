#!/usr/bin/python3
import models.skateboard as skateboard


class TestClassSkateboard(object):
    def test_skateboard_development_configuration(self):
        skate = skateboard.ClassSkateboard(configuration="development")
        assert isinstance(skate, skateboard.ClassSkateboard)

    def test_skateboard_production_configuration(self):
        print("\nCheck production setup")
        try:
            skateboard.ClassSkateboard(configuration="production")
        except ModuleNotFoundError as e:
            print(e)
