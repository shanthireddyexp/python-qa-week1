import pytest


@pytest.mark.sanity
def test_sanity():
    print("This is a sanity test")
    
@pytest.mark.regression
def test_regression(): 
    print("This is a regression test")
    
@pytest.mark.smoke
def test_smoke():
    print("This is a smoke test")
    
@pytest.mark.skip (reason="Test is skipped for demonstration")
def test_skipped():
    print("This test will be skipped")
    