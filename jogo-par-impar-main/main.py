from pygame.draw import rect
import desenhista

from random import randint
from desenhista import (
    desenha_retangulo,
    desenha_texto,
    inicializa_desenhista,
    atualiza_desenhista,
)
import pygame


def main():
    lista_numeros = gera_lista_numeros()
    lista_atual = 0

    acertou_par = 0
    acertou_impar = 0

    pygame.init()
    if desenhista.tela is None:
        inicializa_desenhista()

    perg_tam = 120
    perg_y = 200
    perg_cor = (0, 0, 0)

    rect_tamanho = (250, 160)
    rect_pad = 50
    ret_cor = (255, 0, 0)

    texto_tam = 80
    texto_cor = (0, 0, 0)
    while lista_atual <= 6:
        if lista_atual < 6:
            main_screen = desenha_retangulo(
                (0, 0), (1920, 1080), (150, 150, 150), 0, desenhista.tela
            )

            if lista_atual < 3:
                perg_texto = "Clique no número par"
            else:
                perg_texto = "Clique no número ímpar"

            desenha_texto(
                perg_texto, None, perg_tam, (-1, perg_y), perg_cor, desenhista.tela
            )
            sprites = []
            for sprite in range(6):
                pos = gera_posicao(80, rect_tamanho[0], rect_pad, sprite)
                ret = desenha_retangulo(
                    (pos, -1), rect_tamanho, ret_cor, 0, main_screen
                )
                sprites.append(ret)
                texto = str(lista_numeros[lista_atual][sprite])
                desenha_texto(texto, None, texto_tam, (-1, -1), texto_cor, ret)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    sprites_clicados = [s for s in sprites if s.collidepoint(pos)]
                    ret_clicado = sprites_clicados[0]
                    indice_ret_clicado = sprites.index(ret_clicado)

                    if lista_atual < 3:
                        if lista_numeros[lista_atual][indice_ret_clicado] % 2 == 0:
                            acertou_par += 1
                    else:
                        if lista_numeros[lista_atual][indice_ret_clicado] % 2 == 1:
                            acertou_impar += 1
                    lista_atual += 1
        elif lista_atual == 6:
            tela_principal = desenha_retangulo(
                (0, 0), (1920, 1080), (150, 150, 150), 0, desenhista.tela
            )
            fim_txt = "Jogo finalizado"
            titulo = desenha_texto(
                fim_txt,
                None,
                perg_tam,
                (-1, perg_y),
                perg_cor,
                tela_principal,
            )
            texto_par = f"Você acertou {acertou_par} números pares!"
            sprite_texto_par = desenha_texto(
                texto_par,
                None,
                perg_tam,
                (-1, 250),
                perg_cor,
                titulo,
            )
            texto_impar = f"Você acertou {acertou_impar} números ímpares!"
            sprite_texto_impar = desenha_texto(
                texto_impar,
                None,
                perg_tam,
                (-1, 100),
                perg_cor,
                sprite_texto_par,
            )

            jogar_novamente = desenha_retangulo(
                (250, 200), (500, 200), ret_cor, 0, sprite_texto_impar
            )
            sair = desenha_retangulo(
                (800, 200), (500, 200), ret_cor, 0, sprite_texto_impar
            )
            desenha_texto(
                "Jogar",
                None,
                texto_tam,
                (-1, -1),
                perg_cor,
                jogar_novamente,
            )

            desenha_texto(
                "Sair",
                None,
                texto_tam,
                (-1, -1),
                perg_cor,
                sair,
            )

            sprites = [jogar_novamente, sair]

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    sprites_clicados = [s for s in sprites if s.collidepoint(pos)]
                    ret_clicado = sprites_clicados[0]
                    indice_ret_clicado = sprites.index(ret_clicado)

                    if indice_ret_clicado == 0:
                        lista_atual = 0
                        acertou_impar = 0
                        acertou_par = 0
                    elif indice_ret_clicado == 1:
                        fechar_jogo()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fechar_jogo()
        atualiza_desenhista()


def fechar_jogo():
    pygame.display.quit()
    pygame.quit()
    exit()


def gera_posicao(x_inicial: int, x_largura: int, x_padding: int, indice: int):
    return x_inicial + indice * (x_largura + x_padding)


def gera_lista_numeros(qtd_listas: int = 6, tamanho_lista: int = 6):
    return [gera_numeros(tamanho_lista) for _ in range(qtd_listas)]


def gera_numeros(tamanho_lista: int = 6):
    while True:
        par = 0
        impar = 0
        numeros = [randint(0, 99) for x in range(tamanho_lista)]
        for numero in numeros:
            if numero % 2 == 0:
                par += 1
            else:
                impar += 1
        if par != 0 and impar != 0:
            return numeros


if __name__ == "__main__":
    main()
