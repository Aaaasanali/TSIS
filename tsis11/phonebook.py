import sqlite3 as sq


with sq.connect('phonebook.db') as con:
  cur = con.cursor()
  cur.execute("CREATE TABLE IF NOT EXISTS phonebook(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, phone TEXT)")

  
  # cur.execute("SELECT * FROM phonebook WHERE name LIKE 'Jo%'")
  # print(cur.fetchall())
  # cur.execute("SELECT * FROM phonebook WHERE phone LIKE '+7747%'")
  # print(cur.fetchall())

  # new_name = input('Insert Your Name ')
  # new_phone = input('Insert Your Phone ')
  # cur.execute("SELECT * FROM phonebook")
  # names = cur.fetchall()
  # found = False
  # for i in names:
  #   if i[1] == new_name:
  #     cur.execute("UPDATE phonebook SET phone = ? WHERE name = ?", (new_phone, new_name))
  #     print('You had been already registered, but your phone number is updated')
  #     found = True
  # if not found:
  #   print('You are registered!')
  #   cur.execute("INSERT INTO phonebook (name, phone) VALUES (?, ?)", (new_name, new_phone))

  # lis = [('Anderi', '+77479263120'), ('Klava Koka', '+327198312')]
  # for i in lis:
  #   if len(i[1]) == 12 and i[1][:2] == "+7":
  #     cur.execute("INSERT INTO phonebook (name, phone) VALUES (?,?)", (i[0], i[1]))
  #   else:
  #     print('These values are incorrect:', i)

  # cur.execute("SELECT * FROM phonebook LIMIT 2, 2 ")
  # print(cur.fetchall())

  # delt = input("Name or Phone to delete: ")
  # if delt[:2] == "+7":
  #   cur.execute("DELETE FROM phonebook WHERE phone = ?", (delt,))
  # else:
  #   cur.execute("DELETE FROM phonebook WHERE name = ?", (delt,))
