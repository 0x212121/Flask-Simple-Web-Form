from MySQLdb.cursors import Cursor
import mysql.connector

db_connection = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="assessment"
)

def create_table():
    db_cursor = db_connection.cursor()
    # db_cursor.execute("SHOW DATABASES")
    db_cursor.execute(''' CREATE TABLE results
    (
        id int primary key not null AUTO_INCREMENT, 
        fullname varchar(64) not null, 
        badge varchar(10) not null, 
        hostname varchar(15) not null, 
        sharing_file varchar(15),
        onlineform varchar (15),
        registered varchar (5),
        use_powerbi varchar (5),
        use_macro varchar (5), 
        kpc_mail varchar (5), 
        vpn_user varchar (5), 
        paham_o365 varchar(10),
        mail varchar(20),
        cloud_serv varchar(24),
        result varchar(24) not null,
        `date` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    ) 
    ''')


def drop_table():
    try:
        db_cursor = db_connection.cursor()
        db_cursor.execute("DROP TABLE results")
        print("Berhasil menghapus tabel")
    except:
        print("Gagal menghapus table")

drop_table()
create_table()