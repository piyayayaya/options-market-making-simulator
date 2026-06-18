import math

from src.black_scholes import normal_cdf


def normal_pdf(x):
    return math.exp(-0.5 * x ** 2) / math.sqrt(2 * math.pi)


def calculate_d1(S, K, T, r, sigma):
    return (
        math.log(S / K)
        + (r + 0.5 * sigma ** 2) * T
    ) / (sigma * math.sqrt(T))


def calculate_d2(S, K, T, r, sigma):
    d1 = calculate_d1(S, K, T, r, sigma)
    return d1 - sigma * math.sqrt(T)


def call_delta(S, K, T, r, sigma):
    if T <= 0:
        if S > K:
            return 1
        else:
            return 0

    d1 = calculate_d1(S, K, T, r, sigma)

    return normal_cdf(d1)


def call_gamma(S, K, T, r, sigma):
    if T <= 0:
        return 0

    d1 = calculate_d1(S, K, T, r, sigma)

    gamma = normal_pdf(d1) / (S * sigma * math.sqrt(T))

    return gamma


def call_vega(S, K, T, r, sigma):
    if T <= 0:
        return 0

    d1 = calculate_d1(S, K, T, r, sigma)

    vega = S * normal_pdf(d1) * math.sqrt(T)

    return vega / 100


def call_theta(S, K, T, r, sigma):
    if T <= 0:
        return 0

    d1 = calculate_d1(S, K, T, r, sigma)
    d2 = calculate_d2(S, K, T, r, sigma)

    theta = (
        -S * normal_pdf(d1) * sigma / (2 * math.sqrt(T))
        - r * K * math.exp(-r * T) * normal_cdf(d2)
    )

    return theta / 365