from monstro import Monstro

class Lobo(Monstro):
    def __init__(self, tipo, forca, pontos_vida, pontos_ataque):
        super().__init__(tipo, pontos_vida, pontos_ataque)
        self.forca = forca