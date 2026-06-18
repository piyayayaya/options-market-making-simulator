# Options Market Making Simulator Project Notes

## Project Goal

The objective of this project is to build a realistic market-making simulator and gradually introduce the core concepts used by quantitative trading firms. The project begins with a simple stock market maker and evolves into an options market-making framework incorporating inventory management, risk control, option pricing, Greek risk measurement, and dynamic hedging.

---

# Part I: Stock Market Making

## Phase 1: Simulating the Underlying Market

The first step was creating a stochastic stock price process.

I modeled stock prices using normally distributed random returns so that fair value would evolve unpredictably through time. This created a simulated market environment in which a market maker could operate.

### Key Insight

A market maker does not control the market price. It must continuously react to an external fair value that changes over time.

---

## Phase 2: Building a Basic Market Maker

After creating the underlying price process, I implemented a basic market maker.

The market maker continuously quotes:

* Bid = Fair Value − Spread / 2
* Ask = Fair Value + Spread / 2

using a fixed spread around the current fair value.

### Key Insight

The market maker's fundamental source of revenue is spread capture: buying below fair value and selling above fair value.

---

## Phase 3: Customer Order Flow

I introduced simulated customer trading activity.

Customers could:

* Buy from the market maker
* Sell to the market maker
* Do nothing

Each trade updated inventory and cash balances.

### Key Insight

Market makers cannot control customer behavior. They must manage whatever positions customer flow creates.

---

## Phase 4: Mark-to-Market PnL

I implemented mark-to-market profit and loss tracking.

PnL was calculated as:

PnL = Cash + Inventory × Current Fair Value

This incorporated both realized and unrealized gains and losses.

### Key Insight

Collecting the spread does not guarantee profitability. Inventory risk can overwhelm spread revenue.

---

## Phase 5: Inventory Risk

During testing, I observed situations where customers repeatedly bought shares from the market maker.

As a result:

* Inventory became increasingly negative
* Cash increased from selling stock
* Stock prices continued rising

Although the market maker collected spreads, the short inventory position lost value and produced negative mark-to-market PnL.

### Key Insight

Inventory risk is one of the central challenges of market making.

---

## Phase 6: Inventory-Aware Quoting

To reduce inventory risk, I implemented inventory-aware quoting.

The market maker adjusts quoted prices according to inventory:

When inventory is too positive:

* Quotes shift downward
* Customers are encouraged to buy

When inventory is too negative:

* Quotes shift upward
* Customers are encouraged to sell

The objective is to naturally move inventory back toward zero.

### Key Insight

Market makers manage inventory through pricing rather than simply accepting whatever positions customers create.

---

## Phase 7: Realistic Customer Response

Initially, inventory-aware quoting produced little improvement.

The reason was that customer behavior remained completely random and independent of price.

To address this, I modified customer order probabilities so they respond to quote attractiveness:

* Higher bids increase the probability that customers sell
* Lower asks increase the probability that customers buy

### Key Insight

Price adjustments only matter if customer behavior responds to those prices.

---

## Phase 8: Comparing Quoting Strategies

I added a configuration switch that allows the simulator to run either:

* Fixed quoting
* Inventory-aware quoting

This enabled controlled experiments comparing different market-making approaches.

### Key Insight

Strategies should be evaluated empirically rather than assumed to be effective.

---

## Phase 9: Large-Scale Simulation Testing

I ran 500 independent simulations to compare fixed and inventory-aware quoting.

Results showed:

* Inventory-aware quoting reduced inventory exposure
* Inventory-aware quoting slightly reduced profitability

### Key Insight

Risk reduction often comes at the cost of reduced expected profit.

---

## Phase 10: Parameter Sweep

I introduced a skew-strength parameter that controls how aggressively quotes respond to inventory.

For each skew value, I measured:

* Average final PnL
* Average absolute inventory

### Results

As skew strength increased:

* Inventory exposure decreased
* Profitability decreased

### Key Insight

Inventory management involves a tradeoff between risk reduction and spread capture.

---

## Phase 11: Visualization

I built visualization tools to analyze simulator behavior.

Generated plots included:

* Average PnL versus skew strength
* Average inventory versus skew strength
* Fair value path
* Inventory path
* PnL path

### Key Insight

Visualization often reveals relationships that are difficult to identify from numerical outputs alone.

---

# Part II: Options Market Making

## Phase 12: Black-Scholes Option Pricing

