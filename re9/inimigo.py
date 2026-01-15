from personagem import Personagem
class Inimigo(Personagem):
    def __init__(self, nome, equipamento, dano,vida):
        super().__init__(nome,equipamento,dano, vida)
