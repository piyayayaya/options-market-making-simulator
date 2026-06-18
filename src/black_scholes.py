import math


def normal_cdf(x):
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


def black_scholes_call(S, K, T, r, sigma):
    if T <= 0:
        return max(S - K, 0)

    d1 = (
        math.log(S / K)
        + (r + 0.5 * sigma ** 2) * T
    ) / (sigma * math.sqrt(T))

    d2 = d1 - sigma * math.sqrt(T)

    call_price = (
        S * normal_cdf(d1)
        - K * math.exp(-r * T) * normal_cdf(d2)
    )

    return call_price