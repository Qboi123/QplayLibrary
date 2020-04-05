import tkinter.ttk as ttk
import tkinter as tk
from typing import Union, Callable

from lib.qplay_ui.theme import Theme as Theme_
import lib.qplay_ui.theme

lib.qplay_ui.theme.ACCENT_COLOR_P1 = "#405fff"
lib.qplay_ui.theme.ACCENT_COLOR = "#001fff"
lib.qplay_ui.theme.ACCENT_COLOR_M1 = "#0000df"

THEME_DARK = lambda: Theme_(darkmode=True)
# THEME_LIGHT = Theme_(darkmode=False)


# noinspection PyShadowingNames
class QWindow(tk.Tk):
    def __init__(self, title="QWindow", geometry="800x600", fullscreen=True, alpha=1, theme=THEME_DARK):
        super(QWindow, self).__init__()

        self.geometry(geometry)
        self.title(title)
        self.attributes("-fullscreen", fullscreen, "-alpha", alpha)

        self.theme = theme()

        self.mainFrame = QFrame(self)
        self.mainFrame.pack(fill="both", expand=True)


class QFrame(tk.Frame):
    def __init__(self, master: QWindow):
        self._bgColor = "#373737" if master.theme.isDark() else "#a7a7a7"

        super(QFrame, self).__init__(master, bg=self._bgColor)


class QButton(ttk.Button):
    def __init__(self, master: Union[QWindow, QFrame], text="TEXT", command: Callable = lambda: None):
        super(QButton, self).__init__(master, text=text, command=command)


class QLabel(ttk.Label):
    def __init__(self, master: Union[QWindow, QFrame], text="TEXT"):
        super(QLabel, self).__init__(master, text=text)


class QTreeView(ttk.Treeview):
    def __init__(self, master: Union[QWindow, QFrame], columns=None):
        super(QTreeView, self).__init__(master, columns=columns)


class QCanvas(tk.Canvas):
    def __init__(self, master: Union[QWindow, QFrame]):
        if master._root().theme.isDark():
            self._bgColor = "#2f2f2f"
        else:
            self._bgColor = "#f0f0f0"
        super(QCanvas, self).__init__(master, bg=self._bgColor, highlightthickness=0)


if __name__ == '__main__':
    main_window = QWindow()
    button = QButton(main_window.mainFrame, text="Button 1")
    button.pack()
    button2 = QButton(main_window.mainFrame, text="Button 2")
    button2.pack()
    button3 = QButton(main_window.mainFrame, text="Button 3")
    button3.pack()
    button4 = QButton(main_window.mainFrame, text="Disabled")
    button4.config(state="disabled")
    button4.pack()
    button5 = QButton(main_window.mainFrame, text="Button 5")
    button5.pack()
    treeview = QTreeView(main_window.mainFrame, columns=[])
    print(treeview.keys())
    print(treeview["displaycolumns"])
    treeview["displaycolumns"] = []
    treeview.heading('#0', text="Heading")
    for i in range(20):
        a = treeview.insert("", "end", text=f"Item {i}")
        for j in range(3):
            treeview.insert(a, "end", text=f"Subitem {j}")
    treeview.pack()
    canvas = QCanvas(main_window.mainFrame)
    canvas.pack()
    main_window.mainloop()
