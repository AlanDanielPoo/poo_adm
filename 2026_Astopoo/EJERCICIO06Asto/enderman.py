from mob import Mob

class Enderman(Mob):
    """Mob neutral, suena borroso, se teletransporta o desaparece."""

    def hacer_sonido(self):
        return "Grrrr."
    
    def comportamiento(self):
        return "Neutral"
    def moverse(self):
        return "Se teletransporta o desaparece"