import pymysql
import time

delay = 0.01

def get_db():
    time.sleep(delay)
    conn = pymysql.connect(host='175.113.135.86',
                            user='fallingup',
                            password='dlfdmscnlal!#%',
                            db='FAUP_TEST',
                            port=3306,
                            charset='utf8mb4',
                            connect_timeout=1)
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    return conn, cursor

def select(query):
    try:
        print(query)
        conn, cursor = get_db()
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    finally:
        conn.close()