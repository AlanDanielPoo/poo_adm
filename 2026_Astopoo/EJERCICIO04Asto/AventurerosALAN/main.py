from guerrero import Guerrero
from mago import Mago
from arquero import Arquero

#Crear objetos
guerrero = Guerrero("Daniel", 25, "Hacha")
mago = Mago("Galan", 18, "Bola de fuego")
arquero = Arquero("Scream", 15, 40)

#usar metodos
guerrero.presentarse()
guerrero.usar_habilidad()
print("Habilidad de combate")

mago.presentarse()
mago.usar_habilidad()
print("Habilidad de hechizo")

arquero.presentarse()
arquero.usar_habilidad()
print("Habilidad a distancia")