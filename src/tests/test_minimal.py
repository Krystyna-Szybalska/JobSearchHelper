"""Minimal tests."""

def test_import():
    """Test that the package can be imported and is properly set up."""
    from josh import __version__

    assert __version__ != "0.0.0"
