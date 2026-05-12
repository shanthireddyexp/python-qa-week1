import pytest
import re  # Add this import


def test_assert():
    assert 1 == 1
    assert 2 == 2
    assert 3 == 3
    
def test_assert_false():    
    assert 1 != 2
    assert 2 != 3   
    
def test_assert_true():    
    assert 1 < 2
    assert 2 < 3
    
def test_assert_in():
    assert 'a' in 'abc'
    assert 'b' in 'abc'
    assert 'c' in 'abc'
    
def test_assert_not_in():
    assert 'd' not in 'abc'
    assert 'e' not in 'abc'
    assert 'f' not in 'abc'
    
def test_assert_is():
    a = [1, 2, 3]
    b = a
    assert a is b
    
def test_assert_is_not():
    a = [1, 2, 3]
    b = [1, 2, 3]
    assert a is not b
    
def test_assert_raises():    
    with pytest.raises(ZeroDivisionError):
        1 / 0  
        
def test_assert_raises_message():    
    with pytest.raises(ValueError, match=re.escape("invalid literal for int() with base 10: 'abc'")):  # ✅ Fixed
        int('abc') 
        
def test_assert_almost_equal():
    assert 0.1 + 0.2 == pytest.approx(0.3)
    
def test_assert_not_almost_equal():
    assert 0.1 + 0.2 != pytest.approx(0.4)
    
def test_assert_greater():
    assert 3 > 2
    assert 2 > 1
    
def test_assert_less():
    assert 1 < 2
    assert 2 < 3
    
def test_assert_greater_equal():
    assert 3 >= 2
    assert 2 >= 2
    
def test_assert_less_equal():
    assert 1 <= 2
    assert 2 <= 2

def test_assert_is_instance():
    assert isinstance(1, int)
    assert isinstance("hello", str)
    assert isinstance([1, 2, 3], list)
    
def test_assert_not_is_instance():
    assert not isinstance(1, str)
    assert not isinstance("hello", int)
    assert not isinstance([1, 2, 3], dict)
    
def test_assert_withmessage():
    assert 1 == 1, "This should not fail"
    assert 2 == 2, "This should not fail"
    assert 3 == 3, "This should not fail"