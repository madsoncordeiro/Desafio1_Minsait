from monstro import Monstro

class Globin(Monstro):
    def __init__(self, tipo, inteligencia, pontos_vida, pontos_ataque):
        super().__init__(tipo, pontos_vida, pontos_ataque)
        self.inteligencia = inteligencia