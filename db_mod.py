import sqlite3

print ("")

db_ds = sqlite3.connect("data_siswa.db")
print ('db_ds is connected')

cur_ds = db_ds.cursor()

ds_table = """
CREATE TABLE IF NOT EXISTS data (
    nik INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
	gender TEXT NOT NULL,
    kelas TEXT NOT NULL
);
"""
nil_table = """
CREATE TABLE IF NOT EXISTS nilai (
	nik1 INTEGER PRIMARY KEY ,
    matematika TEXT NOT NULL,
	ipa TEXT NOT NULL,
	indo TEXT NOT NULL,
	ing TEXT NOT NULL,
	FOREIGN KEY (nik1) REFERENCES data(nik) 
);
"""

trigger = """
	CREATE TRIGGER IF NOT EXISTS after_data_insert
	AFTER INSERT ON data
	FOR EACH ROW
	BEGIN
	    INSERT INTO nilai (nik1, matematika, ipa, indo, ing) VALUES (NEW.nik, '', '', '', '');
	END;
"""

cur_ds.execute(ds_table)
cur_ds.execute(nil_table)

cur_ds.executescript(trigger)

#cur_ds.execute('SELECT * FROM data;')
#cur_nil.execute('SELECT * FROM nilai;')

#result_ds = cur_ds.fetchall()
#print (result_ds,"\n")

#result_nil = cur_nil.fetchall()
#print (result_nil)

#cur_ds.execute('SELECT * FROM data;')

"""
def ds_all():

    result = cur_ds.fetchall()
    print (result)
    print (type(result))
"""
		

#cur_nil.close()
#cur_ds.close()

#db_nil.close()
#db_ds.close()