import cx_Oracle
try:
    conn = cx_Oracle.connect('system/Sukantg#007@localhost/orcl')
    cursor = conn.cursor()
    query = 'select sum(fees) from studenttb'
    cursor.execute(query)
    t = cursor.fetchone()
    print('total fees :',t[0])
    conn.commit()
    print('succesfull')
except cx_Oracle.Error as msg:
    print(msg)
finally:
    cursor.close()
    conn.close()