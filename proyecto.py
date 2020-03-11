import sqlite3
con=sqlite3.connect('baseProyecto.db')
cursor = con.cursor()
cursor.execute('''
CREATE TABLE alumno(
    numCuenta NUMBER(3),
    nombre VARCHAR(20),
    edad NUMBER(2),
    correoTutor VARCHAR(30)

);

''')

cursor.execute('''
CREATE TABLE administrador(
    nombreUsuario VARCHAR(20),
    contraseña VARCHAR(20),
    rol NUMBER(2)
)


''')