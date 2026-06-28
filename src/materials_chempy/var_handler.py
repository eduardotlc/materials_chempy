"""
Created on 2026-06-28 15:39:23.

@author: eduardotc
@contributors: lu4vic
@email: eduardotcampos@hotmail.com

Global variables that are used by multiple modules definitions.
"""

from pathlib import Path
from typing import TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from rich.theme import Theme


class VarHandle:
    """
    Handle variables lists and dicts to other modules.

    Attributes
    ----------
    ansi_dicts : dict
        Can be one of the following color names:
            - RST
            - RED
            - GRN
            - YLW
            - BLUE
            - MGN
            - CYAN
            - TXT
            - VLT
            - AQUA
            - PNK
            - LRED
            - ORANGE
            - BLCK
            - DGRAY
            - GRAY
            - LGRAY
            - WHT
            - NONE

    col_aliases : dict
        Can be one of the following:
            - blue
            - yellow
            - red
            - green
            - magenta
            - purple
            - pink
            - reset
            - white
            - black
            - cyan
            - text
            - foreground
            - bold
            - aqua
            - orange
            - dark_gray
            - gray
            - light_gray
            - light_red

    Examples
    --------
    >>> from .argtypes import check_ansi_color_code
    >>> vars = VarHandle()
    >>> tst = vars("YLW")
    >>> print(check_ansi_color_code(tst)[0])
    (38, 3)
    """

    def __init__(self):
        """Init class and assign dicts values."""
        self.ansi_dicts = {
            "RST": "\033[0m",
            "RED": "\033[38;5;001m",
            "GRN": "\033[38;5;002m",
            "YLW": "\033[38;5;003m",
            "BLUE": "\033[38;5;004m",
            "MGN": "\033[38;5;005m",
            "CYAN": "\033[38;5;006m",
            "TXT": "\033[38;5;007m",
            "GOLD": "\033[38;5;011m",
            "BLD": "\033[38;5;015m",
            "DGRN": "\033[38;5;023m",
            "SEA": "\033[38;5;033m",
            "LSEA": "\033[38;5;039m",
            "PRP": "\033[38;5;056m",
            "VLT": "\033[38;5;063m",
            "LSTBLUE": "\033[38;5;067m",
            "AQUA": "\033[38;5;081m",
            "TEAL": "\033[38;5;110m",
            "FBLUE": "\033[38;5;153m",
            "FPNK": "\033[38;5;225m",
            "PNK": "\033[38;5;201m",
            "LPNK": "\033[38;5;219m",
            "LRED": "\033[38;5;203m",
            "ORANGE": "\033[38;5;208m",
            "BLCK": "\033[38;5;232m",
            "DGRAY": "\033[38;5;237m",
            "GRAY": "\033[38;5;242m",
            "LGRAY": "\033[38;5;249m",
            "WHT": "\033[38;5;255m",
            "NONE": "",
        }

        self.col_aliases = {
            "blue": "BLUE",
            "yellow": "YLW",
            "red": "RED",
            "green": "GRN",
            "magenta": "MGN",
            "purple": "PRP",
            "pink": "PNK",
            "reset": "RST",
            "gold": "GOLD",
            "white": "WHT",
            "black": "BLCK",
            "cyan": "CYAN",
            "text": "TXT",
            "foreground": "TXT",
            "bold": "BLD",
            "aqua": "AQUA",
            "orange": "ORANGE",
            "dark_gray": "DGRAY",
            "gray": "GRAY",
            "light_gray": "LGRAY",
            "light_red": "LRED",
            "violet": "VLT",
            "dark_aqua": "DAQUA",
            "dark_violet": "DVLT",
            "dark_red": "DRED",
            "dark_yellow": "DYLW",
        }

        self.rgb_dict = {
            "BLCK": (0, 0, 0),
            "WHT": (1, 1, 1),
            "RED": (1, 0, 0),
            "GRN": (0, 1, 0),
            "BLUE": (0, 0, 1),
            "YLW": (1, 0.92, 0.48),
            "CYAN": (0.55, 1, 0.91),
            "VLT": (0.61, 0.46, 0.95),
            "PNK": (0.95, 0.48, 0.75),
            "DAQUA": (0.23, 0.45, 0.40),
            "DVLT": (0.28, 0.23, 0.45),
            "DRED": (0.45, 0.24, 0.31),
            "DYLW": (0.45, 0.44, 0.29),
            "BLURPLE": (0.64, 0.70, 0.98),
        }

        self.markdown_theme = {
            "markdown.h1": "bold cyan",
            "markdown.h2": "bold magenta",
            "markdown.h3": "bold green",
            "markdown.bold": "bold yellow",
            "markdown.italic": "italic white",
            "markdown.code": "bold black on white",
            "markdown.block_quote": "dim cyan",
            "markdown.list_item": "bright_white",
            "markdown.hr": "red",
            "markdown.link": "underline bright_blue",
        }

        self.markdown_no_colors_theme = {
            "markdown.h1": "",
            "markdown.h2": "",
            "markdown.h3": "",
            "markdown.bold": "",
            "markdown.italic": "",
            "markdown.code": "",
            "markdown.block_quote": "",
            "markdown.list_item": "",
            "markdown.hr": "",
            "markdown.link": "",
        }

        self.css_theme = """
        @page {
          size: A4;
          margin: 25mm;
        }

        body {
          font-family: Arial, sans-serif;
          line-height: 1.5;
          font-size: 12pt;
          color: #333;
        }

        h1, h2, h3, h4, h5, h6 {
          page-break-after: avoid;
          page-break-inside: avoid;
        }

        img {
          max-width: 90%;
          page-break-inside: avoid;
        }

        table {
          width: 90%;
          page-break-inside: auto;
        }

        thead {
          display: table-header-group;
        }

        tfoot {
          display: table-footer-group;
        }

        @page :left {
          margin-left: 25mm;
          margin-right: 15mm;
        }

        @page :right {
          margin-left: 15mm;
          margin-right: 25mm;
        }

        .header {
          position: running(header);
        }

        .footer {
          position: running(footer);
          font-size: 10pt;
          text-align: center;
        }

        @page {
          @top-center {
            content: element(header);
          }
          @bottom-center {
            content: element(footer);
          }
        }

        tr, td, th {
          page-break-inside: avoid;
          page-break-after: auto;
          page-break-before: auto;
          max-width: 90%;
        }

        image-container {
          max-widt: 80%;
        }

        p, ul, ol, dl {
          page-break-inside: avoid;
        }
        """

        self.use_colors = True
        self.checking_count = 0

    def set_use_colors(self, enable: bool):
        """
        Set `use_colors` attribute value, controling if ansi colors will be returned by the class.

        Parameters
        ----------
        enable : bool

        Examples
        --------
        >>> vars = VarHandle()
        >>> print(vars.use_colors)
        True

        >>> vars.set_use_colors(False)
        >>> print(vars.use_colors)
        False
        """
        self.use_colors = enable

    def __call__(self, arg: str) -> str:
        """
        Get ansi color escape code string from the given name, stored in `ansi_dicts`.

        Parameters
        ----------
        arg : str

        Examples
        --------
        >>> from .argtypes import check_ansi_color_code
        >>> tst_cls = VarHandle()
        >>> print(check_ansi_color_code(tst_cls("YLW"))[0])
        (38, 3)

        >>> print(check_ansi_color_code(tst_cls("non_existing_color"))[0])
        (38, 7)
        """
        if not self.use_colors:
            return ""

        return self.ansi_dicts.get(self.col_aliases.get(arg, arg), self.ansi_dicts["TXT"])

    def _get_all_fonts(self) -> dict:
        """
        Search all available fonts files.

        Returns
        -------
        dict
            Dict with keys being a font name, and value its file path

        Examples
        --------
        >>> var_handle = VarHandle()
        >>> fonts = var_handle._get_all_fonts()
        >>> print(fonts["jetbrainsmono-regular"])
        /home/eduardotc/.fonts/JetBrainsMono/fonts/ttf/JetBrainsMono-Regular.ttf
        """
        fonts_exts = [".otf", ".woff2", ".ttf"]
        base_dir = Path("/home/eduardotc/.fonts")
        fonts = {}

        for path in base_dir.rglob("*"):
            if path.is_file() and path.suffix.lower() in fonts_exts:
                base_name = path.stem.lower()
                fonts[base_name] = str(path)

        return fonts

    def deduplicate_dict(self, original_dict: dict, extension_order: list) -> dict:
        """
        Given a dict wit file paths values, remove duplicates based on the file extension.

        Given a dict as parameter `original_dict`, with keys being files names or complete paths
        (should include file extension), remove duplicate keys of the dictionary (key should be the
        same, value can be different), based on a priority order of file extensions defined by
        `extension_order`.

        Parameters
        ----------
        original_dict : dict
        extension_order : list

        Returns
        -------
        dict
            Dictionary with duplicate key values removed.
        """
        sorted_items = sorted(
            original_dict.items(),
            key=lambda item: extension_order.index(item[1].split(".")[-1]),
        )
        new_dict = {}

        for key, value in sorted_items:
            if key not in new_dict:
                new_dict[key] = value

        return new_dict

    def search_fonts(self, name: str, weight: str = "regular") -> str:
        """
        Search between all available fonts for given one.

        Given a font family name and weight, search in "~/.fonts" for a matching font.

        Parameters
        ----------
        name : str
            Font family name
        weight : str, (Default: "regular")
            Font weight

        Returns
        -------
        str
            Font file path

        Examples
        --------
        >>> var_handle = VarHandle()
        >>> font_src = var_handle.search_fonts("FiraMonoNerdFont", "bold")
        >>> print(font_src)
        /home/eduardotc/.fonts/FiraMono/FiraMonoNerdFont-Bold.otf
        """
        fonts = self._get_all_fonts()
        font_src = fonts.get(f"{name.lower()}-{weight.lower()}", fonts["jetbrainsmono-regular"])
        return font_src

    def rgb(self, name: str, mode: int = 1) -> tuple:
        """
        Handle rgb names returning theirs associated tuple, in 0-1 or 0-255 normalization.

        Parameters
        ----------
        name : str
            Color name, one of the dict keys in `col_aliases` or `rgb_dict`
        mode : int, (Default 1)
            Either 1 or 255, defines the normalization of the tuple

        Returns
        -------
        tuple
            rgb tuple

        Examples
        --------
        >>> tst_cls = VarHandle()
        >>> wht_rgb = tst_cls.rgb("white")
        >>> print(wht_rgb)
        (1, 1, 1)

        >>> wht_rgb_255 = tst_cls.rgb("WHT", mode=255)
        >>> print(wht_rgb_255)
        (255, 255, 255)
        """
        rgb_tuple = self.rgb_dict.get(
            self.col_aliases.get(name.lower(), name),
            self.rgb_dict["WHT"],
        )
        rgb_tuple = [(f * 255) for f in rgb_tuple] if mode == 255 else rgb_tuple
        return tuple(rgb_tuple)

    def theme(self, theme_type: str) -> "Theme":
        """
        Get theme based on given `theme_type` parameter.

        Parameters
        ----------
        theme_type : str

        Returns
        -------
        Theme
        """
        from rich.theme import Theme

        themes = {
            "markdown": Theme(self.markdown_theme),
            "markdown_no_color": Theme(self.markdown_no_colors_theme),
            "css": self.css_theme,
        }
        result_theme = themes.get(theme_type.lower())
        return result_theme


