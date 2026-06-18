from pathlib import Path

import numpy as np
import pandas as pd

from src.option_simulation import run_option_simulation
from src.visualization import plot_option_risk_paths


PROJECT_ROOT = Path(__file__).resolve().parent
DATA_DIR = PROJECT_ROOT / "data"

DATA_DIR.mkdir(exist_ok=True)

num_simulations = 500

unhedged_pnls = []
hedged_pnls = []
unhedged_final_deltas = []
hedged_final_deltas = []

for seed in range(num_simulations):

    unhedged_log = run_option_simulation(
        num_steps=50,
        seed=seed,
        hedge_delta=False
    )

    hedged_log = run_option_simulation(
        num_steps=50,
        seed=seed,
        hedge_delta=True
    )

    unhedged_final = unhedged_log[-1]
    hedged_final = hedged_log[-1]

    unhedged_pnls.append(unhedged_final["pnl"])
    hedged_pnls.append(hedged_final["pnl"])

    unhedged_final_deltas.append(abs(unhedged_final["total_delta"]))
    hedged_final_deltas.append(abs(hedged_final["total_delta"]))

comparison_results = pd.DataFrame([
    {
        "strategy": "unhedged",
        "average_final_pnl": np.mean(unhedged_pnls),
        "pnl_standard_deviation": np.std(unhedged_pnls),
        "average_absolute_final_delta": np.mean(unhedged_final_deltas)
    },
    {
        "strategy": "delta_hedged",
        "average_final_pnl": np.mean(hedged_pnls),
        "pnl_standard_deviation": np.std(hedged_pnls),
        "average_absolute_final_delta": np.mean(hedged_final_deltas)
    }
])

comparison_results.to_csv(
    DATA_DIR / "hedged_vs_unhedged_results.csv",
    index=False
)

print(comparison_results)

single_run_log = run_option_simulation(
    num_steps=100,
    seed=42,
    hedge_delta=True
)

plot_option_risk_paths(single_run_log)

print("Saved hedged vs unhedged results to data/hedged_vs_unhedged_results.csv")
print("Saved option risk charts to figures/")