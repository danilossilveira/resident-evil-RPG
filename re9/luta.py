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

    def escolher_personagem(self):
        try:
            escolha = int(input('''Escolha seu personagem
    1- Leon
    2-Chris
    3-Ethan \n'''))
            if escolha == 1:
                personagem_escolhido.nome = self.leon_kennedy.nome
                personagem_escolhido.equipamento = self.leon_kennedy.equipamento
                personagem_escolhido.dano = self.leon_kennedy.dano
                personagem_escolhido.vida = self.leon_kennedy.vida
                personagem_escolhido.especial = self.leon_kennedy.especial
                print(personagem_escolhido)
            elif escolha ==2:
                personagem_escolhido.nome = self.chris_redfield.nome
                personagem_escolhido.equipamento = self.chris_redfield.equipamento
                personagem_escolhido.dano = self.chris_redfield.dano
                personagem_escolhido.vida = self.chris_redfield.vida
                personagem_escolhido.especial = self.chris_redfield.especial
                print(personagem_escolhido)
            elif escolha ==3:
                personagem_escolhido.nome = self.ethan.nome
                personagem_escolhido.equipamento = self.ethan.equipamento
                personagem_escolhido.dano = self.ethan.dano
                personagem_escolhido.vida = self.ethan.vida
                personagem_escolhido.especial = self.ethan.especial
                print(personagem_escolhido)

            else:
                print('Opção inválida')
                Luta.voltar_menu()
        except: print('Você não pode digitas letras e sinais, apenas numeros\n'), Luta.voltar_menu()
        
    
    ataque_nemesis = 25
    def luta(self):
        print(f'Seu primeiro inimigo será o {self.nemesis.nome}')
        contador = 0

        while True:
            critico = 0
            chance = 15
            probabildade = random.randint(1,10)
            if personagem_escolhido.nome == self.ethan.nome:
                if contador == probabildade:
                    personagem_escolhido.vida = (personagem_escolhido.vida + int(5))
                    print(f'{Cores.AZUL}Você regenerou 5 de vida\n{Cores.RESET}')
            elif personagem_escolhido.nome == self.leon_kennedy.nome:
                if contador == probabildade:
                    personagem_escolhido.vida = (personagem_escolhido.vida +25)
                    print(f'{Cores.AZUL}Leon deu um  mortal e desviou do ataque\n{Cores.RESET}')
                    
            elif personagem_escolhido.nome == self.chris_redfield.nome:
                chance = 12

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
                            
                print(f'Você atacou o {self.nemesis.nome}, e ele ficou com {self.nemesis.vida} de vida\n') if self.nemesis.vida > 50 else print(f'O inimigo ficou com apenas {self.nemesis.vida} de vida, você está quase\n')               
                time.sleep(0.5)
                if self.nemesis.vida <= 0:
                    print(f'{Cores.VERDE}Você Ganhou! 👌{Cores.RESET}\n')
                    break  
            personagem_escolhido.vida = (personagem_escolhido.vida - self.nemesis.dano)
            if personagem_escolhido.vida == 0:
                personagem_escolhido.vida += (personagem_escolhido.vida + personagem_escolhido.vida)
            if personagem_escolhido.vida <= 0:
                print(f'{Cores.VERMELHO}Você Perdeu! 🤣{Cores.RESET}\n')
                break                
            print(f'{self.nemesis.nome} te atacou! você ficou com {personagem_escolhido.vida} de vida\n')
            time.sleep(0.5) 

            
    nemesis = Inimigo('Nemesis','Lança míssil', 25, 150 )
    mr_x = Inimigo('Mister X','Soco', 10, 10 )
    
    leon_kennedy = Herois('Leon', 'Pistola',15,140, 'Desvia de ataques')
    chris_redfield = Herois('Chirs', 'Sub-metralhadora',17 ,135, 'Chance de crítico aumenta')
    ethan = Herois('Ethan', 'Shotgun',12, 170,'Regenera vida')
personagem_escolhido = Luta('a','a',0,0,'a')
from luta import Luta
def main():
    Luta.escolher_personagem(Luta)
    Luta.luta(Luta)
if __name__ == '__main__':
    main()  