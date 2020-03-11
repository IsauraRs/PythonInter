import sqlite3
con = sqlite3.connect('bases.db')
cursor = con.cursor()
cursor.execute(''' 
CREATE TABLE IF NOT EXISTS veterinaria( 
    clave_veterinaria NUMERIC(5) PRIMARY KEY,
    direccion VARCHAR2(40),
    nombre VARCHAR2(40)
)

''')
cursor.execute("INSERT INTO veterinaria VALUES(11,'calle siempre viva','Dr.Hiebert')")
cursor.execute("INSERT INTO veterinaria VALUES(22,'calle siempre muerta','Dr.Hiebert')")
cursor.execute("INSERT INTO veterinaria VALUES(33,'calle siempre agonizante','Dr.Simi')")
con.commit()
for row in  cursor.execute("SELECT * FROM veterinaria"):
    print(row)
con.commit()
con.close()    