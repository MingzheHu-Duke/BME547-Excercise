from point_on_line import cal_y
import pytest
import math

@pytest.mark.parametrize('point_1, point_2,,x_value, y', [
((0,1), (1,0), 0.5, 0.5), 
((0,1), (1,0), 0, 1),
((0,1), (1,0), -4, 5), 
((-4, 0), (0, 1), -1, 0.75), 
((-4, 0), (0, 1), 0, 1), 
((-4, 0), (0, 1), -2, 0.5) 
])

def test_cal_y(point_1, point_2, x_value, y):
	assert math.isclose(cal_y(point_1, point_2, x_value), y)
