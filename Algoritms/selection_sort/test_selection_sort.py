
from selection_sort import selection_sort

import pytest


@pytest.mark.parametrize('input_data, expend_result',[
    ( [-10,5,8,11,-9,0], [-10,-9,0,5,8,11] ),
    ( [10,5,8,11,9,0], [0,5,8,9,10,11] ),
    ( [-10,-5,-8,-11,-9,0], [-11,-10,-9,-8,-5,0] )
])
def test_positive(input_data,expend_result):
    assert selection_sort(input_data) == expend_result


@pytest.mark.parametrize('input_data, expend_result',[
    ( [0,0,0], [0,0,0] ),
    ( [0], [0,] ),
    ( [1,1], [1,1] ),
    ( [0,1,2,3,4], [0,1,2,3,4] ),
])
def test_bounds(input_data,expend_result):
    assert selection_sort(input_data) == expend_result

@pytest.mark.parametrize('input_data, expend_result',[
    ('', ValueError),
    (1, ValueError),
    ('a', ValueError),
    (0, ValueError)
])
def test_negative(input_data,expend_result):
    with pytest.raises(expend_result):
        selection_sort(input_data)