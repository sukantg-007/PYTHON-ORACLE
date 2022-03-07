import cx_Oracle
from matplotlib import scale
from matplotlib.cm import ScalarMappable

try:
    con = cx_Oracle.connect('system/Sukantg#007@localhost/orcl')    
    cursor = con.cursor()
    print("Enter Student Information")
    id=int(input("Id    : "))
    name=input("Name  : ")
    addr=input("Addr  : ")
    sclass=input("Clas  : ")
    query="INSERT INTO STUDENTTB VALUES(%d,'%s','%s','%s')"%(id,name,addr,sclass)       
    cursor.execute(query)
    con.commit()
    print("Successfully inserted ....")
except cx_Oracle.Error as msg:
    print(msg)
finally:
    cursor.close()
    con.close()