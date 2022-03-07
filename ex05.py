import cx_Oracle
try:
    conn = cx_Oracle.connect('system/Sukantg#007@localhost/orcl')
    cursor = conn.cursor()
    ID =    int(input('Enter the id of student you whish to delete  : '))
    query1 = 'SELECT SID FROM STUDENTTB WHERE SID = {}'.format(ID)
    cursor.execute(query1)
    t = cursor.fetchone()
    if t:
        query2 = 'DELETE FROM STUDENTTB WHERE SID = {}'.format(ID)
        cursor.execute(query2)
        conn.commit()
        print("Record delted Successfully :[ID:",ID,"]")
    else:
        print('Sorry!Record does not exist....')
except cx_Oracle.Error as msg:
    print(msg)
finally:
    cursor.close()
    conn.close()
    