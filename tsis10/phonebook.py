import sqlite3 as sq

csv = "Popa,+77012462853,15,AbylaiKhan Avenue"

def splitter(str):
  str = tuple(str.split(","))
  return str


with sq.connect('phonebook.db') as con:
  cur = con.cursor()
  cur.execute("CREATE TABLE IF NOT EXISTS phonebook(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, phone TEXT, age INTEGER, adress TEXT NOT NULL)")

  cur.execute("INSERT INTO phonebook (name, phone, age, adress) VALUES (?, ?, ?, ?)", splitter(csv))

  # n = input()
  # p = input()
  # ag = input()
  # a = input()
  # cur.execute("INSERT INTO phonebook VALUES (?, ?, ?, ?)", (n, p, ag, a))

  # change_key = input('Input Key To Change ')
  # new_key = input('Input New Key ')
  # cur.execute("SELECT * FROM phonebook")
  # atts = cur.fetchall()
  # change_id = 0
  # att = ''
  # for i in atts:
  #   k = 0
  #   for j in i:
  #     if j == change_key:
  #       change_id = i[0]
  #       if k == 1:
  #         print("name")
  #         cur.execute("UPDATE phonebook SET name = ? WHERE id = ?", (new_key, change_id))
  #       if k == 2:
  #         print("phone")
  #         cur.execute("UPDATE phonebook SET phone = ? WHERE id = ?", (new_key, change_id))
  #       break
  #     k+=1
  
  # cur.execute("SELECT * FROM phonebook WHERE age BETWEEN 18 AND 100")
  # print(cur.fetchall())

  # del_key = input('Input Key To Delete ')
  # cur.execute("SELECT * FROM phonebook")
  # atts = cur.fetchall()
  # del_id = 0
  # for i in atts:
  #   for j in i:
  #     if j == del_key:
  #       cur.execute("DELETE FROM phonebook WHERE id = ?", (i[0],))
  #       break
