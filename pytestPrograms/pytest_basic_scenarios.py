import pytest


def test_login():
    print("This is login test")
    
def test_logout():
    print("This is logout test")
    
def setup_module():
    print("Setup for the entire module")
    
def teardown_module():
    print("Teardown for the entire module")
    
def setup_function():
    print("Setup for each test function")
    
def teardown_function():
    print("Teardown for each test function")
    
@pytest.fixture(scope="function")
def sample_fixture():
    print("Setup for sample fixture")
    yield
    print("Teardown for sample fixture")
    
@pytest.mark.usefixtures("sample_fixture")
def test_sample():
    print("This is a sample test using fixture")    