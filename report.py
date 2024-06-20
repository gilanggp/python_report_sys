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

report_ds()


cur_ds.close()

db_ds.close()
