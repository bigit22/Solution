import sqlite3


def test(db_name: str):
    connection = sqlite3.connect('db.sqlite3')
    cursor = connection.cursor()
    print("Table: ApplicationInformation")
    cursor.execute('''SELECT * FROM ApplicationInformation''')
    for row in cursor.fetchall():
        print(row)

    print("\nTable: Subject")
    cursor.execute('''SELECT * FROM Subject''')
    for row in cursor.fetchall():
        print(row)

    print("\nTable: RegistrationAddress")
    cursor.execute('''SELECT * FROM RegistrationAddress''')
    for row in cursor.fetchall():
        print(row)

    print("\nTable: SubjectList")
    cursor.execute('''SELECT * FROM SubjectList''')
    for row in cursor.fetchall():
        print(row)