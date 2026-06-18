import numpy as np


def simulate_price_path(
    initial_price=100,
    volatility=0.02,
    num_steps=100,
    seed=42
):
    np.random.seed(seed)

    prices = [initial_price]

    for _ in range(num_steps):
        price_change = np.random.normal(loc=0, scale=volatility)
        new_price = prices[-1] * (1 + price_change)
        prices.append(new_price)

    return prices