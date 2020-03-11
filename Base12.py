import sqlite3
con = sqlite3.connect('bases.db') #Crea la base
cursor = con.cursor() #Sirve para hacer o ejecutar código sql
cursor.execute(''' 
    CREATE TABLE animal1(
        clave_animal NUMERIC(10),
        habitat VARCHAR2(30),
        nombre  VARCHAR2(40),
        color VARCHAR2(40),
        genero VARCHAR2(1),
        especie VARCHAR2(30)
        )
''')
cursor.execute("INSERT INTO animal1 VALUES(1,'casa','Cat','Gris','M','gato')")
cursor.execute("INSERT INTO animal1 VALUES(2,'casa','polito','Gris','M','gato')")
cursor.execute("INSERT INTO animal1 VALUES(3,'casa','Espinocito','Café','M','Erizo')")
con.commit() #Guarda los datos de la tabla
print("Imprimiendo los valores de la tabla")
for row in cursor.execute("SELECT * FROM animal1"):
    print(row)

con.commit()
con.close()    