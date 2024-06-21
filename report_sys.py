from db_mod import *
from admin_func import *
from input_func import *
from report_func import *


print ("""
First Selection :
1. Super User
2. User
""")
 
while True:
	S1 = input ("who are you :")
	try:
	    S1 = int(S1)
	    if S1 not in [1,2]:
	        print ("unvalid uption,please input 1 / 2")
	    else:
	        break
	except:
	    print ("unvalid option, its not a number")
#	else:
#	    break

while True:
	if S1 == 1:
	    print ("""
yo welcome Super User
What u wanna Do :
1. Print All Student data
2. Search report by id (include exam result)
3. Input new student data
4. Edit data 
5. Edit nilai
6. Remove some data by id (include exam result)
e. Exit

	""")
	    ops = input ("choose : \n")
	    try:
	        ops = int(ops)
	    except:
	        print ("Sayonaraa")
	    finally:
	        if ops == 1:
	            report_ds()
	            
	        elif ops == 2:
	            i_nik = input ("input nik : ")
	            ds_idcheck(i_nik)
	            print ("")
	            ds_nilcheck(i_nik)
	            print ("")
	            
	        elif ops == 3:
	            print ("Inputing new data")
	            i_nik = input("masukan nik   : ")
	            input_ds(i_nik)

	        elif ops == 4:
	            print ("editing student data")
	            print ("please input id of the present data")
	            i_nik = input("id :")
	            ds_edit(i_nik)

	        elif ops == 5:
	            print ("editing student exam result\n")
	            print ("please input id of present nilai")
	            inputnil_ds()

	        elif ops == 6:
	            print ("becarefull you about to delete student data\n")
	            i_nik = input ("input nik : ")
	            
	            ds_idcheck(i_nik)
	            
	            while True:
	                print ("Y/n :\n")
	                opsi = input ("")
	                if opsi in ["Y","y"]:
	                    ds_rmnil(i_nik)
	                    ds_rmdt(i_nik)
	                    break
	                else:
	                    break
				
	        elif ops == "e":
	            break

	else:
	    print ("""
yo welcome User meh
What u wanna Do :
1. Print All Student data
2. Search report by id (include exam result)
3. Input new student data
e. Exit

	""")
	    ops = input ("choose : \n")
	    try:
	        ops = int(ops)
	        if ops is ["e"]:
	            break
	    except:
	        print ("Sayonara")
	    finally:
	        if ops == 1:
	            report_ds()
	            
	        elif ops == 2:
	            i_nik = input ("input nik : ")
	            ds_idcheck(i_nik)
	            print ("")
	            ds_nilcheck(i_nik)
	            print ("")
	            
	        elif ops == 3:
	            print ("Inputing new data")
	            i_nik = input("masukan nik   : ")
	            input_ds(i_nik)

	        elif ops == "e":
	            break
				

cur_ds.close()
db_ds.close()