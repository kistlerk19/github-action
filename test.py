def test_simple():
    """A simple test that will always pass."""
    assert True

def add(a, b):
    """Add two numbers and return the result."""
    return a + b

def test_add():
    """Test the add function."""
    assert add(1, 2) == 3
    assert add(5, 7) == 12
    assert add(-1, 1) == 0