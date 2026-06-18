# Options Market Making Simulator

## Overview

This project is a Python-based options market making simulator designed to model how an options market maker manages risk while providing liquidity to customers.

The simulator begins with a stochastic stock price process and builds toward a realistic options market making framework incorporating:

- Black-Scholes option pricing
- Bid-ask market making
- Simulated customer order flow
- Inventory tracking
- Mark-to-market PnL calculation
- Inventory-aware quoting
- Delta hedging
- Dynamic spread adjustment
- Greek risk management (Delta, Gamma, Vega, Theta)

The goal of the project is to understand the tradeoffs between spread capture, inventory risk, directional exposure, and option risk management.

---

## Project Structure

```
options_market_making_simulator/

├── data/
│   └── hedged_vs_unhedged_results.csv
│
├── figures/
│   ├── pnl_vs_skew_strength.png
│   ├── inventory_vs_skew_strength.png
│   ├── total_delta_path.png
│   ├── portfolio_gamma_path.png
│   ├── portfolio_vega_path.png
│   ├── portfolio_theta_path.png
│   ├── stock_hedge_path.png
│   ├── option_pnl_path.png
│   └── dynamic_spread_path.png
│
├── src/
│   ├── black_scholes.py
│   ├── greeks.py
│   ├── price_process.py
│   ├── market_maker.py
│   ├── simulation.py
│   ├── option_market_maker.py
│   ├── option_price_process.py
│   ├── option_simulation.py
│   └── visualization.py
│
├── notes.md
├── README.md
└── main.py
```

---

## Methodology

### 1. Stock Price Simulation

The simulator generates a stochastic stock price path using normally distributed returns.

This provides a changing fair value that the market maker can quote around and introduces uncertainty similar to real financial markets.

---

### 2. Market Making Engine

A market maker continuously quotes:

```
Bid = Fair Value − Spread / 2
Ask = Fair Value + Spread / 2
```

Customer orders are simulated and can:

- Buy from the market maker
- Sell to the market maker
- Do nothing

Each trade updates inventory and cash balances.

---

### 3. Inventory Management

The simulator tracks inventory accumulation resulting from customer flow.

Inventory exposure creates directional risk because the market maker may become excessively long or short.

To reduce this risk, inventory-aware quote skewing is implemented.

Quotes are adjusted to encourage trades that move inventory back toward zero.

---

### 4. PnL Calculation

Mark-to-market PnL is calculated as:

```
PnL = Cash + Inventory Value
```

This demonstrates that spread capture alone does not guarantee profitability.

Inventory risk can create significant losses when prices move against the market maker's position.

---

### 5. Black-Scholes Option Pricing

European call options are priced using the Black-Scholes model.

Inputs include:

- Stock Price
- Strike Price
- Time to Expiration
- Volatility
- Risk-Free Rate

This produces theoretical option values used for quoting.

---

### 6. Option Greeks

The simulator calculates:

### Delta

Measures directional exposure.

```
Delta = ∂Option Price / ∂Stock Price
```

### Gamma

Measures how quickly Delta changes.

```
Gamma = ∂Delta / ∂Stock Price
```

### Vega

Measures volatility exposure.

```
Vega = ∂Option Price / ∂Volatility
```

### Theta

Measures sensitivity to time decay.

```
Theta = ∂Option Price / ∂Time
```

Portfolio-level Greeks are calculated by multiplying each Greek by option inventory.

---

### 7. Delta Hedging

The market maker dynamically hedges option exposure using the underlying stock.

Target hedge:

```
Stock Position = - Portfolio Delta
```

This keeps total portfolio Delta close to zero and significantly reduces directional risk.

---

### 8. Dynamic Spread Adjustment

Option spreads are widened when risk increases.

Spread is adjusted using:

```
Spread =
Base Spread
+ 2 × |Gamma|
+ 0.5 × |Vega|
```

This mimics how market makers widen markets when option risk becomes more difficult to manage.

---

## Results

### Inventory-Aware Quoting

Inventory-aware quoting reduced average inventory exposure relative to fixed quoting while maintaining similar profitability.

### Delta Hedging

Across 500 simulations:

| Strategy | Avg PnL | PnL Std Dev | Avg Absolute Delta |
|-----------|----------|-------------|--------------------|
| Unhedged | 0.89 | 41.98 | 2.37 |
| Delta Hedged | 1.00 | 13.14 | 0.00 |

Delta hedging reduced PnL volatility by roughly 70% while preserving average profitability.

### Dynamic Spread Model

The simulator successfully widened option spreads during periods of elevated Gamma and Vega exposure and narrowed spreads when risk decreased.

---

## Key Takeaways

This project demonstrates several core principles of quantitative market making:

- Spread capture is not sufficient for profitability.
- Inventory management is critical.
- Delta hedging dramatically reduces directional risk.
- Gamma and Vega create risk even when Delta is hedged.
- Dynamic spreads can compensate market makers for elevated risk.
- Risk management and profitability must be balanced simultaneously.

---

## Future Extensions

Potential future improvements include:

- Implied volatility simulation
- Stochastic volatility models
- Multi-option portfolios
- Gamma hedging
- Vega hedging
- Transaction costs
- Order book simulation
- Multiple competing market makers

---

## Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib

---

## Author

Piya Tewari

Independent quantitative finance project exploring market making, option pricing, and risk management.