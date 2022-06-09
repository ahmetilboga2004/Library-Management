import tkinter as tk
from tkinter import *
from database import Database


class takeBook(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        # self.master = master
        self.F_takeBook = tk.Frame(self)
        self.F_takeBook.pack(pady=20)
        tk.Label(self.F_takeBook, text="BURASI KİTAP TESLİM ALMA SAYFASINA AİTTİR").pack(side="top", fill="x", pady=10)


if __name__ == "__main__":
    app = takeBook()
    app.mainloop()
