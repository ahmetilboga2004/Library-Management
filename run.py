#!/usr/bin/python3
# -*- coding: utf-8 -*-

import tkinter as tk
from main import Main
from mainpage import mainPage
from student import Student
from book import Book
from takebook import takeBook
from givebook import giveBook


pages = {
    "Main": Main,
    "MainPage": mainPage,
    "StudentPage": Student,
    "BookPage": Book,
    "GiveBookPage": giveBook,
    "TakeBookPage": takeBook
}


class run(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame("Main")

    def switch_frame(self, page_name):
        """Destroys current frame and replaces it with a new one."""
        cls = pages[page_name]
        new_frame = cls(master=self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


if __name__ == "__main__":
    root = run()
    # ================ WINDOW SETTINGS ================ #
    root.wm_title("MİZANCI MURAT KÜTÜPHANE OTOMASYONU")
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.wm_geometry("%dx%d" % (width, height))
    root.resizable(0, 0)
    root.withdraw()
    root.mainloop()
