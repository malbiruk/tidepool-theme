"""Shared synthetic data for gallery examples.

Seeded for reproducibility — both mpl and plotly galleries render the same data.
"""

import numpy as np

rng = np.random.default_rng(42)

# ── histogram ────────────────────────────────────────────────────────
hist_data = rng.normal(170, 10, 500)

# ── scatter (colormap) ──────────────────────────────────────────────
n_scatter = 300
scatter_x = rng.normal(0, 1, n_scatter)
scatter_y = scatter_x * 0.8 + rng.normal(0, 0.5, n_scatter)
scatter_c = (
    scatter_x**2 + scatter_y**2 + np.random.default_rng(99).exponential(0.8, n_scatter)
)

# ── horizontal bar ──────────────────────────────────────────────────
bar_categories = ["C", "A", "E", "B", "D", "F"]
bar_values = [6, 8, 10, 11, 12, 15]

# ── clustering scatter ──────────────────────────────────────────────
cluster_centers = [(-3, 3), (0, -2), (3, 3), (-2, -3), (4, -1), (1, 4)]
cluster_xs, cluster_ys = [], []
for cx, cy in cluster_centers:
    cluster_xs.append(rng.normal(cx, 0.6, 60))
    cluster_ys.append(rng.normal(cy, 0.6, 60))

# ── heatmap / correlation ───────────────────────────────────────────
n_vars = 10
var_labels = [f"V{i}" for i in range(n_vars)]
raw = rng.normal(0, 1, (200, n_vars))
for i in range(1, n_vars):
    raw[:, i] += raw[:, i - 1] * 0.35
raw[:, 5] = -raw[:, 2] * 0.8 + rng.normal(0, 0.5, 200)
raw[:, 8] = -raw[:, 1] * 0.7 + rng.normal(0, 0.6, 200)
raw[:, 9] = -raw[:, 3] * 0.5 + rng.normal(0, 0.7, 200)
corr = np.corrcoef(raw.T)

# ── lines with confidence intervals ─────────────────────────────────
t = np.linspace(0, 12, 100)
line_actual = np.cumsum(rng.normal(0.05, 0.3, 100))
line_forecast = np.cumsum(rng.normal(0.04, 0.25, 100))
ci_width = 0.3 + rng.uniform(0, 0.4, 100)
