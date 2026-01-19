from Inversion import inversion

import pytest


@pytest.mark.parametrize('input_lst, expend_result',[
    ( [-10,5,8,11,-9,0], [0,-9,11,8,5,-10] ),
    ( [10,5,8,11,9,0], [0,9,11,8,5,10] ),
    ( [-10,-5,-8,-11,-9,0], [0,-9,-11,-8,-5,-10] )
])
def test_positive(input_lst,expend_result):
    assert inversion(input_lst) == expend_result


@pytest.mark.parametrize('input_lst, expend_result',[
    ( [0,0,0], [0,0,0] ),
    ( [0], [0] ),
    ( [1,1], [1,1] ),
    ( [0,1,2,3,4], [4,3,2,1,0] ),
])
def test_bounds(input_lst,expend_result):
    assert inversion(input_lst) == expend_result

@pytest.mark.parametrize('input_lst, expend_result',[
    ('', ValueError),
    (1, ValueError),
    ('a', ValueError),
    (0, ValueError)
])
def test_negative(input_lst,expend_result):
    with pytest.raises(expend_result):
        inversion(input_lst)