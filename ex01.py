import cx_Oracle

try:
    con = cx_Oracle.connect('system/Sukantg#007@localhost/orcl')
    #con=cx_Oracle.connect(user="system",password="Sukantg#007", dsn="localhost/orcl")
    cursor = con.cursor()
    query="INSERT INTO STUDENTTB VALUES(101,'AAA','Daund','MCA')"
    cursor.execute(query)
    con.commit()
    print("Successfully inserted ....")
except cx_Oracle.Error as msg:
    print(msg)
finally:
    cursor.close()
    con.close()