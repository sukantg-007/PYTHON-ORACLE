import cx_Oracle
try:
    conn = cx_Oracle.connect('system/Sukantg#007@localhost/orcl')
    cursor = conn.cursor()
    query1 = 'SELECT * FROM STUDENTTB'
    cursor.execute(query1)
    t = cursor.fetchall()
    print('SID\t\tSNAME\t\tSADDR\t\tSCLASS')
    for row in t:
        print(row[0],' \t\t',row[1],'\t\t',row[2],'\t\t',row[3])
except cx_Oracle.Error as msg:
    print(msg)
finally:
    cursor.close()
    conn.close()
    