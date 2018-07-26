import csv 
import MySQLdb
import random 
 
conn = MySQLdb.connect (
    host = "localhost", 
    user = "root", 
    passwd =  "root", 
    db = "distribuidos")
cursor = conn.cursor()

with open('tgif-v1.0.tsv') as tsvfile:
    reader = csv.reader(tsvfile, delimiter='\t')
    for row in reader:
        acceso = random.randrange(0, 100)
        print row[0]
        valores = ((acceso),row[0],row[1])
        query = ("""INSERT INTO gifs (num_acceso, link, descripcion) VALUES (%s,%s,%s)""")
        cursor.execute(query, valores)
        conn.commit()

    
