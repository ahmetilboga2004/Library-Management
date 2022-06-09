import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from database import Database
from datetime import date, timedelta
from student import Student
from book import Book


class giveBook(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.db = Database()

        self.bookTable()
        self.studentTable()

        self.giveFrame = tk.Frame(self)
        self.giveFrame.pack(expand=1, padx=5, pady=1, side="bottom")

        hbox = self.row(self.giveFrame)
        teslim_et = self.thing(tk.Button, hbox, text="TESLİM ET", command=self.give_book, width=15, height=2, cursor="hand2")

        # TABLO BİLGİLERİ İÇİN LABEL VE ENTRYLER
        st_data_frame = tk.LabelFrame(self, text="ÖĞRENCİ BİLGİLERİ")
        st_data_frame.pack(expand="yes", padx=0, pady=0, fill="x", side="bottom")

        st_name_label = tk.Label(st_data_frame, text="Ad :")
        st_name_label.grid(row=0, column=0, pady=2, padx=2, sticky="e")
        self.st_name_var = tk.StringVar()
        self.st_name_var.set("")
        self.st_name_entry = tk.Entry(st_data_frame, textvariable=self.st_name_var, state="readonly")
        self.st_name_entry.grid(row=0, column=1, padx=5, pady=2, sticky="w")

        surname_label = tk.Label(st_data_frame, text="Soyad :")
        surname_label.grid(row=0, column=2, pady=2, padx=5, sticky="e")
        self.surname_var = tk.StringVar()
        self.surname_var.set("")
        self.surname_entry = tk.Entry(st_data_frame, textvariable=self.surname_var, state="readonly")
        self.surname_entry.grid(row=0, column=3, pady=10, padx=5, sticky="w")

        no_label = tk.Label(st_data_frame, text="Okul No :")
        no_label.grid(row=0, column=4, pady=2, padx=5, sticky="e")
        self.no_var = tk.StringVar()
        self.no_var.set("")
        self.no_entry = tk.Entry(st_data_frame, textvariable=self.no_var, state="readonly")
        self.no_entry.grid(row=0, column=5, pady=2, padx=5, sticky="w")

        class_label = tk.Label(st_data_frame, text="Sınıf :")
        class_label.grid(row=1, column=0, pady=5, padx=5, sticky="e")
        self.class_var = tk.StringVar()
        self.class_var.set("")
        self.st_class = tk.Entry(st_data_frame, textvariable=self.class_var, state="readonly")
        self.st_class.grid(row=1, column=1, pady=5, padx=5, sticky="w")

        gender_label = tk.Label(st_data_frame, text="Cinsiyet :")
        gender_label.grid(row=1, column=2, pady=5, padx=5, sticky="e")
        self.gender_var = tk.StringVar()
        self.gender_var.set("")
        self.gender_entry = tk.Entry(st_data_frame, textvariable=self.gender_var, state="readonly")
        self.gender_entry.grid(row=1, column=3, pady=5, padx=10, sticky="w")

        # TABLO BİLGİLERİ İÇİN LABEL VE ENTRYLER
        bk_data_frame = tk.LabelFrame(self, text="KİTAP BİLGİLERİ")
        bk_data_frame.pack(expand="yes", padx=0, pady=5, fill="x", side="bottom")

        isbn_label = tk.Label(bk_data_frame, text="ISBN :")
        isbn_label.grid(row=0, column=0, pady=5, padx=5, sticky="e")
        self.isbn_var = tk.StringVar()
        self.isbn_var.set("")
        self.isbn_entry = tk.Entry(bk_data_frame, textvariable=self.isbn_var, state="readonly")
        self.isbn_entry.grid(row=0, column=1, pady=5, padx=5, sticky="w")

        bk_name_label = tk.Label(bk_data_frame, text="Kitap Adı :")
        bk_name_label.grid(row=0, column=2, pady=5, padx=5, sticky="e")
        self.bk_name_var = tk.StringVar()
        self.bk_name_var.set("")
        self.bk_name_entry = tk.Entry(bk_data_frame, textvariable=self.bk_name_var, state="readonly")
        self.bk_name_entry.grid(row=0, column=3, padx=5, pady=5, sticky="w")

        author_label = tk.Label(bk_data_frame, text="Yazar :")
        author_label.grid(row=0, column=4, pady=5, padx=5, sticky="e")
        self.author_var = tk.StringVar()
        self.author_var.set("")
        self.author_entry = tk.Entry(bk_data_frame, textvariable=self.author_var, state="readonly")
        self.author_entry.grid(row=0, column=5, pady=5, padx=5, sticky="w")

        issue_label = tk.Label(bk_data_frame, text="Baskı No :")
        issue_label.grid(row=1, column=0, pady=5, padx=5, sticky="e")
        self.issue_var = tk.StringVar()
        self.issue_var.set("")
        self.issue_entry = tk.Entry(bk_data_frame, textvariable=self.issue_var, state="readonly")
        self.issue_entry.grid(row=1, column=1, pady=5, padx=5, sticky="w")

        page_no_label = tk.Label(bk_data_frame, text="Sayfa Sayısı :")
        page_no_label.grid(row=1, column=2, pady=5, padx=5, sticky="e")
        self.page_no_var = tk.StringVar()
        self.page_no_var.set("")
        self.page_no_entry = tk.Entry(bk_data_frame, textvariable=self.page_no_var, state="readonly")
        self.page_no_entry.grid(row=1, column=3, pady=5, padx=5, sticky="w")

        category_label = tk.Label(bk_data_frame, text="Kategori :")
        category_label.grid(row=1, column=4, pady=5, padx=5, sticky="e")
        self.category_var = tk.StringVar()
        self.category_var.set("")
        self.category_entry = tk.Entry(bk_data_frame, textvariable=self.category_var, state="readonly")
        self.category_entry.grid(row=1, column=5, pady=5, padx=5, sticky="w")

    def row(self, parent, **kvargs):
        self.row = tk.Frame(parent, **kvargs)
        self.row.pack(expand=1, fill='both', padx=5, pady=5)
        return self.row

    def thing(self, thing_type, parent, **kvargs):
        self.thing = thing_type(parent, **kvargs)
        self.thing.pack(side='left', expand=1, fill='both', padx=5, pady=5)
        return self.thing

    # def ttkstyle(self):
    #     style = ttk.Style()
    #     style.theme_use('default')
    #     style.configure("Treeview",
    #                     background="#D3D3D3",
    #                     foreground="black",
    #                     rowheight=22,
    #                     fieldbackground="#D3D3D3")
    #     style.map("Treeview", background=[('selected', "#347083")])

    def bookTable(self):
        # self.ttkstyle()
        self.db.im.execute("SELECT book_ID, book_isbn, book_name, book_author,\
                book_issue, book_page_number, book_category\
                FROM books ORDER BY book_name")
        self.data = self.db.im.fetchall()

        self.F_Book_table = tk.Frame(self)
        self.F_Book_table.pack(pady=5, padx=10, side="top", fill="x")

        def bk_records():
            bkrecords = self.search_entry.get()

            # for record in self.bk_tree.get_children():
            #     self.bk_tree.delete(record)

            bk_query = "SELECT * FROM books WHERE book_name LIKE '%"+bkrecords+"%' OR book_author LIKE '%"+bkrecords+"%' OR book_category LIKE '%"+bkrecords+"%'"
            self.db.im.execute(bk_query)
            bk_data = self.db.im.fetchall()
            update(bk_data)


        # Create Label Frame
        self.bk_search_frame = tk.Frame(self.F_Book_table)
        self.bk_search_frame.pack(padx=10, pady=0, expand="yes", fill="x", side="top")

        self.search_label = tk.Label(self.bk_search_frame, text="Kitap Ara", font=("Helvetica", 12))
        self.search_label.pack(side="left")

        self.search_entry = tk.Entry(self.bk_search_frame, font=("Helvetica", 12))
        self.search_entry.pack(side="left", padx=5)

        self.ara_button = tk.Button(self.bk_search_frame, text="Ara", command=bk_records)
        self.ara_button.pack(side="left")

        # Student Table Frame
        self.F_Book_frame = tk.Frame(self.F_Book_table)
        self.F_Book_frame.pack(pady=2, padx=10, side="bottom")


        tree_scroll = tk.Scrollbar(self.F_Book_frame)
        tree_scroll.pack(side=RIGHT, fill=Y)

        self.bk_tree = ttk.Treeview(self.F_Book_frame, columns=(1, 2, 3, 4, 5, 6, 7), show='headings', yscrollcommand=tree_scroll.set, height=5)
        self.bk_tree.pack()
        tree_scroll.config(command=self.bk_tree)
        self.bk_tree["displaycolumns"] = (2, 3, 4, 5, 6, 7)
        self.bk_tree.bind('<<TreeviewSelect>>', self.book_sec)

        self.bk_tree.heading(1, text="ID", anchor="center")
        self.bk_tree.heading(2, text="ISBN", anchor="center")
        self.bk_tree.heading(3, text="KİTAP ADI", anchor="center")
        self.bk_tree.heading(4, text="YAZAR", anchor="center")
        self.bk_tree.heading(5, text="BASKI NO", anchor="center")
        self.bk_tree.heading(6, text="SAYFA SAYISI", anchor="center")
        self.bk_tree.heading(7, text="KATEGORİ", anchor="center")

        self.bk_tree.column(1, minwidth=5, width=10, anchor="center")
        self.bk_tree.column(2, minwidth=70, width=150, anchor="center")
        self.bk_tree.column(3, minwidth=70, width=200, anchor="center")
        self.bk_tree.column(4, minwidth=70, width=200, anchor="center")
        self.bk_tree.column(5, minwidth=70, width=110, anchor="center")
        self.bk_tree.column(6, minwidth=70, width=120, anchor="center")
        self.bk_tree.column(7, minwidth=70, width=100, anchor="center")

        color_odd = self.bk_tree.tag_configure('oddrow', background="white")
        color_even = self.bk_tree.tag_configure('evenrow', background="lightblue")

        s = 0
        for i in self.data:
            if s % 2 == 0:
                self.bk_tree.insert(parent='', index='end', iid=s, text='', values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6]), tags=('evenrow',))
            else:
                self.bk_tree.insert(parent='', index='end', iid=s, text='', values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6]), tags=('oddrow',))
            s += 1

        def update(bk_data):
            self.bk_tree.delete(*self.bk_tree.get_children())
            s = 0
            for i in bk_data:
                self.bk_tree.insert("","end",values=i)

    def studentTable(self):
        # self.ttkstyle()
        self.db.im.execute("SELECT student_ID, student_name, student_surname,\
                student_no, student_class, student_gender\
                FROM students ORDER BY student_name")
        self.data = self.db.im.fetchall()

        # Student Table Frame
        self.F_Student_table = tk.Frame(self)
        self.F_Student_table.pack(pady=5, padx=10, side="top", fill="x")

        # Create Label Frame
        self.search_frame = tk.Frame(self.F_Student_table)
        self.search_frame.pack(padx=10, pady=0, expand="yes", fill="x", side="top")

        self.search_label = tk.Label(self.search_frame, text="Öğrenci Ara", font=("Helvetica", 12))
        self.search_label.pack(side="left")

        self.search_entry = tk.Entry(self.search_frame, font=("Helvetica", 12))
        self.search_entry.pack(side="left", padx=5)

        self.ara_button = tk.Button(self.search_frame, text="Ara", command=self.st_records)
        self.ara_button.pack(side="left")

        # Student Table Frame
        self.F_Student_frame = tk.Frame(self.F_Student_table)
        self.F_Student_frame.pack(pady=2, padx=10, side="top")

        tree_scroll = tk.Scrollbar(self.F_Student_frame)
        tree_scroll.pack(side=RIGHT, fill=Y)

        self.st_tree = ttk.Treeview(self.F_Student_frame, columns=(1, 2, 3, 4, 5, 6), show='headings', yscrollcommand=tree_scroll.set, selectmode="extended", height=5)
        self.st_tree.pack()
        tree_scroll.config(command=self.st_tree)
        self.st_tree["displaycolumns"] = (2, 3, 4, 5, 6)
        self.st_tree.bind('<<TreeviewSelect>>', self.student_sec)

        self.st_tree.heading(1, text="ID", anchor="center")
        self.st_tree.heading(2, text="AD", anchor="center")
        self.st_tree.heading(3, text="SOYAD", anchor="center")
        self.st_tree.heading(4, text="OKUL NO", anchor="center")
        self.st_tree.heading(5, text="SINIF", anchor="center")
        self.st_tree.heading(6, text="CİNSİYET", anchor="center")

        self.st_tree.column(1, minwidth=5, width=10, anchor="center")
        self.st_tree.column(2, minwidth=70, width=205, anchor="center")
        self.st_tree.column(3, minwidth=70, width=205, anchor="center")
        self.st_tree.column(4, minwidth=70, width=160, anchor="center")
        self.st_tree.column(5, minwidth=70, width=150, anchor="center")
        self.st_tree.column(6, minwidth=70, width=160, anchor="center")

        self.st_tree.tag_configure('oddrow', background="white")
        self.st_tree.tag_configure('evenrow', background="lightblue")
        self.st_tree.tag_configure('timefive', background="#ff9b43")
        self.st_tree.tag_configure('timefinish', background="#ff4141")

        s = 0
        for i in self.data:
            if s % 2 == 0:
                self.st_tree.insert(parent='', index='end', iid=s, text='', values=(i[0], i[1], i[2], i[3], i[4], i[5]), tags=('evenrow',))
            else:
                self.st_tree.insert(parent='', index='end', iid=s, text='', values=(i[0], i[1], i[2], i[3], i[4], i[5]), tags=('oddrow',))
            s += 1


    def book_sec(self, event=None):
        self.bk_clear()

        bk_selected = self.bk_tree.focus()
        bk_values = self.bk_tree.item(bk_selected, 'values')

        self.isbn_var.set(bk_values[1])
        self.bk_name_var.set(bk_values[2])
        self.author_var.set(bk_values[3])
        self.issue_var.set(bk_values[4])
        self.page_no_var.set(bk_values[5])
        self.category_var.set(bk_values[6])

    def st_records(self):
        self.strecords = self.search_entry.get()
        for record in self.st_tree.get_children():
            self.st_tree.delete(record)

        self.db.im.execute("SELECT * FROM students WHERE student_name LIKE ?", (self.strecords, ))
        data = self.db.im.fetchall()

        s = 0
        for i in data:
            if s % 2 == 0:
                self.st_tree.insert(parent='', index='end', iid=s, text='', values=(i[0], i[1], i[2], i[3], i[4], i[5]), tags=('evenrow',))
            else:
                self.st_tree.insert(parent='', index='end', iid=s, text='', values=(i[0], i[1], i[2], i[3], i[4], i[5]), tags=('oddrow',))
            s += 1

    def student_sec(self, event=None):
        self.st_clear()

        st_selected = self.st_tree.focus()
        st_values = self.st_tree.item(st_selected, 'values')

        self.st_name_var.set(st_values[1])
        self.surname_var.set(st_values[2])
        self.no_var.set(st_values[3])
        self.class_var.set(st_values[4])
        self.gender_var.set(st_values[5])

    def give_book(self):
        st_selected = self.st_tree.focus()
        st_values = self.st_tree.item(st_selected, 'values')
        bk_selected = self.bk_tree.focus()
        bk_values = self.bk_tree.item(bk_selected, 'values')
        bk_ID = bk_values[0]
        st_ID = st_values[0]

        give_date = date.today()
        take_date = give_date + timedelta(days=10)

        if self.st_name_entry.get() == "" or self.bk_name_entry.get() == "":
            messagebox.showwarning("Uyarı", "Lütfen tablodan Öğrenci ve Kitap seçimi yapınız.")
        else:
            give = self.db.GiveBook(st_ID, bk_ID, take_date, give_date)
            if give:
                messagebox.showinfo("Başarılı", "Kitap teslim etme işlemi başarılı bir şekilde gerçekleşti.")
                self.st_name_var.set("")
                self.surname_var.set("")
                self.no_var.set("")
                self.class_var.set("")
                self.gender_var.set("")

                self.isbn_var.set("")
                self.bk_name_var.set("")
                self.author_var.set("")
                self.issue_var.set("")
                self.page_no_var.set("")
                self.category_var.set("")
            else:
                messagebox.showerror("Hata", "Seçmiş olduğunuz öğrencide kitap bulunmaktadır\
                    veya seçmiş olduğunuz kitap şuan dışarda.")

    def st_clear(self):
        self.surname_entry.delete(0, "end")
        self.no_entry.delete(0, "end")
        self.st_class.delete(0, "end")
        self.gender_entry.delete(0, "end")

    def bk_clear(self):
        self.isbn_entry.delete(0, 'end')
        self.bk_name_entry.delete(0, 'end')
        self.author_entry.delete(0, 'end')
        self.issue_entry.delete(0, 'end')
        self.page_no_entry.delete(0, 'end')
        self.category_entry.delete(0, 'end')
        self.st_name_entry.delete(0, "end")

if __name__ == "__main__":
    app = giveBook()
    app.mainloop()
