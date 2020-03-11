#Create Read Update Delete CRUD
import sqlite3
con = sqlite3.connect('bases.db')
cursor = con.cursor()
def crear_Tabla():
    cursor.execute('''
    CREATE TABLE semestre(
        semestre_clave NUMERIC(18),
        anio NUMERIC(4),
        periodo NUMERIC(2),
        fecha_inicio VARCHAR2(20),
        fecha_fin VARCHAR2(20)
    )
    ''')
    cursor.execute('''
    CREATE TABLE estudiante(
        estudiante_clave NUMERIC(30),
        nombre VARCHAR2(30),
        calificacion NUMERIC(2,2)
    )
    ''')
    cursor.execute("INSERT INTO estudiante VALUES(313326626,'Galileo Garibaldi',8.32)")
    cursor.execute("INSERT INTO estudiante VALUES(365464845,'Dafne Garibaldi',9.72)")
    cursor.execute("INSERT INTO estudiante VALUES(316874651,'Jorge Chavez',8.92)")

def insertar_Tabla():
    tabla_nombre = input("En qué tabla quieres insertar?: ")
    datos = input("Qué datos deseas insertar?: ") 
    cadena = "INSERT INTO" + tabla_nombre + " VALUES ( " + datos + ")"
    cursor.execute(cadena)
    con.commit()

def eliminar_Tabla():
    t = int(input("Qué desea eliminar: \nTabla-> 1\nDato -> 2"))
    if t == 1:
        tabla_nombre = input("De qué tabla quieres borrar?: ")
        cadena = "DELETE FROM " + tabla_nombre
        cursor.execute(cadena)
        con.commit()

    if t ==2:
        try:
            tabla_nombre = input("De qué tabla deseas eliminar?: ")
            clave = int(input("Cuál es la clave del dato que deseas eliminar?: "))
            cadena = "DELETE FROM "+ tabla_nombre + ' WHERE ' + tabla_nombre+'_clave' + ' = ' + clave 
            cadena.execute
        except Exception as e:
            con.commit()
            print("Ocurrió un error")

def ver():
    instruccion = input("De qué tabla deseas obtener valores?: ")
    cadena = "SELECT * FROM " + instruccion
    for row in cursor.execute(cadena):
        print(row)
    con.commit()

while True:
    try:
        crear_Tabla()
        while True:
            op = int(input("Qué desea hacer? \n1.-Insertar datos  \n2.-Eliminar tabla \n3.-Ver tabla \n4.-Salir"))
            if op ==1:
                insertar_Tabla()
            if op == 2:
                eliminar_Tabla()
            if op == 3:
                ver()
            if op == 4:
                break 
    except:
        print("Ocurrió un error")
        con.commit()
        con.close()
        break                       

