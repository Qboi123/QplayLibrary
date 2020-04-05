from tkinter.ttk import Style

FONT = ("Helvetica", 10)

TREEVIEW_BG = "#7f7f7f"
TREEVIEW_FG = "#9f9f9f"
TREEVIEW_SEL_BG = "gold"
TREEVIEW_SEL_FG = "white"

BUTTON_BG = "#7f7f7f"
BUTTON_BG_FOC = "gold"
BUTTON_BG_DIS = "#5c5c5c"
BUTTON_FG = "#a7a7a7"
BUTTON_FG_FOC = "white"
BUTTON_FG_DIS = "#7f7f7f"
BUTTON_BD_COL = "gold"
BUTTON_RELIEF = "flat"
BUTTON_BD_WID = 0

ENTRY_BG = "#7f7f7f"
ENTRY_BG_FOC = "gold"
ENTRY_BG_DIS = "#5c5c5c"
ENTRY_FG = "#a7a7a7"
ENTRY_FG_FOC = "white"
ENTRY_FG_DIS = "#7f7f7f"
ENTRY_BD_COL = "gold"
ENTRY_RELIEF = "flat"
ENTRY_BD_WID = 0
ENTRY_SEL_BG = "gold"
ENTRY_SEL_BG_FOC = "#fce58a"
ENTRY_SEL_BG_DIS = "#ec9712"
ENTRY_SEL_FG = "gold"
ENTRY_SEL_FG_FOC = "white"
ENTRY_SEL_FG_DIS = "#7f7f7f"

ACCENT_COLOR_P1 = "#ffc720"
ACCENT_COLOR = "#ffa700"
ACCENT_COLOR_M1 = "#df8700"

