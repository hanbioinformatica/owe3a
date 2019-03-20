import mysql.connector

woord = input("Waar wil je op zoeken? ")

verbinding = mysql.connector.connect(host="ensembldb.ensembl.org",
                                     user="anonymous",
                                     db="homo_sapiens_core_95_38")

cursor = verbinding.cursor()
cursor.execute("select * from gene where description like '%{}%' limit 10".format(woord))
regel = ""
while regel != None:
    regel = cursor.fetchone()
    print (regel)
cursor.close()
verbinding.close()



