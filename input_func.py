from db_mod import *
from admin_func import ds_idcheck

	
def input_ds(i_nik):
	
    nama = input ("masukan nama   : ")
    gen = input ("masukan gender  : ")
    klas  = input ("masukan kelas  : ")
	
    insert_query_ds = """
    INSERT INTO data (nik,name,gender,kelas)
    VALUES (?, ?, ?, ?);
    """
    cur_ds.execute(insert_query_ds, (i_nik,nama,gen,klas))
    db_ds.commit()


	
def inputnil_ds():
    nik = input ("masukan nik : ")
	
    ds_idcheck(nik)
	
    print("")
	
    matematika = input ("Matematika     : ")
    ipa        = input ("Ipa            : ")
    indo       = input ("B.Indonesia    : ")
    ing        = input ("B.Inggris      : ")

    ds_edit = """
    UPDATE nilai SET matematika=?, ipa=?, indo=?, ing=? WHERE nik1 =?
    """
    cur_ds.execute(ds_edit,(matematika,ipa,indo,ing,nik))
    db_ds.commit()
	

	
    print ("")
    print ("edited successfully")
	
#input_ds()
#inputnil_ds()