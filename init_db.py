import os
import psycopg2


db_host = os.environ.get('database_host')
db_name =  os.environ.get('database_name')
db_username =  os.environ.get('database_user')
db_password =  os.environ.get('database_password')

connection = psycopg2.connect(
        host=db_host,
        database=db_name,
        user=db_username,
        password=db_password,
        port=5432)

# Open a cursor to perform database operations
cursor = connection.cursor()

# Execute a command: this creates a new table
cursor.execute('DROP TABLE IF EXISTS books;')
cursor.execute('CREATE TABLE books (id serial PRIMARY KEY,'
                                 'title varchar (150) NOT NULL,'
                                 'author varchar (50) NOT NULL,'
                                 'pages_num integer NOT NULL,'
                                 'review text,'
                                 'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                 )

# Insert data into the table

cursor.execute('INSERT INTO books (title, author, pages_num, review)'
            'VALUES (%s, %s, %s, %s)',
            ('A Tale of Two Cities',
             'Charles Dickens',
             489,
             'A great classic!')
            )


cursor.execute('INSERT INTO books (title, author, pages_num, review)'
            'VALUES (%s, %s, %s, %s)',
            ('Anna Karenina',
             'Leo Tolstoy',
             864,
             'Another great classic!')
            )

connection.commit()

cursor.close()
connection.close()