class MarketMaker:
    def __init__(self, spread=0.10, inventory_skew_enabled=True, skew_strength=0.01):
        self.spread = spread
        self.inventory = 0
        self.cash = 0
        self.inventory_skew_enabled = inventory_skew_enabled
        self.skew_strength = skew_strength

    def make_quotes(self, fair_value):
        if self.inventory_skew_enabled:
            inventory_skew = self.inventory * self.skew_strength
        else:
            inventory_skew = 0

        adjusted_fair_value = fair_value - inventory_skew

        bid = adjusted_fair_value - self.spread / 2
        ask = adjusted_fair_value + self.spread / 2

        return bid, ask

    def buy_from_customer(self, bid):
        self.inventory += 1
        self.cash -= bid

    def sell_to_customer(self, ask):
        self.inventory -= 1
        self.cash += ask