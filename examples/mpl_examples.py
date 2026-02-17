"""Generate matplotlib/seaborn example gallery for tidepool theme."""

import matplotlib.pyplot as plt
import seaborn as sns
from data import (
    bar_categories,
    bar_values,
    ci_width,
    cluster_centers,
    cluster_xs,
    cluster_ys,
    corr,
    hist_data,
    line_actual,
    line_forecast,
    scatter_c,
    scatter_x,
    scatter_y,
    t,
    var_labels,
)

import tidepool

tidepool.set_mpl_style()

# ── plot ─────────────────────────────────────────────────────────────
fig, axes = plt.subplots(2, 3, figsize=(15, 9))
fig.suptitle("Tidepool — Matplotlib / Seaborn", y=0.95)

# 1. Histogram
ax = axes[0, 0]
ax.hist(hist_data, bins=25)
ax.set_title("Histogram")
ax.set_xlabel("Value")
ax.set_ylabel("Count")

# 2. Scatter — purpor_r colormap
ax = axes[0, 1]
sc = ax.scatter(scatter_x, scatter_y, c=scatter_c, cmap="purpor_r")
fig.colorbar(sc, ax=ax, shrink=0.8)
ax.set_title("Scatter — purpor_r")
ax.set_xlabel("x")
ax.set_ylabel("y")

# 3. Horizontal bar — longest at top
ax = axes[0, 2]
colors = [tidepool.COLORWAY[i] for i in range(len(bar_categories))]
ax.barh(bar_categories, bar_values, color=colors)
ax.set_title("Horizontal Bar")
ax.set_xlabel("Value")

# 4. Clustering scatter
ax = axes[1, 0]
for i in range(len(cluster_centers)):
    ax.scatter(cluster_xs[i], cluster_ys[i], label=f"Cluster {i + 1}")
ax.set_title("Clustering Scatter")
ax.legend(ncol=2, loc="lower right")

# 5. Heatmap — tealrose
ax = axes[1, 1]
sns.heatmap(
    corr,
    cmap="tealrose",
    center=0,
    vmin=-1,
    vmax=1,
    ax=ax,
    square=True,
    cbar_kws={"shrink": 0.8},
    xticklabels=var_labels,
    yticklabels=var_labels,
)
ax.set_title("Correlation — tealrose")

# 6. Lines with confidence intervals
ax = axes[1, 2]
(l1,) = ax.plot(t, line_actual, label="A")
ax.fill_between(
    t,
    line_actual - ci_width,
    line_actual + ci_width,
    color=l1.get_color(),
    alpha=0.15,
)
(l2,) = ax.plot(t, line_forecast, label="B")
ax.fill_between(
    t,
    line_forecast - ci_width * 0.8,
    line_forecast + ci_width * 0.8,
    color=l2.get_color(),
    alpha=0.15,
)
ax.set_title("Lines with CI")
ax.set_xlabel("Time")
ax.set_xlim(0)
ax.grid(visible=True)
ax.legend()

plt.tight_layout(rect=(0, 0, 1, 0.94))
plt.savefig("examples/images/mpl_gallery.png")
plt.close()
print("Saved examples/images/mpl_gallery.png")
