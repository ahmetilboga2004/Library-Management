from email.mime import image
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from database import Database
from PIL import Image, ImageTk


class Main(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.F_menu = tk.Frame(self.master)
        self.F_menu.pack(pady=10, padx=5)
        self.db = Database()
        self.loginPage()

        # Programın Menu Butonlarını oluşturur.
        self.B_anapencere = tk.Button(self.F_menu, text="Ana Pencere", command=lambda: master.switch_frame("MainPage"),
                                     font="bold", cursor="hand2", fg="red", width=13, height=3)
        self.B_anapencere.grid(row=0, column=1, padx=10)

        self.B_ogrenci = tk.Button(self.F_menu, text="Öğrenci İşlemleri", command=lambda: master.switch_frame("StudentPage"),
                            font="bold", cursor="hand2", fg="red", width=13, height=3)
        self.B_ogrenci.grid(row=0, column=2, padx=10)

        self.B_kitap = tk.Button(self.F_menu, text="Kitap İşlemleri", command=lambda: master.switch_frame("BookPage"), font="bold",
                            cursor="hand2", fg="red", width=13, height=3)
        self.B_kitap.grid(row=0, column=3, padx=10)

        self.B_teslim_al = tk.Button(self.F_menu, text="Teslim Al", command=lambda: master.switch_frame("TakeBookPage"),
                            font="bold", cursor="hand2", fg="red", width=13, height=3)
        self.B_teslim_al.grid(row=0, column=4, padx=10)

        self.B_teslim_ver = tk.Button(self.F_menu, text="Teslim Ver", command=lambda: master.switch_frame("GiveBookPage"),
                            font="bold", cursor="hand2", fg="red", width=13, height=3)
        self.B_teslim_ver.grid(row=0, column=5, padx=10)

    # GİRİŞ PENCERESİ
    def loginPage(self):
        # LOGİN WINDOW
        self.LoginPage = tk.Toplevel(bg="#59984a")
        self.LoginPage.transient()
        self.LoginPage.geometry("400x300")
        self.LoginPage.resizable(width=0, height=0)
        self.master.eval(f'tk::PlaceWindow {str(self.LoginPage)} center')
        self.LoginPage.protocol("WM_DELETE_WINDOW", self.on_closing)

        # LOGİN PAGE FRAME
        self.F_login = tk.Frame(self.LoginPage, bg="#6bb658", highlightthickness=1)
        self.F_login.place(relx=0.5, rely=0.5, anchor="c")

        # USERNAME LABEL
        self.username_label = tk.Label(self.F_login, text="Kulanıcı Adı: ", font="Times 16 bold", bg="#6bb658")
        self.username_label.grid(row=0, column=0, sticky="E", padx=5, pady=5)

        # USERNAME ENTRY
        self.username_entry = tk.Entry(self.F_login, bg="#6bb658")
        self.username_entry.grid(row=0, column=1, padx=5, pady=5)

        # PASSWORD LABEL
        self.password_label = tk.Label(self.F_login, text="Şifre: ", font="Times 16 bold", bg="#6bb658")
        self.password_label.grid(row=1, column=0, sticky="E", padx=5, pady=5)

        # PASSWORD ENTRY
        self.password_entry = tk.Entry(self.F_login, show="*", bg="#6bb658")
        self.password_entry.grid(row=1, column=1, padx=5, pady=5)

        # LOGİN BUTTON
        self.login_button = tk.Button(self.F_login, text="GİRİŞ", bg="#6bb658", activebackground="#59984a", highlightthickness=1, borderwidth=2, highlightbackground="#6bb658", command=self.loginControl)
        self.login_button.grid(row=2, column=1, sticky="E", padx=5, pady=5)
        self.bind_giris = self.LoginPage.bind('<Return>', self.loginControl)

    # Giriş bilgilerini kontrol eden fonskiyon.
    def loginControl(self, event=None):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username == "" or password == "":
            messagebox.showwarning("Uyarı", "Kullanıcı Adı veya Şifre boş bırakılamaz.", parent=self.LoginPage)
        if username.isalnum() and password.isalnum():
            kontrol = self.db.adminLoginControl(username, password)
            if kontrol:
                messagebox.showinfo("", "Giriş işlemi başarılı bir şekilde gerçekleşti.", parent=self.LoginPage)
                self.LoginPage.destroy()
                self.master.switch_frame("MainPage")
                self.master.deiconify()
            else:
                self.username_entry.delete(0, 'end')
                self.password_entry.delete(0, 'end')
                messagebox.showwarning("", "Kullanıcı Adı veya Parola hatalı. Lütfen giriş bilgilerini kontrol ediniz", parent=self.LoginPage)
        else:
            messagebox.showwarning("", "Kullanıcı Adı veya Parola hatalı. Lütfen giriş bilgilerini kontrol ediniz", parent=self.LoginPage)
            self.username_entry.delete(0, 'end')
            self.password_entry.delete(0, 'end')

    def on_closing(self):
        sor = messagebox.askokcancel("Çıkış", "Çıkış yapmak istediğinizden eminmisiniz", parent=self.LoginPage)
        if sor:
            self.LoginPage.destroy()
            self.master.quit()
