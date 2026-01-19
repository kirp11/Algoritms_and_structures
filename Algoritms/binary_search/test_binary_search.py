from binary_search import binary_search

import pytest


@pytest.mark.parametrize('input_lst,value, expend_result',[
    ( [-10,-9,0, 5, 8,11],8, 4),
    ( [0,5,8,9,10,11],11, 5 ),
    ( [-8,-5,-8,-11,-9,0],20, -1 )
])
def test_positive(input_lst,value,expend_result):
    assert binary_search(input_lst,value) == expend_result


@pytest.mark.parametrize('input_lst,value, expend_result',[
    ( [0,0,0],0, 1 ),
    ( [0],0, 0 ),
    ( [1,1],1, 1 ),
    ( [0,1,2,3,4],2, 2 ),
])
def test_bounds(input_lst,value,expend_result):
    assert binary_search(input_lst,value) == expend_result

@pytest.mark.parametrize('input_lst,value, expend_result',[
    ('',1, ValueError),
    (1, 1, ValueError),
    ('a', 1, ValueError),
    (0, 1, ValueError)
])
def test_negative(input_lst,value,expend_result):
    with pytest.raises(expend_result):
        binary_search(input_lst,value)