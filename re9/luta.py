import random
import time
import os
from inimigo import Inimigo
from herois import Herois
from cores import Cores
class Luta():
    def __init__(self, nome, equipamento,dano,vida,especial):
        self.nome = nome
        self.equipamento = equipamento
        self.dano = dano
        self.vida = vida
        self.especial = especial
    def __str__(self):
        return (f'Nome: {self.nome} \nEquipamento: {self.equipamento} \nDano: {self.dano} \nVida: {self.vida} \nEspecial: {self.especial}')

    def voltar_menu():        
        input('ENTER para voltar ao menu')
        os.system('cls')
        Luta.escolher_personagem(Luta)

    #Aqui é a escolha o personagem
    def escolher_personagem(self):
        personagens = {
            1: self.leon_kennedy,
            2: self.chris_redfield,
            3: self.ethan,
            4: self.ada_wong,
            5: self.jill_valentine,
            6: self.hunk
                }
        escolha = int(input('''Escolha seu personagem
    1- Leon
    2-Chris
    3-Ethan
    4-Ada
    5-Jill
    6-Hunk
    \n'''))
        if escolha not in personagens:
            print('Essa escolha não exise')
            Luta.escolher_personagem(Luta)

        personagem_escolhido.__dict__.update(personagens[escolha].__dict__)
        print(personagem_escolhido)    




    #Aqui é o combate
    def luta(self):
        print(f'Seu primeiro inimigo será o {self.nemesis.nome}')
        contador = 0

        while True:
            critico = 0
            chance = 15
            #Aqui é os especiais
            probabildade = random.randint(1,10)
            #Ethan
            if personagem_escolhido.nome == self.ethan.nome:
                if contador == probabildade:
                    personagem_escolhido.vida = (personagem_escolhido.vida + int(15))
                    print(f'{Cores.AZUL}Você regenerou 15 de vida\n{Cores.RESET}')
            #Leon        
            elif personagem_escolhido.nome == self.leon_kennedy.nome:
                if contador == probabildade:
                    personagem_escolhido.vida = (personagem_escolhido.vida +25)
                    print(f'{Cores.AZUL}Leon deu um  mortal e desviou do ataque\n{Cores.RESET}')
            #Chris        
            elif personagem_escolhido.nome == self.chris_redfield.nome:
                chance = 12
            #Ada    
            elif personagem_escolhido.nome == self.ada_wong.nome:
                if contador == probabildade:
                    personagem_escolhido.dano = (personagem_escolhido.dano + personagem_escolhido.dano)
                    print(f'{Cores.AZUL}Dano multiplicado\n{Cores.RESET}')
                else:    
                    personagem_escolhido.dano = self.ada_wong.dano
            #Hunk        
            elif personagem_escolhido.nome == self.hunk.nome:
                hitkill = random.randint(1,20)
                probabildade = random.randint(1,20)
                if hitkill == probabildade:
                    print(f'{Cores.AZUL}PESCOÇO DO INIMIGO QUEBRADO\n{Cores.RESET}')
                    self.nemesis.vida = 0
            #Jill
            elif personagem_escolhido.nome == self.jill_valentine.nome:
                if personagem_escolhido.vida <= 130 and personagem_escolhido.vida > 100:
                    personagem_escolhido.dano = 15
                elif personagem_escolhido.vida <= 100 and personagem_escolhido.vida > 70:
                    personagem_escolhido.dano = 16
                elif personagem_escolhido.vida <= 70 and personagem_escolhido.vida > 30:
                    personagem_escolhido.dano = 17
                elif personagem_escolhido.vida <= 30 and personagem_escolhido.vida > 15:
                    personagem_escolhido.dano = 19
                else:
                    personagem_escolhido.dano = 20         

            #Aqui é o sistema de crítico
            contador = (contador + 1)
            critico = random.randint(1,20)
            input('ENTER para atacar\n')
            os.system('cls')
            if critico > chance:
                dano_critico = 0
                dano_critico = (personagem_escolhido.dano + personagem_escolhido.dano * 1.5)
                self.nemesis.vida = (self.nemesis.vida - dano_critico)

                print(f'{Cores.VERMELHO}CRITICO🔥! Você deu {dano_critico} de dano no {self.nemesis.nome}, e ele ficou com {self.nemesis.vida} de vida{Cores.RESET}\n')
                time.sleep(0.5)
                if self.nemesis.vida <= 0:
                    print(f'{Cores.VERDE}Você Ganhou! 👌{Cores.RESET}\n')
                    break
            else:
                self.nemesis.vida = (self.nemesis.vida - personagem_escolhido.dano)
            #Aqui é o sistema de golpe normal                
                print(f'Você atacou o {self.nemesis.nome}, e ele ficou com {self.nemesis.vida} de vida\n') if self.nemesis.vida > 50 else print(f'O inimigo ficou com apenas {self.nemesis.vida} de vida, você está quase\n')               
                time.sleep(0.5)
                if self.nemesis.vida <= 0:
                    print(f'{Cores.VERDE}Você Ganhou! 👌{Cores.RESET}\n')
                    break  
            personagem_escolhido.vida = (personagem_escolhido.vida - self.nemesis.dano)
            if personagem_escolhido.vida == 0:
                personagem_escolhido.vida += (personagem_escolhido.vida + personagem_escolhido.vida)
            #Aqui é o ataque do inimigo    
            if personagem_escolhido.vida <= 0:
                print(f'{Cores.VERMELHO}Você Perdeu! 😢{Cores.RESET}\n')
                break                
            print(f'{self.nemesis.nome} te atacou! você ficou com {personagem_escolhido.vida} de vida\n')
            time.sleep(0.5) 

    #Aqui são os inimigos        
    nemesis = Inimigo('Nemesis','Lança míssil', 25, 150 )
    mr_x = Inimigo('Mister X','Soco', 10, 10 )
    #Aqui são os heróis
    leon_kennedy = Herois('Leon', 'Pistola',15,150, 'Desvia de ataques')
    chris_redfield = Herois('Chirs', 'Sub-metralhadora',17 ,135, 'Chance de crítico aumenta')
    ethan = Herois('Ethan', 'Shotgun',12, 170,'Regenera vida')
    ada_wong = Herois('Ada Wong', 'Balestra' ,14 , 145,'Dano multiplicado')
    hunk = Herois('Hunk', 'Metralhadora', 16, 150, 'Chance de dar um hit kill')    
    jill_valentine = Herois('Jill Valentine', 'Assalto', 14, 150, 'Quanto menos vida, mais dano')

    claire_redfield = Herois('Claire Redfield', 'Revolver', 15, 155, '')
    rebecca_chambers = Herois('Rebecca Chambers', 'Rifle', 13, 125, '')    
    wesker = Herois('Wesker', 'Katana', 19, 180, '')
#Veneno/Sangramento contínuo
#Aumenta força a cada ataque(quanto menos vida)


personagem_escolhido = Luta('a','a',0,0,'a')
#Aqui é a função main
def main():
    Luta.escolher_personagem(Luta)
    Luta.luta(Luta)
if __name__ == '__main__':
    main()  