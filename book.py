import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from tkinter.ttk import Combobox
from database import Database
import re
from datetime import date, timedelta


class Book(tk.Frame):
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

        self.db.im.execute("SELECT book_ID, book_isbn, book_name, book_author,\
                book_issue, book_page_number, book_category\
                FROM books ORDER BY book_name")
        self.data = self.db.im.fetchall()

        def records():
            bkrecords = self.search_entry.get()
            bk_query = "SELECT * FROM books WHERE book_name LIKE '%"+bkrecords+"%' OR book_author LIKE '%"+bkrecords+"%' OR book_category LIKE '%"+bkrecords+"%'"
            self.db.im.execute(bk_query)
            bk_data = self.db.im.fetchall()
            guncelle(bk_data)

        # Create Label Frame
        self.search_frame = tk.Frame(self)
        self.search_frame.pack(padx=10, pady=10, expand="yes", fill="x", side="top")

        self.search_entry = tk.Entry(self.search_frame, font=("Helvetica", 14))
        self.search_entry.pack(side="left")

        self.ara_button = tk.Button(self.search_frame, text="Ara", command=records)
        self.ara_button.pack(side="left")

        # Student Table Frame
        self.F_Book_table = tk.Frame(self)
        self.F_Book_table.pack(pady=0, padx=10, side="top")

        tree_scroll = tk.Scrollbar(self.F_Book_table)
        tree_scroll.pack(side=RIGHT, fill=Y)

        self.bk_tree = ttk.Treeview(self.F_Book_table, columns=(1, 2, 3, 4, 5, 6, 7), show='headings', yscrollcommand=tree_scroll.set, selectmode="extended", height=10)
        self.bk_tree.pack()
        tree_scroll.config(command=self.bk_tree)
        self.bk_tree["displaycolumns"] = (2, 3, 4, 5, 6, 7)
        self.bk_tree.bind('<<TreeviewSelect>>', self.kayit_sec)

        self.bk_tree.heading(1, text="ID", anchor=CENTER)
        self.bk_tree.heading(2, text="ISBN", anchor=CENTER)
        self.bk_tree.heading(3, text="KİTAP ADI", anchor=CENTER)
        self.bk_tree.heading(4, text="YAZAR", anchor=CENTER)
        self.bk_tree.heading(5, text="BASKI NO", anchor=CENTER)
        self.bk_tree.heading(6, text="SAYFA SAYISI", anchor=CENTER)
        self.bk_tree.heading(7, text="KATEGORİ", anchor=CENTER)

        self.bk_tree.column(1, minwidth=70, width=200, anchor=CENTER)
        self.bk_tree.column(2, minwidth=70, width=200, anchor=CENTER)
        self.bk_tree.column(3, minwidth=70, width=200, anchor=CENTER)
        self.bk_tree.column(4, minwidth=70, width=200, anchor=CENTER)
        self.bk_tree.column(5, minwidth=70, width=130, anchor=CENTER)
        self.bk_tree.column(6, minwidth=70, width=130, anchor=CENTER)
        self.bk_tree.column(7, minwidth=70, width=140, anchor=CENTER)

        self.bk_tree.tag_configure('oddrow', background="white")
        self.bk_tree.tag_configure('evenrow', background="lightblue")

        s = 0
        for i in self.data:
            if s % 2 == 0:
                self.bk_tree.insert(parent='', index='end', iid=s, text='', values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6]), tags=('evenrow',))
            else:
                self.bk_tree.insert(parent='', index='end', iid=s, text='', values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6]), tags=('oddrow',))
            s += 1

        def guncelle(bk_data):
            self.bk_tree.delete(*self.bk_tree.get_children())
            for i in bk_data:
                self.bk_tree.insert("", "end", values=i)

        # TABLO BİLGİLERİ İÇİN LABEL VE ENTRYLER
        data_frame = tk.LabelFrame(self, text=" İŞLEMLER ")
        data_frame.pack(expand="yes", padx=10, pady=0, fill="x", side="top")

        isbn_label = tk.Label(data_frame, text="ISBN")
        isbn_label.grid(row=0, column=0, pady=10, padx=5, sticky="w")
        self.isbn_entry = tk.Entry(data_frame)
        self.isbn_entry.grid(row=0, column=1, pady=10, padx=5, sticky="w")

        name_label = tk.Label(data_frame, text="Kitap Adı")
        name_label.grid(row=0, column=2, pady=5, padx=5, sticky="w")
        self.name_entry = tk.Entry(data_frame)
        self.name_entry.grid(row=0, column=3, padx=5, pady=5, sticky="w")

        author_label = tk.Label(data_frame, text="Yazar")
        author_label.grid(row=0, column=4, pady=10, padx=5, sticky="w")
        self.author_entry = tk.Entry(data_frame)
        self.author_entry.grid(row=0, column=5, pady=10, padx=5, sticky="w")

        issue_label = tk.Label(data_frame, text="Baskı No")
        issue_label.grid(row=0, column=6, pady=10, padx=5, sticky="w")
        self.issue_entry = tk.Entry(data_frame)
        self.issue_entry.grid(row=0, column=7, pady=10, padx=5, sticky="w")

        page_no_label = tk.Label(data_frame, text="Sayfa Sayısı")
        page_no_label.grid(row=1, column=0, pady=10, padx=5, sticky="w")
        self.page_no_entry = tk.Entry(data_frame)
        self.page_no_entry.grid(row=1, column=1, pady=10, padx=5, sticky="w")

        category_label = tk.Label(data_frame, text="Kategori")
        category_label.grid(row=1, column=2, pady=10, padx=5, sticky="w")
        self.category_var = tk.StringVar()
        self.category_list = ['Dünya Klasikleri', 'Psikoloji', 'Roman', 'Din (İslam)', 'Tarih',
                          'Kişisel Gelişim', 'Şiir', 'Felsefe-Düşünce', 'Polisiye', 'Edebiyat']
        self.category_combobox = ttk.Combobox(data_frame, values=self.category_list, height=8, textvariable=self.category_var, width=18)
        self.category_combobox.grid(row=1, column=3, pady=10, padx=5, sticky="w")

        # İŞLEM BUTONLARI FRAME
        self.buton_frame = tk.LabelFrame(self, text=" İŞLEMLER ")
        self.buton_frame.pack(expand="yes", padx=5, pady=5, fill="x", side="bottom")

        self.update_button = tk.Button(self.buton_frame, text="GÜNCELLE", command=self.update, width=13, height=2)
        self.update_button.grid(row=0, column=0, padx=5, pady=5)

        self.add_button = tk.Button(self.buton_frame, text="KİTAP EKLE", command=self.add, width=13, height=2)
        self.add_button.grid(row=0, column=1, padx=5, pady=5)

        self.remove_button = tk.Button(self.buton_frame, text="KİTAP SİL", command=self.delete, width=13, height=2)
        self.remove_button.grid(row=0, column=2, padx=5, pady=5)

        self.clear_button = tk.Button(self.buton_frame, text="TEMİZLE", command=lambda: self.temizle(yenile="yenile"), width=13, height=2)
        self.clear_button.grid(row=0, column=4, padx=5, pady=5)

        self.temizle(yenile="yenile")

        # self.records = self.search_entry.get()
        # for record in self.bk_tree.get_children():
        #     self.bk_tree.delete(record)

        # self.db.im.execute("SELECT * FROM books WHERE book_name LIKE ?", (self.records, ))
        # data = self.db.im.fetchall()

        # s = 0
        # for i in data:
        #     if s % 2 == 0:
        #         self.bk_tree.insert(parent='', index='end', iid=s, text='', values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6]), tags=('evenrow',))
        #     else:
        #         self.bk_tree.insert(parent='', index='end', iid=s, text='', values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6]), tags=('oddrow',))
        #     s += 1

    def kayit_sec(self, event=None):
        self.active()
        self.isbn_entry.delete(0, 'end')
        self.name_entry.delete(0, 'end')
        self.author_entry.delete(0, 'end')
        self.issue_entry.delete(0, 'end')
        self.page_no_entry.delete(0, 'end')
        self.category_combobox.set('')

        selected = self.bk_tree.focus()
        values = self.bk_tree.item(selected, 'values')

        self.isbn_entry.insert(0, values[1])
        self.name_entry.insert(0, values[2])
        self.author_entry.insert(0, values[3])
        self.issue_entry.insert(0, values[4])
        self.page_no_entry.insert(0, values[5])
        self.category_combobox.set(values[6])

    def update(self):
        selected = self.bk_tree.focus()
        values = self.bk_tree.item(selected, 'values')

        isbn = self.isbn_entry.get()
        name = self.name_entry.get().strip().title()
        author = self.author_entry.get().strip().title()
        page_no = self.page_no_entry.get()
        issue = self.issue_entry.get()
        category = self.category_var.get().strip()
        bk_ID = values[0]

        if re.match(" ", isbn) or re.match(" ", issue) or re.match(" ", page_no) or re.match(" ", category):
            messagebox.showwarning("Uyarı", "Lütfen girdiğiniz bilgilerin boşluk içermediğinden emin olun.", parent=self)
        else:
            for i in self.category_list:
                if i == category:
                    edit = self.db.EditBook(name, author, int(issue), int(page_no), category, int(bk_ID))
                    if edit:
                        messagebox.showinfo("Başarılı", "Kitap Güncelleme işlemi başarılı bir şekilde tamamlandı", parent=self)
                        self.temizle(yenile="yenile")
                    else:
                        messagebox.showerror("Başarısız", "Kitap Güncelleme işlemi başarısız oldu.", parent=self)

    def add(self):
        isbn = self.isbn_entry.get()
        name = self.name_entry.get().strip().title()
        author = self.author_entry.get().strip().title()
        page_no = self.page_no_entry.get()
        issue = self.issue_entry.get()
        category = self.category_var.get().strip()
        record_date = date.today()

        if isbn == "" or name == "" or author == "" or issue == "" or page_no == "" or category == "":
            messagebox.showwarning("Uyarı", "Lütfen bütün bilgileri girdiğinizden emin olun...")
        else:
            # if name.isalpha():
            if re.match(" ", isbn) or re.match(" ", issue) or re.match(" ", page_no) or re.match(" ", category):
                messagebox.showwarning("Uyarı", "Lütfen girdiğiniz bilgilerin boşluk içermediğinden emin olun.", parent=self)
            else:
                for i in self.category_list:
                    if i == category:
                        add = self.db.AddBook(isbn, name, author, int(issue), int(page_no), category, record_date)
                        if add:
                            messagebox.showinfo("Başarılı", "Kitap kaydetme işlemi başarılı bir şekilde tamamlandı", parent=self)
                            self.temizle(yenile="yenile")
                        else:
                            messagebox.showerror("Başarısız", "Kitap kaydetme işlemi başarısız oldu.", parent=self)
