

class Vehicle():

    def __init__(self, matricula, color, model, vtype):
        self.matricula = matricula
        self.color = color
        self.model = model
        self.vtype = vtype

    def accelerate(self) -> str:
        return "Rrrrmmmr rmmmr rhrhhr"

    def stop(self):
        print(f" The  car with plate {self.matricula} has stopped !")

    def __repr__(self) -> str:
        return f" Car Object { self.matricula }"
    

carro_de_diego = Vehicle("4SF591", "Azul", "BMW", "Sedan")


print( carro_de_diego.accelerate() )

print(carro_de_diego)

carro_de_diego.stop()