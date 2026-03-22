# Generar las instancias para cada mob, y mostrar su sonido, comportamiento y forma de moverse.

from vaca import Vaca

vaca = Vaca("Vaca", 15)
vaca.presentarse()

from creeper import Creeper

creeper = Creeper("Creeper", 25)
creeper.presentarse()

from enderman import Enderman

enderman = Enderman("Enderman", 40)
enderman.presentarse()

from zombie import Zombie

zombie = Zombie("Zombie",35)
zombie.presentarse()