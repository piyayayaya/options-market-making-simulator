class OptionMarketMaker:
    def __init__(self, base_spread=0.10):
        self.base_spread = base_spread
        self.option_inventory = 0
        self.stock_inventory = 0
        self.cash = 0

    def calculate_spread(self, option_gamma, option_vega):
        risk_adjustment = 2.0 * abs(option_gamma) + 0.5 * abs(option_vega)
        return self.base_spread + risk_adjustment

    def make_quotes(self, option_fair_value, option_gamma=0, option_vega=0):
        spread = self.calculate_spread(option_gamma, option_vega)

        bid = option_fair_value - spread / 2
        ask = option_fair_value + spread / 2

        return bid, ask, spread

    def buy_from_customer(self, bid):
        self.option_inventory += 1
        self.cash -= bid

    def sell_to_customer(self, ask):
        self.option_inventory -= 1
        self.cash += ask

    def hedge_delta(self, portfolio_delta, stock_price):
        target_stock_inventory = -portfolio_delta
        hedge_trade_size = target_stock_inventory - self.stock_inventory

        self.stock_inventory += hedge_trade_size
        self.cash -= hedge_trade_size * stock_price

        return hedge_trade_size