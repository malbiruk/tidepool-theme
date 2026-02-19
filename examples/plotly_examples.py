"""Generate plotly example gallery for tidepool theme.

Uses the same data as mpl_examples.py for direct comparison.
"""

import numpy as np
import plotly.graph_objects as go
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
from plotly.subplots import make_subplots

import tidepool

tidepool.set_plotly_template()

# ── plot ─────────────────────────────────────────────────────────────
fig = make_subplots(
    rows=2,
    cols=3,
    subplot_titles=(
        "Histogram",
        "Scatter — purpor_r",
        "Horizontal Bar",
        "Clustering Scatter",
        "Correlation — tealrose",
        "Lines with CI",
    ),
    horizontal_spacing=0.06,
    vertical_spacing=0.14,
)

# 1. Histogram
fig.add_trace(
    go.Histogram(
        x=hist_data,
        xbins={"start": 140, "end": 200, "size": (200 - 140) / 25},
        showlegend=False,
    ),
    row=1,
    col=1,
)

# 2. Scatter — purpor_r
fig.add_trace(
    go.Scatter(
        x=scatter_x,
        y=scatter_y,
        mode="markers",
        marker={"color": scatter_c, "colorscale": "purpor_r"},
        showlegend=False,
    ),
    row=1,
    col=2,
)

# 3. Horizontal bar — longest at top
fig.add_trace(
    go.Bar(
        y=bar_categories,
        x=bar_values,
        orientation="h",
        marker_color=tidepool.COLORWAY[:6],
        showlegend=False,
    ),
    row=1,
    col=3,
)

# 4. Clustering scatter — explicit colors to match mpl (plotly colorway is global)
for i in range(len(cluster_centers)):
    fig.add_trace(
        go.Scatter(
            x=cluster_xs[i],
            y=cluster_ys[i],
            mode="markers",
            marker={"color": tidepool.COLORWAY[i]},
            name=f"Cluster {i + 1}",
            showlegend=False,
        ),
        row=2,
        col=1,
    )

# 5. Heatmap — tealrose
fig.add_trace(
    go.Heatmap(
        z=corr,
        x=var_labels,
        y=var_labels,
        colorscale="Tealrose",
        zmid=0,
        zmin=-1,
        zmax=1,
        showscale=False,
    ),
    row=2,
    col=2,
)

# 6. Comparison lines with CI — explicit colors (plotly colorway is global)
_line_colors = [tidepool.COLORWAY[0], tidepool.COLORWAY[1]]
_ci_alphas = ["rgba(32,178,170,0.15)", "rgba(255,160,122,0.15)"]
for line_y, ci_mult, name, color, ci_fill in [
    (line_actual, 1.0, "A", _line_colors[0], _ci_alphas[0]),
    (line_forecast, 0.8, "B", _line_colors[1], _ci_alphas[1]),
]:
    fig.add_trace(
        go.Scatter(
            x=np.concatenate([t, t[::-1]]),
            y=np.concatenate(
                [line_y + ci_width * ci_mult, (line_y - ci_width * ci_mult)[::-1]],
            ),
            fill="toself",
            fillcolor=ci_fill,
            line={"width": 0},
            showlegend=False,
        ),
        row=2,
        col=3,
    )
    fig.add_trace(
        go.Scatter(
            x=t,
            y=line_y,
            mode="lines",
            name=name,
            line={"color": color},
        ),
        row=2,
        col=3,
    )

# Fix bar order (longest at top)
fig.update_yaxes(
    categoryorder="array",
    categoryarray=bar_categories,
    row=1,
    col=3,
)

# Flip heatmap y-axis (V0 at top, matching seaborn)
fig.update_yaxes(autorange="reversed", row=2, col=2)

# Axis labels (matching mpl)
fig.update_xaxes(title_text="Value", row=1, col=1)
fig.update_yaxes(title_text="Count", row=1, col=1)
fig.update_xaxes(title_text="x", row=1, col=2)
fig.update_yaxes(title_text="y", row=1, col=2)
fig.update_xaxes(title_text="Value", row=1, col=3)
fig.update_xaxes(title_text="Time", row=2, col=3)

# Enable grid on Lines with CI subplot for comparison
fig.update_xaxes(showgrid=True, row=2, col=3)
fig.update_yaxes(showgrid=True, row=2, col=3)

fig.update_layout(
    height=700,
    width=1200,
    title_text="Tidepool — Plotly",
    legend={"x": 0.725, "y": 0.43, "xanchor": "left", "yanchor": "top"},
)

fig.write_image("examples/images/plotly_gallery.png", scale=2)

# Drop fixed dimensions so the HTML adapts to the browser window
fig.update_layout(width=None, height=None)
html_path = "docs/plotly_gallery.html"
fig.write_html(html_path, include_plotlyjs="cdn", config=tidepool.PLOTLY_CONFIG)

print("Saved examples/images/plotly_gallery.png")
print(f"Saved {html_path}")
