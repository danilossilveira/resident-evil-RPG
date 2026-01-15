import random
import time
import os
from inimigo import Inimigo
from herois import Herois
from personagem import Personagem
class Luta(Personagem):
    def __init__(self, nome, equipamento,dano,vida):
        self.nome = nome
        self.equipamento = equipamento
        self.dano = dano
        self.vida = vida

       

    def __str__(self):
        return (f'Nome: {self.nome} \nEquipamento: {self.equipamento} \nDano: {self.dano} \nVida: {self.vida}')            

          
 
    def escolher_personagem(self):
        escolha = int(input('''Escolha seu personagem
1- Leon
2-Chris
3-Ethan \n'''))
        if escolha == 1:
            personagem_escolhido.nome = self.leon_kennedy.nome
            personagem_escolhido.equipamento = self.leon_kennedy.equipamento
            personagem_escolhido.dano = self.leon_kennedy.dano
            personagem_escolhido.vida = self.leon_kennedy.vida
            print(personagem_escolhido)
        elif escolha ==2:
            personagem_escolhido.nome = self.chris_redfield.nome
            personagem_escolhido.equipamento = self.chris_redfield.equipamento
            personagem_escolhido.dano = self.chris_redfield.dano
            personagem_escolhido.vida = self.chris_redfield.vida                
            print(personagem_escolhido)
        elif escolha ==3:
            personagem_escolhido.nome = self.ethan.nome
            personagem_escolhido.equipamento = self.ethan.equipamento
            personagem_escolhido.dano = self.ethan.dano
            personagem_escolhido.vida = self.ethan.vida                
            print(personagem_escolhido) 
            
        else:
            print('Opção inválida')

           


    def luta(self):
        print(f'Seu primeiro inimigo será o {self.nemesis.nome}')
        
        while True:
                       
            critico = 0
            critico = random.randint(1,20)                            
            input('ENTER para atacar')
            os.system('cls')
            if critico > 15:
                dano_critico = 0 
                dano_critico = (personagem_escolhido.dano + personagem_escolhido.dano * 1.5) 
                self.nemesis.vida = (self.nemesis.vida - dano_critico)

               
                print(f'CRITICO🔥! Você deu {dano_critico} de dano no {self.nemesis.nome}, e ele ficou com {self.nemesis.vida} de vida')
                time.sleep(0.5)
                if self.nemesis.vida < 0:
                    print('Você Ganhou! 👌')
                    break
            else:                
                self.nemesis.vida = (self.nemesis.vida - personagem_escolhido.dano)
                            
                print(f'Você atacou o {self.nemesis.nome}, e ele ficou com {self.nemesis.vida} de vida') if self.nemesis.vida > 30 else print(f'O inimigo ficou com apenas {self.nemesis.vida} de, vida, você está quase')               
                time.sleep(0.5)
                if self.nemesis.vida < 0:
                    print('Você Ganhou! 👌')
                    break  
            personagem_escolhido.vida = (personagem_escolhido.vida - self.nemesis.dano)
            if personagem_escolhido.vida == 0:
                personagem_escolhido.vida += (personagem_escolhido.vida + personagem_escolhido.vida)
            if personagem_escolhido.vida < 0:
                print('Você Perdeu! 🤣')
                break                
            print(f'{self.nemesis.nome} te atacou! você ficou com {personagem_escolhido.vida} de vida')
            time.sleep(0.5) 



       




    nemesis = Inimigo('Nemesis','Lança míssil', 25, 150 )
    mr_x = Inimigo('Mister X','Soco', 10, 10 )
    
    leon_kennedy = Herois('Leon', 'Pistola',15,100)
    chris_redfield = Herois('Chirs', 'Sub-metralhadora',17,135)
    ethan = Herois('Ethan', 'Shotgun',12,170)
personagem_escolhido = Luta('a','a',0,0)