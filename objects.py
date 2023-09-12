
# Idea abstracta de un objeto
class Vehicle():

    all_vehicles = []

    def __init__(self, matricula, color, model, vtype, **kwargs):
        self.matricula = matricula
        self.color = color
        self.model = model
        self.vtype = vtype

        __class__.all_vehicles.append(self)

    # classmethod - method - staticmethod

    @classmethod
    def get_all_vehicles(cls):
        return [ item for item in cls.all_vehicles ]


    @staticmethod
    def accelerate() -> str:
        return "Rrrrmmmr rmmmr rhrhhr"
    
    #@staticmethod Error
    def stop(self):
        print(f" The vehicle with plate {self.matricula} has stopped !")

    def __repr__(self) -> str:
        return f" Vehicle Object { self.matricula }"
    
print( Vehicle.get_all_vehicles() )

class Spaceship():

    def __init__(self, turbine, engine, **kwargs):
        self.engine = engine
        self.turbine = turbine
        super(Spaceship, self).__init__(**kwargs)

    def fly(self):
        return f" To infinty and beyond! "

enterprise = Spaceship(engine='Motor de Bera', turbine='Turbine 12')

print( enterprise.engine )

class Car (Spaceship, Vehicle): # Base Declarativa - ORM

    def __init__(self, country, wheels, engine, turbine, **kargs):
        
        # Car specs
        self.country = country
        self.wheels = wheels

        super(Car, self).__init__(engine=engine, turbine=turbine, **kargs)
        
    def stop(self):
        print( f"The Car has %s stop! %s" % ( self.engine, self.color) )

    def __repr__(self) -> str:
        return f" Car Object { self.matricula } { self.country }"
    
class Bote(Vehicle):

    def __init__(self, matricula, color, model, vtype, c_velas, propela, **kwargs):
        self.c_velas = c_velas
        self.propela = propela
        super().__init__(matricula, color, model, vtype, **kwargs)

carro_de_diego = Car( color="Azul",
                      matricula="4SF591",
                        model="BMW",
                          vtype="Sedan",
                            wheels=4,
                              country="Germany",
                                engine="V8",
                                  turbine="Classic Turbine")

print( carro_de_diego.accelerate() )

print( carro_de_diego.fly() )

print(carro_de_diego)

carro_de_diego.stop()


bote_de_stefano = Bote(matricula="FG54SA",
                        color="Esmeralda",
                          model="Titanic",
                            vtype="Velero",
                              c_velas=2,
                                propela=6)

print( bote_de_stefano )

lista_vehiculos = Vehicle.get_all_vehicles() 

lista_vehiculos[0].color = "Naranja"

print( lista_vehiculos[0].color , carro_de_diego.color )