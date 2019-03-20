import mysql.connector

connect = mysql.connector.connect(host="ensembldb.ensembl.org",
                                  user="anonymous",
                                  db="homo_sapiens_core_95_38")

woord = input("Waar wil je op zoeken? ")
cursor = connect.cursor()
cursor.execute("select * from gene "
               "where description "
               "like '%{}%' limit 10".format(woord))
rows = cursor.fetchall()
for regel in rows:
    print(regel)
cursor.close()
connect.close()
