from mob import Mob

class Vaca(Mob):
    """Mob Pasivo, suena 'Muuuu', camina lento por el pasto."""
    # TODO: implementa hacer_sonido, comportamiento, moverse

    def hacer_sonido(self) -> str:
        return "Muuuu"

    def comportamiento(self) -> str:
        return "pasivo"

    def moverse(self) -> str:
        return "Camina lento por el pasto"