dark_theme = lambda: {
    "TEntry": {
        "configure": {"font": FONT, "relief": "flat", "selectborderwidth": 0},
        "map": {
            "relief": [("active", "flat"),
                       ("focus", "flat"),
                       ("!disabled", "flat")],
            "bordercolor": [("active", ACCENT_COLOR),
                            ("focus", ACCENT_COLOR),
                            ("!disabled", ACCENT_COLOR)],
            "background": [("active", "#5c5c5c"),
                           ("focus", ACCENT_COLOR),
                           ("!disabled", "#373737")],
            "fieldbackground": [("active", "#5c5c5c"),
                                ("focus", ACCENT_COLOR),
                                ("!disabled", "#373737")],
            "foreground": [("active", "#939393"),
                           ("focus", "white"),
                           ("!disabled", "#5c5c5c")],
            "selectbackground": [("active", "#7f7f7f"),
                                 ("focus", ACCENT_COLOR_P1),
                                 ("!disabled", "#373737")],
            "selectforeground": [("active", "#a7a7a7"),
                                 ("focus", "white"),
                                 ("!disabled", "#5c5c5c")]
        }
    },
    "TLabel": {
        "configure": {"background": "#373737",
                      "foreground": "#a7a7a7",
                      "font": FONT}
    },
    "TButton": {
        "configure": {"font": FONT, "relief": "flat"},
        "map": {
            "relief": [("pressed", "flat"),
                       ("active", "flat"),
                       ("focus", "flat"),
                       ("!disabled", "flat"),
                       ("disabled", "flat")],
            "background": [("pressed", ACCENT_COLOR_M1),
                           ("active", ACCENT_COLOR),
                           ("focus", ACCENT_COLOR_P1),
                           ("!disabled", "#5c5c5c"),
                           ("disabled", "#373737")],
            "bordercolor": [("pressed", ACCENT_COLOR_M1),
                            ("active", ACCENT_COLOR),
                            ("focus", ACCENT_COLOR_P1),
                            ("!disabled", "#5c5c5c"),
                            ("disabled", "#373737")],
            "foreground": [("pressed", "#dadada"),
                           ("active", "white"),
                           ("focus", "white"),
                           ("!disabled", "#a7a7a7"),
                           ("disabled", "#5c5c5c")],
        }
    },
    "Treeview": {
        "configure": {"padding": 0, "font": FONT, "relief": "flat", "border": 0, "rowheight": 24},
        "map": {
            "background": [("selected", ACCENT_COLOR),
                           ("active", "#5c5c5c"),
                           ("focus", ACCENT_COLOR),
                           ("!disabled", "#5c5c5c"),
                           ("disabled", "#373737")],
            "fieldbackground": [("selected", ACCENT_COLOR),
                                ("active", "#5c5c5c"),
                                ("focus", ACCENT_COLOR),
                                ("!disabled", "#5c5c5c"),
                                ("disabled", "#373737")],
            "foreground": [("selected", "white"),
                           ("active", "#a7a7a7"),
                           ("focus", "white"),
                           ("!disabled", "#a7a7a7"),
                           ("disabled", "#5c5c5c")],
            "relief": [("selected", "flat"),
                       ("active", "flat"),
                       ("focus", "flat"),
                       ("!disabled", "flat"),
                       ("disabled", "flat")]
        }
    },
    "Treeview.Item": {
        "configure": {"padding": 0, "font": FONT, "border": 0, "highlightthickness": 0},
        "map": {
            "background": [("selected", ACCENT_COLOR),
                           ("pressed", ACCENT_COLOR_M1),
                           ("active", ACCENT_COLOR),
                           ("focus", ACCENT_COLOR),
                           ("!disabled", "#5c5c5c"),
                           ("disabled", "#373737")],
            "fieldbackground": [("selected", ACCENT_COLOR),
                                ("pressed", ACCENT_COLOR_M1),
                                ("active", ACCENT_COLOR),
                                ("focus", ACCENT_COLOR),
                                ("!disabled", TREEVIEW_SEL_BG),
                                ("disabled", "#373737")],
            "foreground": [("selected", "white"),
                           ("pressed", "white"),
                           ("active", "white"),
                           ("focus", "white"),
                           ("!disabled", "#a7a7a7"),
                           ("disabled", "#5c5c5c")],
            "relief": [("selected", "flat"),
                       ("pressed", "flat"),
                       ("active", "flat"),
                       ("focus", "flat"),
                       ("!disabled", "flat"),
                       ("disabled", "flat")]
        }
    },
    "Treeview.Heading": {
        "configure": {"padding": 0, "font": FONT, "border": 0, "highlightthickness": 0},
        "map": {
            "background": [("selected", ACCENT_COLOR_P1),
                           ("pressed", "#dadada"),
                           ("focus", "white"),
                           ("active", "white"),
                           ("!disabled", ACCENT_COLOR_P1),
                           ("disabled", "#5c5c5c")],
            "fieldbackground": [("selected", ACCENT_COLOR_P1),
                                ("pressed", "#dadada"),
                                ("focus", "white"),
                                ("active", "white"),
                                ("!disabled", ACCENT_COLOR_P1),
                                ("disabled", "#5c5c5c")],
            "foreground": [("selected", "white"),
                           ("pressed", ACCENT_COLOR_M1),
                           ("focus", ACCENT_COLOR),
                           ("active", ACCENT_COLOR),
                           ("!disabled", "white"),
                           ("disabled", "#7f7f7f")],
            "relief": [("selected", "flat"),
                       ("pressed", "flat"),
                       ("focus", "flat"),
                       ("active", "flat"),
                       ("!disabled", "flat"),
                       ("disabled", "flat")]
        },
        "Treeview.Cell": {
            "configure": {"padding": 0, "border": 0, "highlightthickness": 0},
            "map": {
                "background": [("selected", ACCENT_COLOR_P1),
                               ("pressed", "#dadada"),
                               ("focus", "white"),
                               ("active", ACCENT_COLOR_P1),
                               ("!disabled", ACCENT_COLOR),
                               ("disabled", "#5c5c5c")],
                "fieldbackground": [("selected", ACCENT_COLOR_P1),
                                    ("pressed", "#dadada"),
                                    ("focus", "white"),
                                    ("active", ACCENT_COLOR_P1),
                                    ("!disabled", ACCENT_COLOR),
                                    ("disabled", "#5c5c5c")],
                "foreground": [("selected", "white"),
                               ("pressed", ACCENT_COLOR_M1),
                               ("focus", ACCENT_COLOR),
                               ("active", "white"),
                               ("!disabled", "white"),
                               ("disabled", "#7f7f7f")],
                "relief": [("selected", "flat"),
                           ("pressed", "flat"),
                           ("focus", "flat"),
                           ("active", "flat"),
                           ("!disabled", "flat"),
                           ("disabled", "flat")]
            }
        }
    }
}


class Theme(object):
    def __init__(self, darkmode=True):
        self._darkMode = darkmode

        if self.isDark():
            s = Style()
            s.theme_settings("default", dark_theme())
            s.theme_use("default")
        else:
            raise NotImplementedError("Light mode is not supported")

    def isDark(self):
        return self._darkMode

    def isLight(self):
        return not self._darkMode
