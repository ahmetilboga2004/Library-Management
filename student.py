import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from tkinter.ttk import Combobox
from database import Database
import re
from datetime import date, timedelta


class Student(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.db = Database()
        style = ttk.Style()
        style.theme_use('default')
        style.configure("Treeview",
                        background="#D3D3D3",
                        foreground="black",
                        rowheight=25,
                        fieldbackground="#D3D3D3")
        style.map("Treeview", background=[('selected', "#347083")])

        self.db.im.execute("SELECT student_ID, student_name, student_surname,\
                student_no, student_class, student_gender\
                FROM students ORDER BY student_name")
        self.data = self.db.im.fetchall()

        # Create Label Frame
        self.search_frame = tk.Frame(self)
        self.search_frame.pack(padx=10, pady=10, expand="yes", fill="x", side="top")

        self.search_entry = tk.Entry(self.search_frame, font=("Helvetica", 14))
        self.search_entry.pack(side="left")

        self.ara_button = tk.Button(self.search_frame, text="Ara", command=self.records)
        self.ara_button.pack(side="left")

        # Student Table Frame
        self.F_Student_table = tk.Frame(self)
        self.F_Student_table.pack(pady=0, padx=10, side="top")


        tree_scroll = tk.Scrollbar(self.F_Student_table)
        tree_scroll.pack(side=RIGHT, fill=Y)

        self.st_tree = ttk.Treeview(self.F_Student_table, columns=(1, 2, 3, 4, 5, 6), show='headings', yscrollcommand=tree_scroll.set, selectmode="extended", height=10)
        self.st_tree.pack()
        tree_scroll.config(command=self.st_tree)
        self.st_tree["displaycolumns"] = (2, 3, 4, 5, 6)
        self.st_tree.bind('<<TreeviewSelect>>', self.kayit_sec)

        self.st_tree.heading(1, text="ID", anchor=CENTER)
        self.st_tree.heading(2, text="AD", anchor=CENTER)
        self.st_tree.heading(3, text="SOYAD", anchor=CENTER)
        self.st_tree.heading(4, text="OKUL NO", anchor=CENTER)
        self.st_tree.heading(5, text="SINIF", anchor=CENTER)
        self.st_tree.heading(6, text="CİNSİYET", anchor=CENTER)

        self.st_tree.column(1, minwidth=120, width=200, anchor=CENTER)
        self.st_tree.column(2, minwidth=120, width=200, anchor=CENTER)
        self.st_tree.column(3, minwidth=120, width=200, anchor=CENTER)
        self.st_tree.column(4, minwidth=120, width=200, anchor=CENTER)
        self.st_tree.column(5, minwidth=100, width=200, anchor=CENTER)
        self.st_tree.column(6, minwidth=100, width=200, anchor=CENTER)

        self.st_tree.tag_configure('oddrow', background="white")
        self.st_tree.tag_configure('evenrow', background="lightblue")

        s = 0
        for i in self.data:
            if s % 2 == 0:
                self.st_tree.insert(parent='', index='end', iid=s, text='', values=(i[0], i[1], i[2], i[3], i[4], i[5]), tags=('evenrow',))
            else:
                self.st_tree.insert(parent='', index='end', iid=s, text='', values=(i[0], i[1], i[2], i[3], i[4], i[5]), tags=('oddrow',))
            s += 1

        # TABLO BİLGİLERİ İÇİN LABEL VE ENTRYLER
        data_frame = tk.LabelFrame(self, text=" İŞLEMLER ")
        data_frame.pack(expand="yes", padx=10, pady=0, fill="x", side="top")

        name_label = tk.Label(data_frame, text="Ad")
        name_label.grid(row=0, column=0, pady=5, padx=5, sticky="w")
        self.name_entry = tk.Entry(data_frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        surname_label = tk.Label(data_frame, text="Soyad")
        surname_label.grid(row=0, column=2, pady=10, padx=5, sticky="w")
        self.surname_entry = tk.Entry(data_frame)
        self.surname_entry.grid(row=0, column=3, pady=10, padx=5, sticky="w")

        no_label = tk.Label(data_frame, text="Okul No")
        no_label.grid(row=0, column=4, pady=10, padx=5, sticky="w")
        self.no_entry = tk.Entry(data_frame)
        self.no_entry.grid(row=0, column=5, pady=10, padx=5, sticky="w")

        class_label = tk.Label(data_frame, text="Sınıf")
        class_label.grid(row=1, column=0, pady=10, padx=5, sticky="w")
        self.class_var = tk.StringVar()
        self.classlist = ['9/A', '9/B', '10/A', '10/B', '11/A',
                          '11/B', '12/A', '12/B', '12/A FEN', '12/B FEN']
        self.class_combobox = ttk.Combobox(data_frame, values=self.classlist, height=8, textvariable=self.class_var, width=18)
        self.class_combobox.grid(row=1, column=1, pady=10, padx=5, sticky="w")

        gender_label = tk.Label(data_frame, text="Cinsiyet")
        gender_label.grid(row=1, column=2, pady=10, padx=5, sticky="w")
        self.gender_var = tk.StringVar()
        self.gender_var.set("")
        gender_male = tk.Radiobutton(data_frame, text="Kız ", value="Kız", variable=self.gender_var)
        gender_male.grid(row=1, column=3, pady=10, sticky="w")
        gender_female = tk.Radiobutton(data_frame, text="Erkek ", value="Erkek", variable=self.gender_var)
        gender_female.grid(row=1, column=3, pady=10, sticky="s")

        # İŞLEM BUTONLARI FRAME
        self.buton_frame = tk.LabelFrame(self, text=" İŞLEMLER ")
        self.buton_frame.pack(expand="yes", padx=5, pady=5, fill="x", side="bottom")

        self.update_button = tk.Button(self.buton_frame, text="GÜNCELLE", command=self.update, width=13, height=2)
        self.update_button.grid(row=0, column=0, padx=5, pady=5)

        self.add_button = tk.Button(self.buton_frame, text="ÖĞRENCİ EKLE", command=self.add, width=13, height=2)
        self.add_button.grid(row=0, column=1, padx=5, pady=5)

        self.remove_button = tk.Button(self.buton_frame, text="ÖĞRENCİ SİL", command=self.delete, width=13, height=2)
        self.remove_button.grid(row=0, column=2, padx=5, pady=5)

        self.clear_button = tk.Button(self.buton_frame, text="TEMİZLE", command=lambda: self.temizle(yenile="yenile"), width=13, height=2)
        self.clear_button.grid(row=0, column=4, padx=5, pady=5)

        self.temizle(yenile="yenile")

    def records(self):
        self.records = self.search_entry.get()
        for record in self.st_tree.get_children():
            self.st_tree.delete(record)

        self.db.im.execute("SELECT * FROM students WHERE student_name LIKE ?", (self.records, ))
        data = self.db.im.fetchall()

        s = 0
        for i in data:
            if s % 2 == 0:
                self.st_tree.insert(parent='', index='end', iid=s, text='', values=(i[0], i[1], i[2], i[3], i[4], i[5]), tags=('evenrow',))
            else:
                self.st_tree.insert(parent='', index='end', iid=s, text='', values=(i[0], i[1], i[2], i[3], i[4], i[5]), tags=('oddrow',))
            s += 1

    def kayit_sec(self, event=None):
        self.active()
        self.name_entry.delete(0, "end")
        self.surname_entry.delete(0, "end")
        self.no_entry.delete(0, "end")
        self.class_combobox.set('')

        selected = self.st_tree.focus()
        values = self.st_tree.item(selected, 'values')

        self.name_entry.insert(0, values[1])
        self.surname_entry.insert(0, values[2])
        self.no_entry.insert(0, values[3])
        self.class_combobox.set(values[4])
        if values[5] == "Erkek":
            self.gender_var.set('Erkek')
        if values[5] == "Kız":
            self.gender_var.set('Kız')

    def update(self):
        selected = self.st_tree.focus()
        values = self.st_tree.item(selected, 'values')

        name = self.name_entry.get().strip().title()
        surname = self.surname_entry.get().strip().title()
        no = self.no_entry.get().strip()
        stclass = self.class_var.get().strip()
        gender = self.gender_var.get().strip()
        st_ID = values[0]

        if name.isalpha() and surname.isalpha():
            if re.match(" ", surname) or re.match(" ", no) or re.match(" ", stclass):
                messagebox.showwarning("Uyarı", "Lütfen girdiğiniz bilgilerin boşluk içermediğinden emin olun.", parent=self)
            else:
                for i in self.classlist:
                    if i == stclass:
                        if gender == "":
                            messagebox.showwarning("Uyarı", "Lütfen Öğrenci cinsiyetini seçiniz", parent=self)
                        else:
                            edit = self.db.EditStudent(name, surname, int(no), stclass, gender, int(st_ID))
                            if edit:
                                messagebox.showinfo("Başarılı", "Öğrenci Güncelleme işlemi başarılı bir şekilde tamamlandı", parent=self)
                                self.temizle(yenile="yenile")
                            else:
                                messagebox.showerror("Başarısız", "Öğrenci Güncelleme işlemi başarısız oldu.", parent=self)
        else:
            messagebox.showerror("Hata", "Lütfen girdiğiniz verileri kontrol edip tekrar deneyiniz", parent=self)

    def add(self):
        name = self.name_entry.get().strip().title()
        surname = self.surname_entry.get().title()
        no = self.no_entry.get()
        stclass = self.class_var.get()
        gender = self.gender_var.get()
        record_date = date.today()

        if name == "" or surname == "" or no == "" or stclass == "" or gender == "":
            messagebox.showwarning("Uyarı", "Lütfen bütün bilgileri girdiğinizden emin olun...")
        else:
            if name.isalpha() and surname.isalpha():
                if re.match(" ", surname) or re.match(" ", no) or re.match(" ", stclass):
                    messagebox.showwarning("Uyarı", "Lütfen girdiğiniz bilgilerin boşluk içermediğinden emin olun.", parent=self)
                else:
                    for i in self.classlist:
                        if i == stclass:
                            if gender == "":
                                messagebox.showwarning("Uyarı", "Lütfen öğrenci cinsiyetini belirtip tekrar deneyiniz", parent=self)
                            else:
                                add = self.db.AddStudent(name, surname, int(no), stclass, gender, record_date)
                                if add:
                                    messagebox.showinfo("Başarılı", "Öğrenci kaydetme işlemi başarılı bir şekilde tamamlandı", parent=self)
                                    self.temizle(yenile="yenile")
                                else:
                                    messagebox.showerror("Başarısız", "Öğrenci kaydetme işlemi başarısız oldu.", parent=self)
            else:
                messagebox.showerror("Hata", "Lütfen Öğrenci bilgilerini kontrol edip tekrar deneyiniz", parent=self)

    def delete(self):
        selected = self.st_tree.focus()
        values = self.st_tree.item(selected, 'values')

        sor = messagebox.askyesno("Sil", "Seçili Öğrenciyi silmek istediğinizden eminmisiniz?", parent=self)
        if sor:
            sil = self.db.DelStudent(values[0])
            if sil:
                messagebox.showinfo("Başarılı", "Öğrenci kayıt silme işlemi başarılı bir şekilde gerçekleşti", parent=self)
                self.temizle(yenile="yenile")
            else:
                messagebox.showerror("Hata", "Öğrenci silme işlemi gerçekleştirilemedi!", parent=self)

    def active(self):
        self.update_button.config(state="normal", cursor="hand2")
        self.remove_button.config(state="normal", cursor="hand2")
        self.add_button.config(state="disabled", cursor="hand2")

    def temizle(self, yenile=""):
        if yenile == "yenile":
            self.tablo_yenile()
        self.update_button.config(state="disabled", cursor="hand2")
        self.remove_button.config(state="disabled", cursor="hand2")
        self.add_button.config(state="normal", cursor="hand2")
        self.clear_button.config(state="normal", cursor="hand2")
        self.name_entry.delete(0, "end")
        self.surname_entry.delete(0, "end")
        self.no_entry.delete(0, "end")
        self.class_combobox.set("")
        self.gender_var.set("")

    def tablo_yenile(self):
        self.db.im.execute("SELECT student_ID, student_name, student_surname,\
                student_no, student_class, student_gender\
                FROM students ORDER BY student_name")
        self.data = self.db.im.fetchall()

        for i in self.st_tree.get_children():
            self.st_tree.delete(i)

        s = 0
        for i in self.data:
            if s % 2 == 0:
                self.st_tree.insert(parent='', index='end', iid=s, text='', values=(i[0], i[1], i[2], i[3], i[4], i[5]), tags=('evenrow',))
            else:
                self.st_tree.insert(parent='', index='end', iid=s, text='', values=(i[0], i[1], i[2], i[3], i[4], i[5]), tags=('oddrow',))
            s += 1


if __name__ == "__main__":
    app = Student()
    app.mainloop()
