# tidepool

A light, minimal plotting theme with soft coastal colors and serif typography.
Available for both **matplotlib/seaborn** and **plotly**.

## Gallery

### Matplotlib / Seaborn

![Matplotlib gallery](examples/images/mpl_gallery.png)

### Plotly

![Plotly gallery](examples/images/plotly_gallery.png)

**[Interactive version](https://malbiruk.github.io/tidepool-theme/plotly_gallery.html)**

## Installation

```bash
pip install tidepool-theme
```

Or with specific backends only:

```bash
pip install "tidepool-theme[mpl]"
pip install "tidepool-theme[plotly]"
pip install "tidepool-theme[all]"
```

## Usage

### Matplotlib / Seaborn

```python
import tidepool
tidepool.set_mpl_style()

# seaborn inherits the style automatically
import seaborn as sns
sns.scatterplot(...)
```

> **Note:** calling `sns.set_theme()` after `set_mpl_style()` will override
> the style. Use seaborn plotting functions directly instead.

### Plotly

```python
import tidepool
tidepool.set_plotly_template()

import plotly.express as px
fig = px.scatter(...)  # uses tidepool template by default
```

## What's included

- **Background:** `#fafafa` — light warm gray
- **Font:** [Source Serif 4](https://github.com/adobe-fonts/source-serif) (bundled, SIL Open Font License)
- **Color cycle:** 34 soft coastal tones starting with lightseagreen, lightsalmon, steelblue
- **Colormaps:** `purpor` / `purpor_r` (sequential) and `tealrose` / `tealrose_r` (diverging), from [CARTOColors](https://carto.com/carto-colors/)
- **Layout:** no grid, left+bottom spines only, clean axis lines

## License

MIT
