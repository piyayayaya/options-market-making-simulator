from src.price_process import simulate_price_path
from src.black_scholes import black_scholes_call
from src.greeks import call_delta, call_gamma, call_vega, call_theta


def simulate_option_price_path(
    num_steps=100,
    strike=100,
    volatility=0.20,
    risk_free_rate=0.05,
    time_to_expiry=30 / 365,
    seed=42
):
    stock_prices = simulate_price_path(
        num_steps=num_steps,
        seed=seed
    )

    option_data = []

    for stock_price in stock_prices:

        option_price = black_scholes_call(
            S=stock_price,
            K=strike,
            T=time_to_expiry,
            r=risk_free_rate,
            sigma=volatility
        )

        option_delta = call_delta(
            S=stock_price,
            K=strike,
            T=time_to_expiry,
            r=risk_free_rate,
            sigma=volatility
        )

        option_gamma = call_gamma(
            S=stock_price,
            K=strike,
            T=time_to_expiry,
            r=risk_free_rate,
            sigma=volatility
        )

        option_vega = call_vega(
            S=stock_price,
            K=strike,
            T=time_to_expiry,
            r=risk_free_rate,
            sigma=volatility
        )

        option_theta = call_theta(
            S=stock_price,
            K=strike,
            T=time_to_expiry,
            r=risk_free_rate,
            sigma=volatility
        )

        option_data.append({
            "stock_price": stock_price,
            "option_price": option_price,
            "option_delta": option_delta,
            "option_gamma": option_gamma,
            "option_vega": option_vega,
            "option_theta": option_theta
        })

    return option_data