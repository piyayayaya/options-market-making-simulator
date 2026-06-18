from pathlib import Path
import matplotlib.pyplot as plt


PROJECT_ROOT = Path(__file__).resolve().parent.parent
FIGURES_DIR = PROJECT_ROOT / "figures"

FIGURES_DIR.mkdir(exist_ok=True)


def plot_parameter_sweep(skew_strengths, average_pnls, average_inventories):
    plt.figure()
    plt.plot(skew_strengths, average_pnls, marker="o")
    plt.title("Average PnL vs Inventory Skew Strength")
    plt.xlabel("Skew Strength")
    plt.ylabel("Average Final PnL")
    plt.savefig(FIGURES_DIR / "pnl_vs_skew_strength.png")
    plt.show()

    plt.figure()
    plt.plot(skew_strengths, average_inventories, marker="o")
    plt.title("Average Absolute Inventory vs Inventory Skew Strength")
    plt.xlabel("Skew Strength")
    plt.ylabel("Average Absolute Inventory")
    plt.savefig(FIGURES_DIR / "inventory_vs_skew_strength.png")
    plt.show()


def plot_single_simulation_path(trade_log):
    time_steps = list(range(len(trade_log)))

    fair_values = [row["fair_value"] for row in trade_log]
    inventories = [row["inventory"] for row in trade_log]
    pnls = [row["pnl"] for row in trade_log]

    plt.figure()
    plt.plot(time_steps, fair_values)
    plt.title("Simulated Fair Value Over Time")
    plt.xlabel("Time Step")
    plt.ylabel("Fair Value")
    plt.savefig(FIGURES_DIR / "fair_value_path.png")
    plt.show()

    plt.figure()
    plt.plot(time_steps, inventories)
    plt.title("Market Maker Inventory Over Time")
    plt.xlabel("Time Step")
    plt.ylabel("Inventory")
    plt.savefig(FIGURES_DIR / "inventory_path.png")
    plt.show()

    plt.figure()
    plt.plot(time_steps, pnls)
    plt.title("Market Maker PnL Over Time")
    plt.xlabel("Time Step")
    plt.ylabel("PnL")
    plt.savefig(FIGURES_DIR / "pnl_path.png")
    plt.show()


def plot_option_risk_paths(trade_log):
    time_steps = list(range(len(trade_log)))

    deltas = [row["total_delta"] for row in trade_log]
    gammas = [row["option_portfolio_gamma"] for row in trade_log]
    vegas = [row["option_portfolio_vega"] for row in trade_log]
    thetas = [row["option_portfolio_theta"] for row in trade_log]
    stock_hedges = [row["stock_inventory"] for row in trade_log]
    pnls = [row["pnl"] for row in trade_log]
    spreads = [row["spread"] for row in trade_log]

    plt.figure()
    plt.plot(time_steps, deltas)
    plt.title("Total Delta Over Time")
    plt.xlabel("Time Step")
    plt.ylabel("Total Delta")
    plt.savefig(FIGURES_DIR / "total_delta_path.png")
    plt.show()

    plt.figure()
    plt.plot(time_steps, gammas)
    plt.title("Portfolio Gamma Over Time")
    plt.xlabel("Time Step")
    plt.ylabel("Portfolio Gamma")
    plt.savefig(FIGURES_DIR / "portfolio_gamma_path.png")
    plt.show()

    plt.figure()
    plt.plot(time_steps, vegas)
    plt.title("Portfolio Vega Over Time")
    plt.xlabel("Time Step")
    plt.ylabel("Portfolio Vega")
    plt.savefig(FIGURES_DIR / "portfolio_vega_path.png")
    plt.show()

    plt.figure()
    plt.plot(time_steps, thetas)
    plt.title("Portfolio Theta Over Time")
    plt.xlabel("Time Step")
    plt.ylabel("Portfolio Theta")
    plt.savefig(FIGURES_DIR / "portfolio_theta_path.png")
    plt.show()

    plt.figure()
    plt.plot(time_steps, stock_hedges)
    plt.title("Stock Hedge Position Over Time")
    plt.xlabel("Time Step")
    plt.ylabel("Stock Inventory")
    plt.savefig(FIGURES_DIR / "stock_hedge_path.png")
    plt.show()

    plt.figure()
    plt.plot(time_steps, pnls)
    plt.title("Delta-Hedged Option Market Maker PnL")
    plt.xlabel("Time Step")
    plt.ylabel("PnL")
    plt.savefig(FIGURES_DIR / "option_pnl_path.png")
    plt.show()

    plt.figure()
    plt.plot(time_steps, spreads)
    plt.title("Dynamic Option Spread Over Time")
    plt.xlabel("Time Step")
    plt.ylabel("Spread")
    plt.savefig(FIGURES_DIR / "dynamic_spread_path.png")
    plt.show()