import tkinter as tk
from tkinter import *
from database import Database


class mainPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        # self.master = master
        self.anasayfa = tk.Frame(self)
        self.anasayfa.pack(pady=20)
        tk.Label(self.anasayfa, text="PENCERE ANASAYFA GİRİŞ EKRANI").pack(side="top", fill="x", pady=10)


if __name__ == "__main__":
    app = mainPage()
    app.mainloop()
