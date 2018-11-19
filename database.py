import sqlite3


def create_functions():
    conn = sqlite3.connect('test_2.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS Students(
                id_tg int,
                last_name varchar(15),
                name varchar(15),
                surname varchar(20),
                zachetka int,
                rating int default 0,
                primary key(id_tg)
                )''')
    conn.commit()
    c.execute('''CREATE TABLE IF NOT EXISTS Admins(
                id int primary key
                )''')
    conn.commit()
    c.execute('''CREATE TABLE IF NOT EXISTS Homework(
                data date,
                dz varchar(45),
                bil varchar check(bil='bil' or bil='ne bil')
                )''')
    conn.commit()
    c.execute('''CREATE TABLE IF NOT EXISTS Proguli(
                data date,
                id_stud int,
                primary key(data, id_stud),
                foreign key(id_stud) references Students(id_tg) on delete cascade
                )''')
    conn.commit()
    conn.close()


def add_info_into_table(table_name, values):
    conn = sqlite3.connect('test_2.db')
    c = conn.cursor()
    quest = "(" + "?, " * (len(values)-1) + "?)"
    c.execute("INSERT INTO " + table_name + " values " + quest, values)
    conn.commit()
    conn.close()


def sign_on_course(values):
    conn = sqlite3.connect('test_2.db')
    c = conn.cursor()
    c.execute("INSERT INTO Students values(?,?,?,?,?,?)", values)
    conn.commit()
    conn.close()


def delete_from_course(id_user):
    conn = sqlite3.connect('test_2.db')
    c = conn.cursor()
    c.execute("DELETE FROM Students where id_tg="+str(id_user))
    conn.commit()
    conn.close()


def show_table(table_name):
    conn = sqlite3.connect('test_2.db')
    c = conn.cursor()
    c.execute("SELECT * FROM " + table_name)
    row = c.fetchone()
    while row is not None:
        print(row)
        row = c.fetchone()
    conn.commit()
    conn.close()


def show_info_table(table_name):
    conn = sqlite3.connect('test_2.db')
    c = conn.cursor()
    c.execute("SELECT * FROM " + table_name)
    print(c.fetchone())
    conn.commit()
    conn.close()


def get_rating(user_id):
    conn = sqlite3.connect('test_2.db')
    c = conn.cursor()
    c.execute("SELECT last_name FROM Students where id_tg="+user_id)
    conn.commit()
    conn.close()
