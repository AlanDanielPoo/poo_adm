from comida import Comida
from bebida import Bebida
from postre import Postre

#Mostrar Objetos
comida = Comida("Espaguetti", 100.0, "principal")
bebida = Bebida("Soda", 35.0, "Fria")
postre = Postre("Pastel de chocolate", 45.0, False)

#Mostrar Informacion
comida.mostrar_info()
comida.tipo()
print("---")

bebida.mostrar_info()
bebida.tipo()
print("---")

postre.mostrar_info()
postre.tipo()