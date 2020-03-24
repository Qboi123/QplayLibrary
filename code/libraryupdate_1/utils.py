import zipfile

from tkinter import Frame, Canvas

from PIL import ImageTk, ImageDraw2, ImageDraw, ImageFont, Image


def extract_zipfile(path2zip: str, extract_path: str):
    zip_ref = zipfile.ZipFile(path2zip, 'r')
    zip_ref.extractall(extract_path)
    zip_ref.close()


def replace_dir2ver(string: str):
    return string.replace("_pre", "-pre").replace("_", ".")


def replace_ver2dir(string: str):
    return string.replace("-pre", "_pre").replace(".", "_")


def replace_name2dir(string: str):
    return replace_ver2dir(replace_name2ver(string))


def replace_name2ver(string: str):
    return string.replace(" - Pre Release ", "-pre")


def replace_any2name(ver: str):
    ver = replace_dir2ver(ver)
    return ver.replace("-pre", " - Pre Release ")


def yamldict2class(obj: dict):
    """
    DON'T USE THIS. THIS DOESN'T WORKING
    :param obj:
    :return:
    """
    keys = list(obj.keys())
    values = list(obj.values())
    length = len(keys)

    class DictClass:
        def __init__(self):
            pass

    obj2 = dict()

    for index in range(length):
        key = keys[index]
        value = values[index]
        print("Key: %s | Find Dot: %s" % (key, key.find(".")))

        keys2, values2 = dotkeyvalue(key, value)
        # length2 =

        # for index2 in range(length2):


        dictClass.__dict__[key] = value



def dict2class(obj: dict):
    import sys
    class DictClass:
        def __init__(self):
            pass

    print("Object: %s" % obj)

    dictClass = DictClass()

    print("Keys: %s" % list(obj.keys()))

    for index in range(len(list(obj.keys()))):
        key = list(obj.keys())[index]
        value = list(obj.values())[index]
        print("Key: %s | Value: %s" % (key, value))
        if type(key) == dict:
            print("ERROR: Key is a Dict!", file=sys.stderr)
            exit(1)
        if type(value) == dict:
            value = dict2class(value)
        dictClass.__dict__[key] = value

    return dictClass


def draw_ellipse(image, bounds, width=1.0, outline='white', antialias=4):
    """Improved ellipse drawing function, based on PIL.ImageDraw."""

    # Use a single channel image (mode='L') as mask.
    # The size of the mask can be increased relative to the imput image
    # to get smoother looking results.
    mask = Image.new(
        size=[int(dim * antialias) for dim in image.size],
        mode='L', color='black')
    draw = ImageDraw.Draw(mask)

    # draw outer shape in white (color) and inner shape in black (transparent)
    for offset, fill in (width / -1.5, '#ffffffff'), (width / 1.5, '#000000ff'):  # Note: Was first white, black
        left, top = [(value + offset) * antialias for value in bounds[:2]]
        right, bottom = [(value - offset) * antialias for value in bounds[2:]]
        draw.ellipse([left, top, right, bottom], fill=fill)

    # downsample the mask using PIL.Image.LANCZOS
    # (a high-quality downsampling filter).
    mask = mask.resize(image.size, Image.LANCZOS)
    # paste outline color to input image through the mask
    image.paste(outline, mask=mask)


def openbackground(fp, size: tuple):
    im = Image.open(fp)
    im = im.resize(size)
    return ImageTk.PhotoImage(im)


def openresized(fp, size: tuple):
    im = Image.open(fp)
    im = im.resize(size)
    return ImageTk.PhotoImage(im)


def openimage(fp):
    im = Image.open(fp)
    return ImageTk.PhotoImage(im)


def maketextimage(text: str, color=None):
    font = ImageFont.truetype("font/Superfats.ttf", 15)
    a = font.getsize_multiline(text)
    # a = list(a)
    # a[0] *= 2
    # a[1] *= 2
    # a = tuple(a)

    im = Image.new('RGBA', a, (0, 0, 0, 0))
    # fonts = ImageDraw2.ImageFont.load_path("font/")
    drawing = ImageDraw2.ImageDraw.Draw(im)

    drawing.text((0, 0), text, font=font)
    return ImageTk.PhotoImage(im)


