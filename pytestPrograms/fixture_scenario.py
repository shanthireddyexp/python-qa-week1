import pytest


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
    
@pytest.fixture(scope="module")
def module_fixture():
    print("Setup for module fixture")
    yield
    print("Teardown for module fixture") 