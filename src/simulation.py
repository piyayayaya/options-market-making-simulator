import numpy as np

from src.price_process import simulate_price_path
from src.market_maker import MarketMaker


def run_simulation(num_steps=20, seed=42, inventory_skew_enabled=True, skew_strength=0.01):
    np.random.seed(seed)

    prices = simulate_price_path(num_steps=num_steps, seed=seed)
    market_maker = MarketMaker(
    spread=0.10,
    inventory_skew_enabled=inventory_skew_enabled,
    skew_strength=skew_strength
    )

    trade_log = []

    for price in prices:
        bid, ask = market_maker.make_quotes(price)

        bid_attractiveness = max(0, bid - price)
        ask_attractiveness = max(0, price - ask)

        prob_customer_sells = 0.30 + bid_attractiveness
        prob_customer_buys = 0.30 + ask_attractiveness
        prob_no_trade = 0.40

        total_prob = prob_customer_sells + prob_customer_buys + prob_no_trade

        prob_customer_sells /= total_prob
        prob_customer_buys /= total_prob
        prob_no_trade /= total_prob

        customer_action = np.random.choice(
            ["sell", "buy", "none"],
            p=[prob_customer_sells, prob_customer_buys, prob_no_trade]
        )

        if customer_action == "buy":
            market_maker.sell_to_customer(ask)
            trade_price = ask

        elif customer_action == "sell":
            market_maker.buy_from_customer(bid)
            trade_price = bid

        else:
            trade_price = None

        trade_log.append({
            "fair_value": price,
            "bid": bid,
            "ask": ask,
            "customer_action": customer_action,
            "trade_price": trade_price,
            "inventory": market_maker.inventory,
            "cash": market_maker.cash, 
            "pnl": market_maker.cash + market_maker.inventory * price
        })

    return trade_log