"""
Core logic for stockflow project.
Example: Simple demand forecasting stub.
"""

import numpy as np


def moving_average_forecast(data: list[float], window: int = 3) -> float:
    """
    Simple moving average forecast.

    Args:
        data: List of historical demand values.
        window: Number of past values to average.

    Returns:
        Forecasted demand (float).
    """
    if len(data) < window:
        raise ValueError("Not enough data for the given window size.")
    return float(np.mean(data[-window:]))
