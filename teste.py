import random
from random import randint, sample

lista_acerto_impar = []
lista_acerto_par = []

def listaNum():
    lista_num = sample(range(1, 80), 6)
    print("--------------------------------------")
    print("######", lista_num, "######")
    print("-------------------------------------- \n")
    return lista_num

def par(par_n):
    for i in range(par_n):
        lista_num = listaNum()
        n = int(input("Digite um número da lista que seja PAR: "))

        if n in lista_num:
            if n % 2 == 0:
                print('Parabens, você acertou, o numero ' + str(n) + ' é um numero Par. \n')
                lista_acerto_par.append(n)

            else:
                print('Infelizmente você não acertou, o numero ' + str(n) + ' não é um numero Par. \n')
        else:
            print('O numero digitado não se encontra presente na lista! \n')

        resultado_par = len(lista_acerto_par)
    return resultado_par

def impar(impar_n):
    for i in range(impar_n):
        lista_num = listaNum()
        n = int(input("Digite um número da lista que seja ÍMPAR: \n"))

        if n in lista_num:
            if n % 2 != 0:
                print('Parabens, você acertou, o numero ' + str(n) + ' é um numero ÍMPAR. \n')
                lista_acerto_impar.append(n)

            else:
                print('Infelizmente você não acertou, o numero ' + str(n) + ' não é um numero ÍMPAR. \n')
        else:
            print('O numero digitado não se encontra presente na lista! \n')

        resultado_impar = len(lista_acerto_impar)
    return resultado_impar

def main():
    print("Vamos Aprender Par ou Ímpar! \n" )
    placar_par = par(3)
    placar_impar = impar(3)

    print("Placar do Jogo! \n")
    print('Parabens, você acertou ' + str(placar_par) + ' pares e ' + str(placar_impar) + ' impares.' +' \n')




main()

