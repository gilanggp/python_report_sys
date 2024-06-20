from db_mod import *

	
def input_ds():
	
    nama = input ("masukan nama   : ")
    gen = input ("masukan gender  : ")
    klas  = input ("masukan kelas  : ")
	
    insert_query_ds = """
    INSERT INTO data (name,gender,kelas)
    VALUES (?, ?, ?);
    """
    cur_ds.execute(insert_query_ds, (nama,gen,klas))
    db_ds.commit()

    cur_ds.close()

    db_ds.close()
	
input_ds()
