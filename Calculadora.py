from math import sqrt

n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))
operador = input('Operador [+, -, *, /, **, √(r2)]: ').lower()

if operador == '+':
    print(f'{n1} + {n2} = {n1 + n2}')
elif operador == '-':
    print(f'{n1} - {n2} = {n1 - n2}')
elif operador == '*':
    print(f'{n1} * {n2} = {n1 * n2}')
elif operador == '/':
    if n2 != 0:
        print(f'{n1} / {n2} = {n1 / n2}')
    else:
        print('Erro: divisão por zero.')
elif operador == '**':
    expoente = int(n2)
    valor = n1
    for _ in range(expoente - 1):
        valor *= n1
    print(f'{n1} ** {n2} = {valor}')
elif operador == 'r2':
    print(f'Raiz quadrada de {n1} = {sqrt(n1)}')
else:
    print('Erro: operação inválida.')
