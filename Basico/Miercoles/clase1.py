class Perro():
    color = "blanco"
    olor = "Olor a perro :v"
    num_patas = 4
    num_orejas = 2
    tam = "Pequeño"
    def ladrar(self):
        print("Decir Guau :V ")
    def comer(self):
        print("Comiendo :v")
    def caminar(self):
        print("Caminando :v")

prro = Perro()
print(prro.color)
print(prro.olor)
prro.ladrar()
prro.caminar()
prro.comer()
