import sqlite3

db = sqlite3.connect("contacts.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contacts(name, phone, email) VALUES('Emilio', 31312434, 'ea3@mail.com')")
db.execute("INSERT INTO contacts VALUES('Brian', 234234, 'brian@mail.com')")

cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")
for row in cursor:
    print(row)

cursor.close()


db.close()