HB_HUB = "/home/eduardotc/.local/ai/drive/huggingface/hub"


GIMP_PALETTES = [
    f.stem for f in Path("/home/eduardotc/.config/GIMP/3.0/palettes").iterdir() if f.is_file()
]

OPTIONS_DICT = {
    "palette_name": [
        "sioyek",
        "latex_iq",
        "latex_timeline",
        "ariake",
        "dracula",
        "catppuccin_mocha",
        "bittersweet",
        "tokyo_night",
        "cyberdream",
        "moonlight",
        "nightfly",
        "kyoto_night",
        "nord",
        "ipe_midnight",
        "ipe_midnight_soft",
        "ipe_midnight_cold",
        "abyss",
        "penumbra",
        "penumbra_plus",
        "penumbra_plus_plus",
        "oh_lucy",
        *GIMP_PALETTES,
    ],
    "weight": [
        "regular",
        "medium",
        "bold",
        "italic",
        "thin",
        "light",
        "oblique",
        "heavy",
        "retina",
        "black",
        "semibold",
        "extralight",
        "extrabold",
        "extrathick",
        "bolditalic",
        "lightitalic",
        "thinitalic",
        "mediumitalic",
        "heavyitalic",
        "lightoblique",
        "thinoblique",
        "boldoblique",
        "mediumoblique",
        "semiboldoblique",
        "extraboldoblique",
        "extralightoblique",
        "semibolditalic",
        "extralightitalic",
        "extrabolditalic",
        "condensedblack",
        "semicondensedblack",
        "semicondensedextralight",
        "semicondensedextrabold",
        "condensedextralight",
        "condensedblackitalic",
        "extracondensedlightitalic",
    ],
    "study_category": ["russian"],
    "study_group": ["letters"],
    "protocol": ["tcp", "udp"],
}

