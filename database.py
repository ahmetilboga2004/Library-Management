from curses.ascii import isalnum
import sqlite3


class Database:
    def __init__(self):
        super().__init__()
        self.vt = sqlite3.connect("library.sql3")
        self.im = self.vt.cursor()
        self.AdminTable()
        self.StudentTable()
        self.BookTable()
        self.StudentBookTable()

    # Admin tablosu oluşturma fonksiyonu.
    def AdminTable(self):
        self.im.execute("""CREATE TABLE IF NOT EXISTS admins (
            admin_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            admin_name TEXT DEFAULT 'admin',
            admin_pass TEXT DEFAULT 'pass')""")
        self.vt.commit()

    # Yeni yönetici oluşturma fonskiyonu.
    def AddAdmin(self, admin_name, admin_pass):
        controlAdmin = self.im.execute("SELECT * FROM admins WHERE admin_name = ?", (admin_name, ))
        lengthControl = controlAdmin.fetchall()
        if len(lengthControl) > 0:
            return False
        else:
            self.im.execute("INSERT INTO admins (admin_ID, admin_name, admin_pass) VALUES (null,?,?) ", (admin_name, admin_pass))
            self.vt.commit()
            return True

    # Var olan bir yöneticiyi silme fonskiyonu
    def DelAdmin(self, username):
        delAdmin = self.im.execute("DELETE * FROM admins WHERE username = ?", (username, ))
        self.vt.commit()
        if delAdmin:
            return True
        else:
            return False

    # Yönetici giriş kontrolü fonksiyonu.
    def adminLoginControl(self, username, password):
        if username == '' or password == '':
            return False
        else:
            if username.isalnum() and password.isalnum():
                self.im.execute("SELECT * FROM admins WHERE admin_name = ? AND admin_pass = ? ", (username, password))
                control = self.im.fetchone()
                if control:
                    return True
                else:
                    return False
            else:
                return False

    # Giriş ve diğer işlemleri kayıt edileceği tablo fonksiyonu.
    def logTable(self):
        pass

    # Log tablosuna işlem kaydı ekleme fonksiyonu.
    def addLog(self):
        pass

    # öğrenciler tablosunu oluşturma fonksiyonu.
    def StudentTable(self):
        self.im.execute("""CREATE TABLE IF NOT EXISTS students (
            student_ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            student_name TEXT,
            student_surname TEXT,
            student_no INTEGER,
            student_class TEXT,
            student_gender TEXT,
            student_record_date DATE,
            student_status BOOLEAN DEFAULT 0)""")
        self.vt.commit()

    # Öğrenciler tablosuna öğrenci ekleme fonskiyonu.
    def AddStudent(self, st_name, st_surname, st_no, st_class, st_gender, st_record):
        controlStudent = self.im.execute("SELECT * FROM students WHERE student_name = ? AND student_surname = ? OR student_no = ?", (st_name, st_surname, st_no))
        lengthControl = controlStudent.fetchall()
        if len(lengthControl) > 0:
            return False
        else:
            self.im.execute("""INSERT INTO students (
                student_ID,
                student_name,
                student_surname,
                student_no,
                student_class,
                student_gender,
                student_record_date)
                VALUES (null,?,?,?,?,?,?)""", (st_name, st_surname, st_no, st_class, st_gender, st_record))
            self.vt.commit()
            return True

    # Öğreciler tablosundan öğrenci silme fonskiyonu.
    def DelStudent(self, st_ID):
        delStudent = self.im.execute("DELETE FROM students WHERE student_ID = ?", (st_ID, ))
        self.vt.commit()
        if delStudent:
            return True
        else:
            return False

    # Öğrenciler tablosundaki öğrenci bilgilerini düzenleme fonskiyonu.
    def EditStudent(self, st_name, st_surname, st_no, st_class, st_gender, st_ID):
        editStudent = self.im.execute("""UPDATE students SET
            student_name = ?,
            student_surname = ?,
            student_no = ?,
            student_class = ?,
            student_gender = ?
            WHERE student_ID = ?""", (st_name, st_surname, st_no, st_class, st_gender, st_ID))
        self.vt.commit()
        if editStudent:
            return True
        else:
            return False

    def searchStudent(self, column, search):
        query = "SELECT student_name, student_surname, student_no, student_class, student_gender FROM students WHERE '"+column+"' LIKE '%"+search+"%'"
        self.im.execute(query)

    # Öğrneci bilgilerini getirme fonksiyonu.
    def getStudentInfo(self, st_ID):
        self.im.execute("SELECT * FROM students WHERE student_ID = ?", (st_ID, ))
        self.data = self.im.fetchall()
        return self.data

    # Kitaplar tablosunu oluşturma fonksiyonu.
    def BookTable(self):
        self.im.execute("""CREATE TABLE IF NOT EXISTS books (
            book_ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            book_isbn INTEGER,
            book_name TEXT,
            book_author TEXT,
            book_issue TEXT,
            book_page_number INTEGER,
            book_category TEXT,
            book_record_date DATE,
            book_status BOOLEAN DEFAULT 0) """)
        self.vt.commit()

    # Kitaplar tablosuna kitap ekleme fonskiyonu.
    def AddBook(self, bk_isbn, bk_name, bk_author, bk_issue, bk_page_no, bk_category, bk_record):
        controlBook = self.im.execute("SELECT * FROM books WHERE book_isbn = ? AND book_name = ? AND book_author = ?", (bk_isbn, bk_name, bk_author))
        lengthControl = controlBook.fetchall()
        if len(lengthControl) > 0:
            return False
        else:
            self.im.execute("""INSERT INTO books (
                book_ID,
                book_isbn,
                book_name,
                book_author,
                book_issue,
                book_page_number,
                book_category,
                book_record_date)
                VALUES (null,?,?,?,?,?,?,?)""", (bk_isbn, bk_name, bk_author, bk_issue, bk_page_no, bk_category, bk_record))
            self.vt.commit()
            return True

    # Kitaplar tablsoundan kitap silme fonksiyonu.
    def DelBook(self, bk_ID):
        delBook = self.im.execute("DELETE FROM books WHERE book_isbn = ?", (bk_ID, ))
        self.vt.commit()
        if delBook:
            return True
        else:
            return False

    # Kitaplar tablosundaki kitap bilgilerini düzenlemek fonskiyonu.
    def EditBook(self, bk_name, bk_author, bk_issue, bk_page_no, bk_category, bk_ID):
        editBook = self.im.execute("""UPDATE books SET
            book_name = ?,
            book_author = ?,
            book_issue = ?,
            book_page_number = ?,
            book_category = ?
            WHERE book_ID = ?""", (bk_name, bk_author, bk_issue, bk_page_no, bk_category, bk_ID))
        self.vt.commit()
        if editBook:
            return True
        else:
            return False

    # Kitap alan öğrenciler tablosu oluşturma fonskiyonu.
    def StudentBookTable(self):
        self.im.execute("""CREATE TABLE IF NOT EXISTS StudentBook (
            proccess_ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            student_ID INTEGER,
            book_ID INTEGER,
            take_date DATE,
            give_date DATE,
            FOREIGN KEY (student_ID) REFERENCES students(student_ID) ON DELETE CASCADE ON UPDATE CASCADE,
            FOREIGN KEY (book_ID) REFERENCES books(book_ID) ON DELETE CASCADE ON UPDATE CASCADE)""")
        self.vt.commit()

    # Öğrenciye kitap teslim etme fonskiyonu.
    def GiveBook(self, st_no, bk_ID, take_date, give_date):
        self.im.execute("SELECT * FROM StudentBook WHERE student_ID = ? OR book_ID = ?", (st_no, bk_ID))
        lengthControl = self.im.fetchall()
        if len(lengthControl) > 0:
            return False
        else:
            giveBook = self.im.execute("""INSERT INTO StudentBook(
                proccess_ID,
                student_ID,
                book_ID,
                take_date,
                give_date)
                VALUES (null, ?, ?, ?, ?)""", (st_no, bk_ID, take_date, give_date))
            self.vt.commit()
            if giveBook:
                self.im.execute("UPDATE students SET student_status = 1 WHERE student_no = ?", (st_no, ))
                self.vt.commit()
                self.im.execute("UPDATE books SET book_status = 1 WHERE book_ID = ?", (bk_ID, ))
                self.vt.commit()
                return True
            else:
                return False

    # Alınan kitabı öğrenciden teslim alma fonskiyonu.
    def TakeBook(self, st_ID):
        updateBookStatus = self.im.execute("UPDATE books SET book_status = 0 WHERE book_ID = (SELECT book_ID FROM StudentBook WHERE student_ID = ?)", (st_ID, ))
        self.vt.commit()
        updateStudentStatus = self.im.execute("UPDATE students SET student_status = 0 WHERE student_ID = ?", (st_ID, ))
        self.vt.commit()
        if updateBookStatus and updateStudentStatus:
            delStudent = self.im.execute("DELETE FROM StudentBook WHERE student_ID = ?", (st_ID, ))
            self.vt.commit()
            if delStudent:
                return True
        else:
            return True
        return True
