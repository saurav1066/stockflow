"""
Utility functions for stockflow project.
"""

def calculate_wape(y_true: list[float], y_pred: list[float]) -> float:
    """
    Weighted Absolute Percentage Error (WAPE).

    Args:
        y_true: Actual demand values.
        y_pred: Forecasted demand values.

    Returns:
        WAPE score (lower is better).
    """
    numerator = sum(abs(t - p) for t, p in zip(y_true, y_pred))
    denominator = sum(y_true)
    return numerator / denominator if denominator != 0 else float("inf")
