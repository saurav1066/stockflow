import pytest
from stockflow.core import moving_average_forecast

def test_moving_average_forecast_basic():
    data = [10, 20, 30, 40, 50]
    result = moving_average_forecast(data, window=3)
    assert result == pytest.approx(40.0)  # mean of [30, 40, 50]

def test_moving_average_forecast_small_window():
    data = [5, 10]
    with pytest.raises(ValueError):
        moving_average_forecast(data, window=3)
