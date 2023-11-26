import random
import time


def escolharcerta (): #função para saber se o usuario vai escolher uma das opções proposta 
    decs = input ("\nDigite sua escolhar: ")

    while (decs not in padrao ):
        print("\nErro não temos essa opcão, digite novamente...")
        decs = input ("\nDigite sua escolhar: ")

    return decs


#Fazendo um menu para o usuario

padrao = ["1","2","3"]

dic = {'1' : "Pedra", '2': "Tesoura", '3': "Papel"}

while True:

    print (">_<"*7)
    print ("|  [1] - Jogar      |")
    print ("|  [2] - Sobre      | ")
    print ("|  [3] - Sair       | ")
    print (">_<"*7)



    escolhar = escolharcerta() #chamando a função para receber o valor correto

    if escolhar == "1":
        print (">-<"*7)
        print ("|  [1] - Pedra      |")
        print ("|  [2] - Tesoura    | ")
        print ("|  [3] - Papel      | ")
        print (">-<"*7)

        decisao = escolharcerta()

        decisao = dic [decisao] # Usando o dicionario para descobrir a escolhar do usuario

        adver = dic [str(random.randint(1,3))] # Pegando um numero aleatorio é usando o dicionario para troca o numero por uma opção


        if adver == decisao:
            for x in range (0,4):
                print ("." * x) 
                time.sleep(1)
            print(f"O computador escolheu: {adver}")
            print("Que pena!!!")
            print("Você empatou com o computador >~<\n")

        elif decisao == "Pedra":

            if adver == "Papel":
                for x in range (0,4):
                    print ("." * x) 
                    time.sleep(1)
                print(f"O computador escolheu: {adver}")
                print("Que pena!!!")
                print("Você Perdeu para o computador >~<\n")
            
            else:
                for x in range (0,4):
                    print ("." * x) 
                    time.sleep(1)
                print(f"O computador escolheu: {adver}")
                print("Parabéns, Surgiu uma nova lenda no Jokempo!!")
                print("Você Ganhouu do computador >.<\n")
            
        
        elif decisao == "Tesoura":

            if adver == "Pedra":
                for x in range (0,4):
                    print ("." * x) 
                    time.sleep(1)
                
                print(f"O computador escolheu: {adver}")
                print("Que pena!!!")
                print("Você Perdeu para o computador >~<\n")

            else:
                for x in range (0,4):
                    print ("." * x) 
                    time.sleep(1)
                
                print(f"O computador escolheu: {adver}")
                print("Parabéns, Surgiu uma nova lenda no Jokempo!!")
                print("Você Ganhouu do computador >.<\n")

        elif decisao == "Papel":

            if adver == "Tesoura":
                for x in range (0,4):
                    print ("." * x) 
                    time.sleep(1)
                
                print(f"O computador escolheu: {adver}")
                print("Que pena!!!")
                print("Você Perdeu para o computador >~<")

            else:
                for x in range (0,4):
                    print ("." * x) 
                    time.sleep(1)
                
                print(f"O computador escolheu: {adver}")
                print("Parabéns, Surgiu uma nova lenda no Jokempo!!")
                print("Você Ganhouu do computador >.<")


    elif escolhar == "2":
        print ("\nOlá meu nome é Carlos Vitor Freitas Santos")
        print ("Fiz esse projeto para treinar meu entendimento sobre o Python, como também, para mim distraiar um pouco... ")
        print ("Torça que tenha apreciado e tenha uma otima gameplay >.<")
        print ("\n " * 3)
        print ("Email: Carlosvit26@gmail.com \nTelefone: (87) 99911-3105")

    else:
        print("Fim do programa...")
        print("Obrigado por jogar, tmj")
        break