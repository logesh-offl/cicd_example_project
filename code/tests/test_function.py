from src.math_function import add,sub

def test_add():
    assert add(2,3)==5
    assert add(1,1)==2
    
def test_sub():
    assert sub(2,1)==1
    assert sub(5,1)==4


