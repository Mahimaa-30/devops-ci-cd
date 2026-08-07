from app import add_num

def test_add_num():
    assert add_num(2,3) == 5

def test_add_neg():
    assert add_num(-1,1)==0