from db_mod import *

# function to select one of data by id
def ds_idcheck(i_nik):	
   try:
       ds_select = """
       SELECT * from data where nik = ?
       """
       cur_ds.execute(ds_select, (i_nik,))
       result = cur_ds.fetchone()
       print ("id     : ", result[0])
       print ("nama   : ", result[1])
       print ("gender : ", result[2])
       print ("kelas  : ", result[3])
   except sqlite3.Error as error:
       print ("SQL error", error)

	   
# function to select one nilai by id
def ds_nilcheck(i_nik):
   try:
       ds_select = """
       SELECT * from nilai where nik1 = ?
       """
       cur_ds.execute(ds_select, (i_nik,))
       result = cur_ds.fetchone()
#       print ("id           : ", result[0])
       print ("Matematika   : ", result[1])
       print ("ipa          : ", result[2])
       print ("B.indo       : ", result[3])
       print ("B,inggris.   : ", result[4])
   except sqlite3.Error as error:
       print ("SQL error", error)
	   
	   

# function to edit data 
def ds_edit(i_nik):
    nama = input ("masukan nama   : ")
    gen = input ("masukan gender  : ")
    klas  = input ("masukan kelas  : ")

    ds_edit = """
    UPDATE data SET name=?, gender=?, kelas=? WHERE nik =?
    """
    cur_ds.execute(ds_edit,(nama,gen,klas,i_nik))
    db_ds.commit()
	
		
    print ("")
    print ("edited successfully")

# function to remove the data
def ds_rmdt(i_nik):
   try:
       ds_remove = """
       DELETE FROM data where nik = ?
       """
       cur_ds.execute(ds_remove, (i_nik))
       db_ds.commit()
   except sqlite3.Error as error:
       print ("SQL error", error)
   finally:
       print ("this :", i_nik, "student data successfully deleted")
	   
	   
	   
def ds_rmnil(i_nik):
   try:
       ds_remove = """
       DELETE FROM nilai where nik = ?
       """
       cur_ds.execute(ds_remove, (i_nik))
       db_ds.commit()
   except sqlite3.Error as error:
       print ("SQL error", error)
   finally:
       print ("this :", i_nik, "exam result successfully deleted")
	   
# input the i_nik value 
def search():
   i_nik = input ("Input id : ")
   print ("")
   try :
       if i_nik == str():
           print ("id salah", error)
       elif i_nik == None:
           print ("data kosong", error)
   finally:
       ds_idcheck(i_nik)
       ds_nilcheck(i_nik)

# operation process
def admin_ops():
   while True:
      print ("""
Choose operation :
1. edit
2. remove
3. cancel
""")

      ops = input(": ")
      try:
	      ops = str(ops)
      finally:
          if ops == "1":
              ds_edit(i_nik)
          elif ops == "2":
              ds_rmdt(i_nik)
          elif ops == "3":
              print ("sayonara")
          break
		   		   