# --- Full CSS3 names to hex mapping (140 colors) ---
CSS3_NAMES_TO_HEX: dict[str, str] = {
    "aliceblue": "#f0f8ff",
    "antiquewhite": "#faebd7",
    "aqua": "#00ffff",
    "aquamarine": "#7fffd4",
    "azure": "#f0ffff",
    "beige": "#f5f5dc",
    "bisque": "#ffe4c4",
    "black": "#000000",
    "blanchedalmond": "#ffebcd",
    "blue": "#0000ff",
    "blueviolet": "#8a2be2",
    "brown": "#a52a2a",
    "burlywood": "#deb887",
    "cadetblue": "#5f9ea0",
    "chartreuse": "#7fff00",
    "chocolate": "#d2691e",
    "coral": "#ff7f50",
    "cornflowerblue": "#6495ed",
    "cornsilk": "#fff8dc",
    "crimson": "#dc143c",
    "cyan": "#00ffff",
    "darkblue": "#00008b",
    "darkcyan": "#008b8b",
    "darkgoldenrod": "#b8860b",
    "darkgray": "#a9a9a9",
    "darkgreen": "#006400",
    "darkgrey": "#a9a9a9",
    "darkkhaki": "#bdb76b",
    "darkmagenta": "#8b008b",
    "darkolivegreen": "#556b2f",
    "darkorange": "#ff8c00",
    "darkorchid": "#9932cc",
    "darkred": "#8b0000",
    "darksalmon": "#e9967a",
    "darkseagreen": "#8fbc8f",
    "darkslateblue": "#483d8b",
    "darkslategray": "#2f4f4f",
    "darkslategrey": "#2f4f4f",
    "darkturquoise": "#00ced1",
    "darkviolet": "#9400d3",
    "deeppink": "#ff1493",
    "deepskyblue": "#00bfff",
    "dimgray": "#696969",
    "dimgrey": "#696969",
    "dodgerblue": "#1e90ff",
    "firebrick": "#b22222",
    "floralwhite": "#fffaf0",
    "forestgreen": "#228b22",
    "fuchsia": "#ff00ff",
    "gainsboro": "#dcdcdc",
    "ghostwhite": "#f8f8ff",
    "gold": "#ffd700",
    "goldenrod": "#daa520",
    "gray": "#808080",
    "green": "#008000",
    "greenyellow": "#adff2f",
    "grey": "#808080",
    "honeydew": "#f0fff0",
    "hotpink": "#ff69b4",
    "indianred": "#cd5c5c",
    "indigo": "#4b0082",
    "ivory": "#fffff0",
    "khaki": "#f0e68c",
    "lavender": "#e6e6fa",
    "lavenderblush": "#fff0f5",
    "lawngreen": "#7cfc00",
    "lemonchiffon": "#fffacd",
    "lightblue": "#add8e6",
    "lightcoral": "#f08080",
    "lightcyan": "#e0ffff",
    "lightgoldenrodyellow": "#fafad2",
    "lightgray": "#d3d3d3",
    "lightgreen": "#90ee90",
    "lightgrey": "#d3d3d3",
    "lightpink": "#ffb6c1",
    "lightsalmon": "#ffa07a",
    "lightseagreen": "#20b2aa",
    "lightskyblue": "#87cefa",
    "lightslategray": "#778899",
    "lightslategrey": "#778899",
    "lightsteelblue": "#b0c4de",
    "lightyellow": "#ffffe0",
    "lime": "#00ff00",
    "limegreen": "#32cd32",
    "linen": "#faf0e6",
    "magenta": "#ff00ff",
    "maroon": "#800000",
    "mediumaquamarine": "#66cdaa",
    "mediumblue": "#0000cd",
    "mediumorchid": "#ba55d3",
    "mediumpurple": "#9370db",
    "mediumseagreen": "#3cb371",
    "mediumslateblue": "#7b68ee",
    "mediumspringgreen": "#00fa9a",
    "mediumturquoise": "#48d1cc",
    "mediumvioletred": "#c71585",
    "midnightblue": "#191970",
    "mintcream": "#f5fffa",
    "mistyrose": "#ffe4e1",
    "moccasin": "#ffe4b5",
    "navajowhite": "#ffdead",
    "navy": "#000080",
    "oldlace": "#fdf5e6",
    "olive": "#808000",
    "olivedrab": "#6b8e23",
    "orange": "#ffa500",
    "orangered": "#ff4500",
    "orchid": "#da70d6",
    "palegoldenrod": "#eee8aa",
    "palegreen": "#98fb98",
    "paleturquoise": "#afeeee",
    "palevioletred": "#db7093",
    "papayawhip": "#ffefd5",
    "peachpuff": "#ffdab9",
    "peru": "#cd853f",
    "pink": "#ffc0cb",
    "plum": "#dda0dd",
    "powderblue": "#b0e0e6",
    "purple": "#800080",
    "rebeccapurple": "#663399",
    "red": "#ff0000",
    "rosybrown": "#bc8f8f",
    "royalblue": "#4169e1",
    "saddlebrown": "#8b4513",
    "salmon": "#fa8072",
    "sandybrown": "#f4a460",
    "seagreen": "#2e8b57",
    "seashell": "#fff5ee",
    "sienna": "#a0522d",
    "silver": "#c0c0c0",
    "skyblue": "#87ceeb",
    "slateblue": "#6a5acd",
    "slategray": "#708090",
    "slategrey": "#708090",
    "snow": "#fffafa",
    "springgreen": "#00ff7f",
    "steelblue": "#4682b4",
    "tan": "#d2b48c",
    "teal": "#008080",
    "thistle": "#d8bfd8",
    "tomato": "#ff6347",
    "turquoise": "#40e0d0",
    "violet": "#ee82ee",
    "wheat": "#f5deb3",
    "white": "#ffffff",
    "whitesmoke": "#f5f5f5",
    "yellow": "#ffff00",
    "yellowgreen": "#9acd32",
}


VARHANDLE = VarHandle()
