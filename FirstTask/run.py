import sqlite3
import db
from test_db import test

if __name__ == '__main__':
    connection = sqlite3.connect('db.sqlite3')

    # CREATE
    db.create_table_application_information(connection=connection)
    db.create_table_subject(connection=connection)
    db.create_table_registration_address(connection=connection)
    db.create_table_subject_list(connection=connection)
    
    # FILL (already filled)
    # db.fill_table_application_information(connection=connection)
    # db.fill_table_subject(connection=connection)
    # db.fill_table_registration_address(connection=connection)
    # db.fill_table_subject_list(connection=connection)
    
    # TEST
    test(db_name='db.sqlite3')


    # ANSWER
    answer = db.get_answer(connection=connection)
    print('\nAnswer: ')
    for i in answer:
        print('Id:', *answer[0])

    connection.close()
