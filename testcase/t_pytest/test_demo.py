import pytest


def fuc(x):
    return x+1


def test_a():
    print("test_a")
    assert fuc(3)  == 5

@pytest.mark.flaky(reruns=3)
def test_c():
    print("test_c")
    assert fuc(4) == 6

def test_b():
    print("test_b")
    assert 1
#
if __name__ == '__main__':
    # pytest.main(["-s","test_demo.py"])
    pytest.main(["-s"])