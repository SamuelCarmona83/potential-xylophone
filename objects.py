
# Idea abstracta de un objeto
class Vehicle():

    def __init__(self, matricula, color, model, vtype, **kwargs):
        self.matricula = matricula
        self.color = color
        self.model = model
        self.vtype = vtype

    def accelerate(self) -> str:
        return "Rrrrmmmr rmmmr rhrhhr"

    def stop(self):
        print(f" The vehicle with plate {self.matricula} has stopped !")

    def __repr__(self) -> str:
        return f" Vehicle Object { self.matricula }"
    
class Spaceship():

    def __init__(self, engine, turbine, **kwargs):
        self.engine = engine
        self.turbine = turbine
        super(Spaceship, self).__init__(**kwargs)

    def fly(self):
        return f" To infinty and beyond! "


class Car(Spaceship, Vehicle): # Base Declarativa - ORM

    def __init__(self, country, wheels, engine, turbine, **kargs):
        
        # Car specs
        self.country = country
        self.wheels = wheels

        super(Car, self).__init__(engine=engine, turbine=turbine, **kargs)
        
    def stop(self):
        print( f"The Car has %s  %s stop!" % ( self.engine, self.color) )

    def __repr__(self) -> str:
        return f" Car Object { self.matricula } { self.country }"
    
class Bote():
    pass

carro_de_diego = Car( matricula="4SF591", color="Azul", model="BMW", vtype="Sedan", wheels=4, country="Germany", engine="V8", turbine="Classic Turbine")
print( carro_de_diego.accelerate() )

print( carro_de_diego.fly() )

print(carro_de_diego)
carro_de_diego.stop()