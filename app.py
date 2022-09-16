import os
import psycopg2
from flask import Flask, render_template,  request, url_for, redirect

app = Flask(__name__)

db_host = os.environ['database_host']
db_name = os.environ['database_name']
db_username = os.environ['database_user']
db_password = os.environ['database_password']

def get_db_connection():
    connection = psycopg2.connect(
            host=db_host,
            database=db_name,
            user=db_username,
            password=db_password,
            port=5432)
    return connection


@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM books;')
    books = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', books=books)


# ...

@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        pages_num = int(request.form['pages_num'])
        review = request.form['review']

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO books (title, author, pages_num, review)'
                    'VALUES (%s, %s, %s, %s)',
                    (title, author, pages_num, review))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))

    return render_template('create.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')