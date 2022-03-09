import cx_Oracle
try:
    conn = cx_Oracle.connect('system/Sukantg#007@localhost/orcl')
    cursor = conn.cursor()
    query = 'UPDATE STUDENTTB SET FEES ={}'.format(5000)
    cursor.execute(query)
    conn.commit()
    print('Succesfully Updated')
except cx_Oracle.Error as msg:
    print(msg)
finally:
    cursor.close()
    conn.close()
