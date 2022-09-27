import pytest


class TestFunc:
    def setup(self):
        print("setup")

    def teardown(self):
        print("teardown")

    def test_a(self):
        print("a")

    def test_b(self):
        print("b")

if __name__ == '__main__':
    pytest.main(["-vs","t_func.py"])