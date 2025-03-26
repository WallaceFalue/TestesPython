from random import randint

jogo = input('Vamos jogar um jogo? \n [y/n]:').lower()
if jogo == 'y':
    print('Serão 10 rounds \n Você ganha se acertar pelo menos 1')
    pc = 0
    for c in range(10):
        n = int(input('Escolha um número de 1 a 10: '))
        nc = randint(1, 10)
        print(f'Meu número: {nc}')
        if n == nc:
            print('Parabéns!!! Você ganhou!')
            break
        elif n != nc:
            pc += 1
            if pc == 1:
                print(f'Infelizmente você perdeu! Placar: (0x{pc}')
            elif pc >= 1:
                print(f'Que pena! Perdeu mais uma! Placar: (0x{pc})')
else:
    print('blz então, até mais!')