After completing the stock market-making framework, I added option pricing.

Using the simulated stock path, I calculated call option values using the Black-Scholes model.

Inputs included:

* Stock price
* Strike price
* Time to expiration
* Volatility
* Risk-free rate

This generated a dynamic option fair-value path.

### Key Insight

Options derive their value from the underlying stock and can be continuously repriced as market conditions change.

---

## Phase 13: Option Market Making

I extended the market maker from stocks to options.

The simulator now:

* Quotes bid and ask prices around theoretical option values
* Simulates customer option trades
* Tracks option inventory
* Tracks option cash flows
* Calculates option mark-to-market PnL

### Key Insight

Option inventory risk is nonlinear because option values respond convexly to stock price movements.

---

## Phase 14: Delta Tracking

I implemented Black-Scholes Delta calculations.

Portfolio Delta was computed as:

Portfolio Delta = Option Inventory × Option Delta

This converted option inventory into an equivalent stock exposure.

### Key Insight

Even a seemingly small option position can create substantial directional exposure.

---

## Phase 15: Delta Hedging

I introduced dynamic delta hedging.

The simulator trades stock inventory according to:

Stock Position = − Portfolio Delta

This keeps total portfolio Delta approximately zero.

PnL calculations were expanded to include both:

* Option inventory
* Stock hedge inventory

### Key Insight

Delta hedging removes most directional risk while preserving spread revenue.

---

## Phase 16: Hedged vs Unhedged Analysis

I compared hedged and unhedged option market making across 500 simulations.

### Results

Unhedged:

* Average Final PnL ≈ 0.89
* PnL Standard Deviation ≈ 41.98
* Average Absolute Delta ≈ 2.37

Delta Hedged:

* Average Final PnL ≈ 1.00
* PnL Standard Deviation ≈ 13.14
* Average Absolute Delta ≈ 0.00

### Key Insight

Delta hedging dramatically reduced risk without materially reducing expected profitability.

---

## Phase 17: Gamma Tracking

I added Gamma calculations to the simulator.

Portfolio Gamma was computed by multiplying option Gamma by option inventory.

Gamma measures how quickly Delta changes as the stock price moves.

### Key Insight

A portfolio can be perfectly Delta-neutral while still carrying substantial Gamma risk.

---

## Phase 18: Vega Tracking

I added Vega calculations.

Portfolio Vega measures sensitivity to volatility changes.

### Key Insight

Delta hedging removes directional exposure but does not eliminate volatility risk.

A short option portfolio typically carries negative Vega exposure.

---

## Phase 19: Theta Tracking

I implemented Theta calculations.

Theta measures the effect of time decay on option values.

For short call inventory:

* Theta becomes positive
* Time decay benefits the market maker

### Key Insight

Option market makers often earn positive Theta while managing other forms of risk.

---

## Phase 20: Dynamic Spread Adjustment

I introduced risk-sensitive option spreads.

Instead of using a fixed spread, the simulator widens spreads when risk increases.

Spread is calculated as:

Spread = Base Spread + 2 × |Gamma| + 0.5 × |Vega|

### Key Insight

Real market makers demand additional compensation when managing greater risk.

---

## Phase 21: Greek Risk Visualization

I created visualizations for:

* Total Delta
* Portfolio Gamma
* Portfolio Vega
* Portfolio Theta
* Stock hedge inventory
* Dynamic option spreads
* Delta-hedged option PnL

These visualizations provide a detailed view of how risk evolves through time.

### Key Insight

Risk management is a dynamic process involving continuous monitoring of multiple exposures simultaneously.

---

# Current Status

The simulator currently includes:

### Stock Market Making

* Stochastic stock price simulation
* Bid/ask quoting
* Customer order flow
* Inventory tracking
* Cash tracking
* Mark-to-market PnL
* Inventory-aware quoting
* Quote-sensitive customer behavior
* Parameter optimization
* Strategy comparison
* Visualization tools

### Options Market Making

* Black-Scholes option pricing
* Option bid/ask quoting
* Option inventory tracking
* Option PnL tracking
* Delta calculations
* Delta hedging
* Gamma tracking
* Vega tracking
* Theta tracking
* Dynamic spread adjustment
* Risk visualization
* Hedged versus unhedged analysis

The simulator now captures many of the core ideas used by professional options market makers, including inventory management, dynamic hedging, Greek risk monitoring, and risk-adjusted quoting.
