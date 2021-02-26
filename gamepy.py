from models.calcular import Calcular

def main():
    pontos: int = 0
    jogar(pontos)

def jogar(pontos: int) -> None:
    dificuldade: int = int(input('Informe o nível de dificuldade desejado [1, 2, 3, 4]: '))

    calc: Calcular = Calcular(dificuldade)

    print('Informe o resultado para a seguinte operação: ')
    calc.mostrar_operacao()

    resultado: int = int(input())

    if calc.checar_resultado(resultado):
        pontos += 1
        print(f'Você tem {pontos} pontos!')

    #continuar: int = int(input('Deseja continuar jogando? [1-Sim, 0-Não]: '))  #Metodo comum
    if (continuar := int(input('Deseja continuar jogando? [1-Sim, 0-Não]: '))) == 1: #utilizando  o operador Walrus
        jogar(pontos)
    else:
        print(f'Você finalizou o jogo com {pontos} ponto(s)!')





if __name__ == '__main__':
    main()
