from ventanas import *
import sqlite3
con= sqlite3.connect('baseProyecto.db')
cursor = con.cursor()
import random



#creacion tablas 
def crea_tab():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS admin(
        nombreUsuario VARCHAR(20),
        contraseña VARCHAR(20),
        rol NUMBER(2)
    );         
    ''')

def crea_tabalm():    
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS alumno(
            numCuenta NUMBER(3),
            nombre VARCHAR(20),
            apellidos VARCHAR(40),
            correoTutor VARCHAR(30),
            edad NUMBER(2)
        
        );
        ''')    
#fin creacion tablas

def insert_tabla(u,c,r):
    ins = ('''INSERT INTO admin VALUES (?, ?, ?)''')
    datos = (u,c,r)
    cursor.execute(ins,datos)
    con.commit()


def insert_tabla_alu(num_cuenta, nombre, apellido,correo,edad):
    ins = ('''INSERT INTO alumno VALUES(?, ?, ?, ?, ?)''')
    datos = (num_cuenta, nombre, apellido,correo,edad)
    cursor.execute(ins,datos)
    con.commit()

def eliminar(num_cuenta):
    ins=(''' DELETE FROM alumno WHERE numCuenta= ?''')
    datos=str(num_cuenta)
    cursor.execute(ins, datos)
    con.commit()

def actualizar(c1, c2,c3,c4,c5):
    ins = ('''UPDATE alumno SET nombre = ?,
     apellidos=?,
     correoTutor=?,
     edad=?
    WHERE numCuenta=?;''')
    datos = (c1, c2,c3,c4,c5)
    cursor.execute(ins,datos)
    con.commit()

def aleaotario():
    n=1
    aleatorios = [random.randint(0,1000) for i in range(n)]
    return aleatorios[0]


def consultas():
    cadena = "SELECT * FROM alumno"
    for row in cursor.execute(cadena):
        print(row)

#consultas()