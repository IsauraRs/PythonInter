class Estudiante:
    def __init__(self, Nombre, Carrera):
        self.nombre = Nombre
        self.carrera = Carrera
        print("MEtodo constructor")


    def Estudiar(self):
        print('Voy a estudiar un rato..')


estudiante1 = Estudiante('Ale', 'Conta')
estudiante2 = Estudiante('Vero', 'Medicina')

estudiante1.Estudiar()
estudiante2.verNetflix('Club de Cuervos', 2)