import tkinter as tk


class CustomScrollbar(tk.Canvas):
    def __init__(self, parent, **kwargs):
        self.command = kwargs.pop("command", None)
        tk.Canvas.__init__(self, parent, **kwargs)
        if "fg" not in kwargs.keys():
            kwargs["fg"] = "darkgray"

        # coordinates are irrelevant; they will be recomputed
        # in the 'set' method\
        self.old_y = 0
        self.create_rectangle(0, 0, 1, 1, fill=kwargs["fg"], outline=kwargs["fg"], tags=("thumb",))
        self.bind("<ButtonPress-1>", self.on_press)
        self.bind("<ButtonRelease-1>", self.on_release)

    def redraw(self, event):
        # The command is presumably the `yview` method of a widget.
        # When called without any arguments it will return fractions
        # which we can pass to the `set` command.
        self.set(*self.command())

    def set(self, first, last):
        first = float(first)
        last = float(last)
        height = self.winfo_height()
        x0 = 2
        x1 = self.winfo_width() - 2
        y0 = max(int(height * first), 0)
        y1 = min(int(height * last), height)
        self._x0 = x0
        self._x1 = x1
        self._y0 = y0
        self._y1 = y1

        self.coords("thumb", x0, y0, x1, y1)

    def on_press(self, event):
        self.bind("<Motion>", self.on_click)
        self.pressed_y = event.y
        self.on_click(event)

    def on_release(self, event):
        self.unbind("<Motion>")

    def on_click(self, event):
        y = event.y / self.winfo_height()
        y0 = self._y0
        y1 = self._y1
        # print(y0, y1)
        # print(y1-y0)
        # print((y1-y0)/2)
        a = y + (((y1 - y0) / -(self.winfo_height() * 2)))
        # print(((y1-y0)/2)*y/100)
        self.command("moveto", a)


if __name__ == '__main__':
    root = tk.Tk()

    text = tk.Text(root, height=1)
    sb = CustomScrollbar(root, width=5, command=text.yview)
    text.configure(yscrollcommand=sb.set)

    sb.pack(side="right", fill="y")
    text.pack(side="left", fill="both", expand=True)

    with open(__file__, "r") as f:
        text.insert("end", f.read())

    root.mainloop()