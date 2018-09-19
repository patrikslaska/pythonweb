from flask import Flask
import mysql.connector
import os

db_hostname = ''
db_user = 'webapp'
db_password = ''
db_database = 'webapp'
db_connection = ''

app = Flask(__name__)


@app.route("/")
def hello():
    return get_content()


def get_content():
    try:
        cur = db_connection.cursor()
        cur.execute("SELECT * FROM pages WHERE id = 1")
        (id_int, string) = cur.fetchone()
        return string
    except:
        return "LOL!"

def init_pw():
    global db_password
    db_password = os.environ['DB_PASSWORD']


def init_hostname():
    global db_hostname
    db_hostname = os.environ['DB_HOSTNAME']


def init_db():
    init_tables = 'CREATE TABLE IF NOT EXISTS pages (id int(3) NOT NULL, description varchar(45), PRIMARY KEY(id))'
    add_page1 = 'INSERT INTO pages(id,description) VALUES (1,"Hello World from the DB!") ON DUPLICATE KEY UPDATE'
    global db_connection

    try:
        db_connection = mysql.connector.connect(user=db_user, password=db_password,
                                            host=db_hostname, database=db_database)
        cur = db_connection.cursor()
        cur.execute(init_tables)
#        cur.execute(add_page1)

        db_connection.commit()

    except mysql.connector.Error as err:
        if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        exit()


if __name__ == "__main__":
    init_hostname()
    init_pw()
    init_db()
    app.run(host='0.0.0.0',port=80)
