from pico import Pico
from espada import Espada
from pala import Pala
from arco import Arco

if __name__ == "__main__":
    herramientas = [
        Pico("Oro", 2),
        Espada("Diamante", 2),
        Pala("Hierro",2),
        Arco("Piedra",3, 10),
    ]

    objetivos = ["Mena de diamante", "Zombie", "Arena","Esqueleto"]

    for h,obj in zip(herramientas, objetivos):
        #Bucle hasta que se rompa
        while not  h.rota:
            print(h.usar(obj))
            h.estado()
            print()