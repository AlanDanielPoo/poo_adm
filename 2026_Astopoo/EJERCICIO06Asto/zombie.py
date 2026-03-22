from mob import Mob

class Zombie(Mob):
    """Mob No amigable, suena 'Grrr… uuuuhh… raaaahh…', Te ataca ."""

    def hacer_sonido(self):
        return "Grrr… uuuuhh… raaaahh…"
    
    def comportamiento(self):
        return "No amigable"
    def moverse(self):
        return "Se mueve medio lento hacia el jugador para atacar"