def _new(mode, size, color):
    return Image.new(mode, size, color)


def _open(fp, mode: str = "r"):
    return Image.open(fp, mode)


def createbackground(size, color):
    return _new("RGBA", size, color)


def createcolorfield(size, color):
    return createbackground(size, color)


def createellipse(size, bg, fill=None, outline=None, width: int = 0):
    im = _new('RGBA', size, bg)
    draw = ImageDraw.Draw(im, 'RGBA')
    draw.ellipse((0, 0, *size), fill, outline, width)


def createbubble_image(size, fpToPng=None, *colors):
    im = _new('RGBA', size, '#ffffff00')
    # im.putalpha(0)
    if fpToPng is not None:
        png = _open(fpToPng)
    # draw = ImageDraw.Draw(im, "RGBA")
    i = 2

    # Drawung ellipses for Bubble.
    width = 1
    w = width
    for circ_color in colors:
        if circ_color != colors[0]:
            draw_ellipse(im, (0 + i, 0 + i, size[0] - i, size[0] - i), outline=circ_color, width=w, antialias=8)
        elif circ_color != colors[-1]:
            draw_ellipse(im, (0 + i, 0 + i, size[0] - i, size[0] - i), outline=circ_color, width=w, antialias=8)
        else:
            draw_ellipse(im, (0 + i, 0 + i, size[0] - i, size[0] - i), outline=circ_color, width=w, antialias=8)
        i += 1.5

    i += 10

    if fpToPng is not None:
        png2 = _new('RGBA', size, (0, 0, 0, 0))
        # noinspection PyUnboundLocalVariable
        png = png.resize((size[0] - int(i), size[1] - int(i)))
        png2.paste(png, (int(i / 2), int(i / 2)))

        im = Image.alpha_composite(png2, im)

    return ImageTk.PhotoImage(im)


def makebuttonimage(fp: str, text: str, font: str, size: tuple):
    pass


# noinspection PyAttributeOutsideInit,PyUnusedLocal
class CustomScrollbar(Canvas):
    def __init__(self, parent, **kwargs):
        """
        Custom scrollbar, using canvas. It can be configured with fg, bg and command

        :param parent:
        :param kwargs:
        """

        self.command = kwargs.pop("command", None)
        kw = kwargs.copy()
        bd = 0
        hlt = 0
        if "fg" in kw.keys():
            del kw["fg"]
        if "bd" in kw.keys():
            bd = kw.pop("bd")
        if "border" in kw.keys():
            bd = kw.pop("border")
        if "highlightthickness" in kw.keys():
            hlt = kw.pop("highlightthickness")
        Canvas.__init__(self, parent, **kw, highlightthickness=hlt, border=bd, bd=bd)
        if "fg" not in kwargs.keys():
            kwargs["fg"] = "darkgray"

        # coordinates are irrelevant; they will be recomputed
        # in the 'set' method\
        self.old_y = 0
        self._id = self.create_rectangle(0, 0, 1, 1, fill=kwargs["fg"], outline=kwargs["fg"], tags=("thumb",))
        self.bind("<ButtonPress-1>", self.on_press)
        self.bind("<ButtonRelease-1>", self.on_release)

    def configure(self, cnf=None, **kwargs):
        command = kwargs.pop("command", None)
        self.command = command if command is not None else self.command
        kw = kwargs.copy()
        if "fg" in kw.keys():
            del kw["fg"]
        super().configure(**kw, highlightthickness=0, border=0, bd=0)
        if "fg" not in kwargs.keys():
            kwargs["fg"] = "darkgray"
        self.itemconfig(self._id, fill=kwargs["fg"], outline=kwargs["fg"])

    def config(self, cnf=None, **kwargs):
        self.configure(cnf, **kwargs)

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
        a = y + ((y1 - y0) / -(self.winfo_height() * 2))
        self.command("moveto", a)


