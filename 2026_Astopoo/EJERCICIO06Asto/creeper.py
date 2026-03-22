from mob import Mob

class Creeper(Mob):
    """Mob Agresivo, suena '.Sssss', Camina rapido hacia el jugador y explota"""
    # TODO: implementa hacer_sonido, comportamiento, moverse

    def hacer_sonido(self) -> str:
        return ".Sssss"

    def comportamiento(self) -> str:
        return "Agresivo"

    def moverse(self) -> str:
        return "Camina rapido hacia el jugador y explota"