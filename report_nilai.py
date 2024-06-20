from db_mod import *

def reportnil_ds():
    
    cur_ds.execute('SELECT * FROM nilai;')
	
    print ('\nnilai:')
    for row in cur_ds.fetchall():
        display_nik   = row[0]
        display_mtk   = row[1]
        display_ipa   = row[2]
        display_indo  = row[3]
        display_ing  = row[4]
		
        print(f'id     : {display_nik}\nmatematika   : {display_mtk}\nipa : {display_ipa}\nindo  : {display_indo}\nb.ing  : {display_ing}')

reportnil_ds()

cur_ds.close()

db_ds.close()