#             else:
                # messagebox.showerror("Hata", "Lütfen Kitap bilgilerini kontrol edip tekrar deneyiniz", parent=self)

    def delete(self):
        selected = self.bk_tree.focus()
        values = self.bk_tree.item(selected, 'values')

        sor = messagebox.askyesno("Sil", "Seçili Kitapyi silmek istediğinizden eminmisiniz?", parent=self)
        if sor:
            sil = self.db.DelStudent(values[0])
            if sil:
                messagebox.showinfo("Başarılı", "Kitap kayıt silme işlemi başarılı bir şekilde gerçekleşti", parent=self)
                self.temizle(yenile="yenile")
            else:
                messagebox.showerror("Hata", "Kitap silme işlemi gerçekleştirilemedi!", parent=self)

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
        self.isbn_entry.delete(0, 'end')
        self.name_entry.delete(0, 'end')
        self.author_entry.delete(0, 'end')
        self.issue_entry.delete(0, 'end')
        self.page_no_entry.delete(0, 'end')
        self.category_combobox.set('')

    def tablo_yenile(self):
        self.db.im.execute("SELECT book_ID, book_isbn, book_name, book_author,\
                book_issue, book_page_number, book_category\
                FROM books ORDER BY book_name")
        self.data = self.db.im.fetchall()

        for i in self.bk_tree.get_children():
            self.bk_tree.delete(i)

        s = 0
        for i in self.data:
            if s % 2 == 0:
                self.bk_tree.insert(parent='', index='end', iid=s, text='', values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6]), tags=('evenrow',))
            else:
                self.bk_tree.insert(parent='', index='end', iid=s, text='', values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6]), tags=('oddrow',))
            s += 1


if __name__ == "__main__":
    app = Book()
    app.mainloop()
