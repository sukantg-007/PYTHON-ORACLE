import cx_Oracle
try:    
    conn = cx_Oracle.connect('system/Sukantg#007@localhost/orcl')
    cursor = conn.cursor()
    sid = int(input("Enter the Id of Student Which you wish to Update   : "))
    query = "SELECT SID FROM STUDENTTB WHERE SID = {}".format(sid)
    cursor.execute(query)
    t = cursor.fetchone()
    if t:
        sname = input("Enter the name of student    :")
        saddr = input("Enter the address of student :")
        sclass = input("Enter the class of student  :")
        query = "UPDATE STUDENTTB SET SNAME = :1,SADDR = :2,SCLASS = :3 WHERE SID= {}".format(sid)
        cursor.execute(query,[sname,saddr,sclass])
        conn.commit()
        print("succesfully updated")
    else :
        print("Record not available")
except cx_Oracle.Error as msg:
    print(msg)
finally:
    cursor.close()
    conn.close()

