from db_mod import *

def report_ds():
    
    cur_ds.execute('SELECT * FROM data;')
	
    print ('\nData:')
    for row in cur_ds.fetchall():
        display_nik    = row[0]
        display_name   = row[1]
        display_gender = row[2]
        display_kelas  = row[3]
		
        print(f'id     : {display_nik}\nnama   : {display_name}\ngender : {display_gender}\nkelas  : {display_kelas}\n')
		

def reportnil_ds():
		
    cur_ds.execute('SELECT * FROM nilai;')
	
    print ('\nNilai: ')
    for row in cur_ds.fetchall():
        display_nik   = row[0]
        display_mtk   = row[1]
        display_ipa   = row[2]
        display_indo  = row[3]
        display_ing   = row[4]
		
        print(f'id           : {display_nik}\nmatematika   : {display_mtk}\nipa          : {display_ipa}\nindo         : {display_indo}\nb.ing        : {display_ing}\n')
		

#report_ds()

#reportnil_ds()