import sqlite3


def create_table_application_information(connection: sqlite3.Connection):
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ApplicationInformation (
        Id TEXT PRIMARY KEY,
        CreatedDate DATETIME,
        Strategy TEXT NOT NULL,
        SubjectList 
        )
        ''')
    connection.commit()


def create_table_subject(connection: sqlite3.Connection):
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Subject (
        Id TEXT PRIMARY KEY,
        SubjectIncome REAL,
        SubjectRole TEXT,
        RegistrationAddressId TEXT,
        FOREIGN KEY(RegistrationAddressId) REFERENCES RegistrationAddress(Id)
        )
        ''')
    connection.commit()


def create_table_registration_address(connection: sqlite3.Connection):
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS RegistrationAddress (
        Id TEXT PRIMARY KEY,
        Region TEXT,
        City TEXT,
        House TEXT
        )
        ''')
    connection.commit()


def create_table_subject_list(connection: sqlite3.Connection):
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS SubjectList (
        Id TEXT PRIMARY KEY,
        host_mtype TEXT,
        value_mtype TEXT,
        FOREIGN KEY(host_mtype) REFERENCES ApplicationInformation(Id),
        FOREIGN KEY(value_mtype) REFERENCES Subject(Id)
        )
        ''')
    connection.commit()


def fill_table_application_information(connection: sqlite3.Connection):
    cursor = connection.cursor()
    cursor.executemany('''
        INSERT INTO ApplicationInformation (Id, CreatedDate, Strategy, SubjectList)
        VALUES (?, ?, ?, ?)''', [
            ('1', '2024-03-14', 'Strategy1', '1'),
            ('2', '2024-03-15', 'Strategy2', '2'),
            ('3', '2024-03-16', 'Strategy3', '3'),
            ('4', '2024-03-17', 'Strategy4', '4'),
            ('5', '2024-03-18', 'Strategy5', '5')
            ]
        )
    connection.commit()


def fill_table_subject(connection: sqlite3.Connection):
    cursor = connection.cursor()
    cursor.executemany('''
        INSERT INTO Subject (Id, SubjectIncome, SubjectRole, RegistrationAddressId)
        VALUES (?, ?, ?, ?)''', [
            ('1', 50000.0, 'Role1', '1'),
            ('2', 60000.0, 'Role2', '2'),
            ('3', 70000.0, 'Role3', '3'),
            ('4', 80000.0, 'Role4', '4'),
            ('5', 90000.0, 'заемщик', '5')
            ]
        )
    connection.commit()
    

def fill_table_registration_address(connection: sqlite3.Connection):
    cursor = connection.cursor()
    cursor.executemany('''
        INSERT INTO RegistrationAddress (Id, Region, City, House)
        VALUES (?, ?, ?, ?)''', [
            ('1', 'Region1', 'City1', 'House1'),
            ('2', 'Region2', 'City2', 'House2'),
            ('3', 'Region3', 'City3', 'House3'),
            ('4', 'Region4', 'City4', 'House4'),
            ('5', 'Новосибирская обл.', 'City5', 'House5')
            ]
        )
    connection.commit()


def fill_table_subject_list(connection: sqlite3.Connection):
    cursor = connection.cursor()
    cursor.executemany('''
        INSERT INTO SubjectList (Id, host_mtype, value_mtype)
        VALUES (?, ?, ?)''', [
            ('1', '1', '1'),
            ('2', '2', '2'),
            ('3', '3', '3'),
            ('4', '4', '4'),
            ('5', '5', '5')
            ]
        )
    connection.commit()


def get_answer(connection: sqlite3.Connection):
    cursor = connection.cursor()
    cursor.execute('''
        SELECT ai.Id
        FROM ApplicationInformation ai
        JOIN Subject s ON ai.SubjectList = s.Id
        JOIN RegistrationAddress ra ON s.RegistrationAddressId = ra.Id
        WHERE ra.Region = 'Новосибирская обл.' 
            AND s.SubjectRole = 'заемщик' 
            AND s.SubjectIncome > 60000
    ''')
    connection.commit()
    return cursor.fetchall()
