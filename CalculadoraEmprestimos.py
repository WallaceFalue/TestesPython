from time import sleep

print('Regras do empréstimo: \n'
      '1º: Não há juros mensais até R$ 1000\n'
      '2º: De R$ 1000 até R$ 10000, os juros são de 3% ao mês\n'
      '3º: Para valores acima de R$ 10000, os juros são de 6% ao mês\n'
      '4º: Em qualquer opção, há juros anuais de 12% ao ano')

sleep(0.3)

valor = float(input('Valor que deseja adquirir (em reais): '))
tempo = int(input('Tempo total do parcelamento (em meses): '))

sleep(0.3)

juros_anuais = 12 / 100

if valor <= 1000:
    juros_mensais = 0
elif 1000 < valor <= 10000:
    juros_mensais = 3 / 100
else:
    juros_mensais = 6 / 100

montante_final = valor * ((1 + juros_mensais) ** tempo)

if tempo >= 12:
    montante_final *= (1 + juros_anuais) ** (tempo // 12)

print(f'O valor total a ser pago será de R$ {montante_final:.2f}')
