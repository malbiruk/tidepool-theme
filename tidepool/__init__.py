"""
Tidepool — a light, minimal plotting theme.

Soft coastal palette, Source Serif 4 typography, clean layout.
Available for both matplotlib/seaborn and plotly.

Usage:
    import tidepool

    # Matplotlib / Seaborn
    tidepool.set_mpl_style()

    # Plotly
    tidepool.set_plotly_template()
"""

from pathlib import Path

_PKG_DIR = Path(__file__).parent
_STYLE_PATH = _PKG_DIR / "tidepool.mplstyle"
_FONTS_DIR = _PKG_DIR / "fonts"

COLORWAY = [
    "lightseagreen",
    "lightsalmon",
    "steelblue",
    "lightpink",
    "plum",
    "skyblue",
    "darkseagreen",
    "darkgray",
    "darksalmon",
    "mediumturquoise",
    "lightcoral",
    "palegreen",
    "orchid",
    "powderblue",
    "thistle",
    "lightslategray",
    "peachpuff",
    "mistyrose",
    "lavender",
    "aquamarine",
    "wheat",
    "paleturquoise",
    "sandybrown",
    "lightcyan",
    "khaki",
    "mediumaquamarine",
    "lemonchiffon",
    "pink",
    "palevioletred",
    "moccasin",
    "burlywood",
    "gainsboro",
    "rosybrown",
    "palegoldenrod",
]

PLOTLY_CONFIG = {
    "displaylogo": False,
    "scrollZoom": True,
}

_PURPOR_COLORS = [
    "#f9ddda",
    "#f2b9c4",
    "#e597b9",
    "#ce78b3",
    "#ad5fad",
    "#834ba0",
    "#573b88",
]
_TEALROSE_COLORS = [
    "#009392",
    "#72aaa1",
    "#b1c7b3",
    "#f1eac8",
    "#e5b9ad",
    "#d98994",
    "#d0587e",
]


def _register_fonts():
    """Register bundled Source Serif 4 fonts with matplotlib."""
    from matplotlib.font_manager import fontManager

    for ttf in _FONTS_DIR.glob("*.ttf"):
        fontManager.addfont(str(ttf))


def _register_colormaps():
    """Register purpor and tealrose colormaps matching the plotly template."""
    import matplotlib as mpl
    from matplotlib.colors import LinearSegmentedColormap

    for name, colors in [("purpor", _PURPOR_COLORS), ("tealrose", _TEALROSE_COLORS)]:
        if name not in mpl.colormaps:
            cm = LinearSegmentedColormap.from_list(name, colors, N=256)
            mpl.colormaps.register(cm)
            mpl.colormaps.register(cm.reversed())


def set_mpl_style():
    """Activate the tidepool style for matplotlib and seaborn.

    Registers the bundled Source Serif 4 font, custom colormaps
    (purpor, tealrose + reversed variants), and applies the style.

    Seaborn inherits matplotlib's rcParams automatically — just call
    this before creating any seaborn plots.

    Note: if you call sns.set_theme() after this, it will override
    the style. Use seaborn plotting functions directly instead.

    Note: seaborn desaturates fill colors by default (saturation=0.75).
    Use saturation=1.0 in seaborn calls for exact color matching.
    """
    import matplotlib as mpl
    import matplotlib.pyplot as plt

    _register_fonts()
    _register_colormaps()
    plt.style.use(str(_STYLE_PATH))
    mpl.rcParams["font.serif"] = [
        "Source Serif 4",
        "Source Serif Pro",
        "Georgia",
        "DejaVu Serif",
        "serif",
    ]
    mpl.rcParams["image.cmap"] = "purpor_r"


def set_plotly_template(*, set_default=True):
    """Register and activate the tidepool template for plotly.

    Args:
        set_default: If True, sets tidepool as the default template.
    """
    import plotly.graph_objects as go
    import plotly.io as pio

    template = go.layout.Template()

    # Background
    template.layout.paper_bgcolor = "#fafafa"
    template.layout.plot_bgcolor = "#fafafa"

    # Font — matches font.size/family/labelsize in mplstyle
    template.layout.font.family = "Source Serif Pro, Georgia, serif"
    template.layout.font.color = "#000000"
    template.layout.font.size = 12

    template.layout.hovermode = "closest"

    # Title & subplot titles — scaled up to visually match mpl's pt-based sizes
    # (plotly font.size is CSS px; mpl figure.titlesize is 16pt at 150 DPI)
    template.layout.title.font.size = 20

    # Axes — matches axes.edgecolor/linewidth/labelsize and xtick/ytick in mplstyle
    for axis in ("xaxis", "yaxis"):
        ax = getattr(template.layout, axis)
        ax.showgrid = False
        ax.showline = True
        ax.linecolor = "#000000"
        ax.linewidth = 0.8
        ax.ticks = ""  # no tick marks, labels only (xtick.major.size: 0)
        ax.tickfont.size = 14
        ax.title.font.size = 14
        ax.title.standoff = 4
        ax.zerolinecolor = "#eaeaea"
        ax.gridcolor = "#eaeaea"
        ax.gridwidth = 0.6

    # Legend — semi-transparent bg, matches legend.fontsize: 8
    template.layout.legend.bgcolor = "rgba(250,250,250,0.7)"
    template.layout.legend.borderwidth = 0
    template.layout.legend.font.size = 9

    # Annotations — matches axes.titlesize: 14 (used by make_subplots titles)
    template.layout.annotationdefaults = {"font": {"size": 14}}

    # Interaction — pan by default, hide box/lasso select
    template.layout.dragmode = "pan"
    template.layout.modebar.remove = ["select2d", "lasso2d"]

    template.layout.colorway = COLORWAY
    template.layout.colorscale = {
        "sequential": "purpor_r",
        "diverging": "Tealrose_r",
    }

    template.layout.coloraxis.colorbar.len = 0.75
    template.layout.coloraxis.colorbar.thickness = 20

    # Trace defaults — matches lines.linewidth and patch.edgecolor in mplstyle
    template.data.scatter = [go.Scatter(line={"width": 1.8})]
    template.data.bar = [go.Bar(marker={"line": {"color": "#fafafa", "width": 1.0}})]
    template.data.histogram = [
        go.Histogram(marker={"line": {"width": 0}}),
    ]

    pio.templates["tidepool"] = template
    if set_default:
        pio.templates.default = "tidepool"
