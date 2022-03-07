import cx_Oracle
from matplotlib import scale
from matplotlib.cm import ScalarMappable

try:
    con = cx_Oracle.connect('system/Sukantg#007@localhost/orcl')    
    cursor = con.cursor()
    list_record=[]
    while True:
        print("Enter Student Information")
        id=int(input("Id    : "))
        name=input("Name  : ")
        addr=input("Addr  : ")
        sclass=input("Clas  : ")       
        list_record.append([id,name,addr,sclass])
        choice=input("Enter y to continue[n/y] :")
        if choice!='y':
            break

    query="INSERT INTO STUDENTTB VALUES(:1,:2,:3,:4)"
    cursor.executemany(query,list_record)
    con.commit()
    print("Successfully inserted ....")
    
except cx_Oracle.Error as msg:
    print(msg)
finally:
    cursor.close()
    con.close()