# noinspection PyUnusedLocal
class ScrolledWindow(Frame):
    """
    1. Master widget gets scrollbars and a canvas. Scrollbars are connected
    to canvas scrollregion.

    2. self.scrollwindow is created and inserted into canvas

    Usage Guideline:
    Assign any widgets as children of <ScrolledWindow instance>.scrollwindow
    to get them inserted into canvas

    __init__(self, parent, canv_w = 400, canv_h = 400, *args, **kwargs)
    docstring:
    Parent = master of scrolled window
    canv_w - width of canvas
    canv_h - height of canvas

    """

    def __init__(self, parent, canv_w=400, canv_h=400, expand=False, fill=None, height=None, width=None, *args,
                 scrollcommand=lambda: None, scrollbarbg=None, scrollbarfg="darkgray", **kwargs):
        """Parent = master of scrolled window
        canv_w - width of canvas
        canv_h - height of canvas

       """
        super().__init__(parent, *args, **kwargs)

        self.parent = parent
        self.scrollCommand = scrollcommand

        # creating a scrollbars

        if width is None:
            __width = 0
        else:
            __width = width

        if height is None:
            __height = 0
        else:
            __height = width

        self.canv = Canvas(self.parent, bg='#FFFFFF', width=canv_w, height=canv_h,
                           scrollregion=(0, 0, __width, __height), highlightthickness=0)

        self.vbar = CustomScrollbar(self.parent, width=10, command=self.canv.yview, bg=scrollbarbg, fg=scrollbarfg, bdcolor=scrollbarbg, bd=1)
        self.canv.configure(yscrollcommand=self.vbar.set)

        self.vbar.pack(side="right", fill="y")
        self.canv.pack(side="left", fill=fill, expand=expand)

        # creating a frame to inserto to canvas
        self.scrollwindow = Frame(self.parent, height=height, width=width)

        self.scrollwindow2 = self.canv.create_window(0, 0, window=self.scrollwindow, anchor='nw', height=height,
                                                     width=width)

        self.canv.config(  # xscrollcommand=self.hbar.set,
            yscrollcommand=self.vbar.set,
            scrollregion=(0, 0, canv_h, canv_w))

        self.scrollwindow.bind('<Configure>', self._configure_window)
        self.scrollwindow.bind('<Enter>', self._bound_to_mousewheel)
        self.scrollwindow.bind('<Leave>', self._unbound_to_mousewheel)

        return

    def _bound_to_mousewheel(self, event):
        self.canv.bind_all("<MouseWheel>", self._on_mousewheel)

    def _unbound_to_mousewheel(self, event):
        self.canv.unbind_all("<MouseWheel>")

    def _on_mousewheel(self, event):
        self.canv.yview_scroll(int(-1 * (event.delta / 120)), "units")
        # self.scrollCommand(int(-1 * (event.delta / 120)), self.scrollwindow.winfo_reqheight(), self.vbar.get(),
        # self.vbar)

    def _configure_window(self, event):
        # update the scrollbars to match the size of the inner frame
        size = (self.scrollwindow.winfo_reqwidth(), self.scrollwindow.winfo_reqheight() + 1)
        self.canv.config(scrollregion='0 0 %s %s' % size)
        # if self.scrollwindow.winfo_reqwidth() != self.canv.winfo_width():
        #     # update the canvas's width to fit the inner frame
        #     # self.canv.config(width=self.scrollwindow.winfo_reqwidth())
        # if self.scrollwindow.winfo_reqheight() != self.canv.winfo_height():
        #     # update the canvas's width to fit the inner frame
        #     # self.canv.config(height=self.scrollwindow.winfo_reqheight())


if __name__ == '__main__':
    from tkinter import *
    from PIL import Image
    root = Tk()
    root.wm_attributes("-fullscreen", True)
    c = Canvas(root, highlightthickness=0)

    size_ = 60
    i = size_

    ddd = createbubble_image((i, i), None, "black", "orange", "yellow")

    c.create_rectangle(5, 5, size_/2+10, size_/2+10, fill="darkcyan")
    c.create_image(size_/2+10, size_/2+10, image=ddd)
    c.pack(fill=BOTH, expand=True)
    root.mainloop()
