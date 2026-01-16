from personagem import Personagem
class Herois(Personagem):
    def __init__(self, nome, equipamento, dano,vida,especial):
        super().__init__(nome,equipamento,dano,vida)
        self.especial = especial
