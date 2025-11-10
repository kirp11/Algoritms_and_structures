from shift import shift

import pytest


@pytest.mark.parametrize('input_lst,direction,value, expend_result',[
    ( [-10,5,8,11,-9,0],"right",1, [0,-10,5,8,11,-9] ),
    ( [10,5,8,11,9,0],"right",0, [10,5,8,11,9,0] ),
    ( [-10,-5,-8,-11,-9,0],"right",3, [-11,-9,0,-10,-5,-8] )
])
def test_positive(input_lst,direction,value,expend_result):
    assert shift(input_lst,direction,value) == expend_result


@pytest.mark.parametrize('input_lst,direction,value, expend_result',[
    ( [0,0,0],"right",1, [0,0,0] ),
    ( [0],"right",1, [0] ),
    ( [1,1],"right",1, [1,1] ),
    ( [0,1,2,3,4],"right",1, [4,0,1,2,3] ),
])
def test_bounds(input_lst,direction,value,expend_result):
    assert shift(input_lst,direction,value) == expend_result

@pytest.mark.parametrize('input_lst,direction,value, expend_result',[
    ('', "right",1, ValueError),
    (1, "right",1, ValueError),
    ('a', "right",1, ValueError),
    (0, "right",1, ValueError)
])
def test_negative(input_lst,direction,value,expend_result):
    with pytest.raises(expend_result):
        shift(input_lst,direction,value)