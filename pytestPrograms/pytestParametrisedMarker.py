import pytest


def get_data():
    return [
        {"pytestuser@domain.com","password123"},
        {"pytestuser2@domain.com","password456"}
    ]
    
@pytest.mark.parametrize("email,password", get_data())
def test_login(email, password):
        print(f"Testing login with email: {email} and password: {password}")