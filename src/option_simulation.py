import numpy as np

from src.option_price_process import simulate_option_price_path
from src.option_market_maker import OptionMarketMaker


def run_option_simulation(num_steps=20, seed=42, hedge_delta=True):
    np.random.seed(seed)

    option_data = simulate_option_price_path(
        num_steps=num_steps,
        seed=seed
    )

    market_maker = OptionMarketMaker(base_spread=0.10)

    trade_log = []

    for row in option_data:

        stock_price = row["stock_price"]
        option_fair_value = row["option_price"]
        option_delta = row["option_delta"]
        option_gamma = row["option_gamma"]
        option_vega = row["option_vega"]
        option_theta = row["option_theta"]

        bid, ask, spread = market_maker.make_quotes(
            option_fair_value,
            option_gamma,
            option_vega
        )

        customer_action = np.random.choice(["buy", "sell", "none"])

        if customer_action == "buy":
            market_maker.sell_to_customer(ask)
            trade_price = ask

        elif customer_action == "sell":
            market_maker.buy_from_customer(bid)
            trade_price = bid

        else:
            trade_price = None

        option_portfolio_delta = market_maker.option_inventory * option_delta
        option_portfolio_gamma = market_maker.option_inventory * option_gamma
        option_portfolio_vega = market_maker.option_inventory * option_vega
        option_portfolio_theta = market_maker.option_inventory * option_theta

        if hedge_delta:
            hedge_trade_size = market_maker.hedge_delta(
                option_portfolio_delta,
                stock_price
            )
        else:
            hedge_trade_size = 0

        total_delta = option_portfolio_delta + market_maker.stock_inventory

        pnl = (
            market_maker.cash
            + market_maker.option_inventory * option_fair_value
            + market_maker.stock_inventory * stock_price
        )

        trade_log.append({
            "stock_price": stock_price,
            "option_fair_value": option_fair_value,
            "option_delta": option_delta,
            "option_gamma": option_gamma,
            "option_vega": option_vega,
            "option_theta": option_theta,
            "spread": spread,
            "bid": bid,
            "ask": ask,
            "customer_action": customer_action,
            "trade_price": trade_price,
            "option_inventory": market_maker.option_inventory,
            "option_portfolio_delta": option_portfolio_delta,
            "option_portfolio_gamma": option_portfolio_gamma,
            "option_portfolio_vega": option_portfolio_vega,
            "option_portfolio_theta": option_portfolio_theta,
            "stock_inventory": market_maker.stock_inventory,
            "hedge_trade_size": hedge_trade_size,
            "total_delta": total_delta,
            "cash": market_maker.cash,
            "pnl": pnl
        })

    return trade_log