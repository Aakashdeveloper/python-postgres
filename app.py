import psycopg2

connection = psycopg2.connect('dbname=udacity')
cursor = connection.cursor()
cursor.execute('''
    CREATE TABLE test (
        id INTEGER PRIMARY KEY,
        task BOOLEAN NOT NULL DEFAULT FALSE
    );
''')

cursor.execute('INSERT INTO test (id, task) VALUES (1, true);')

connection.commit()
connection.close()
cursor.close()