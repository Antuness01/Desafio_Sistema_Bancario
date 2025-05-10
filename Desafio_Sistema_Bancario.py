menu = '''
============= Menu ===========
|                            |
|       [3] Depositar        |
|       [2] Sacar            |
|       [1] Extrato          |
|       [0] Sair             |
|                            |
==============================
'''
saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

    
while True:

    opcao = input(menu)

    if opcao == '3':
        valor = float(input('Informe o valor do deposito: '))

        if valor > 0:
            saldo += valor
            extrato += f'Deposito: R$ {valor:.2f}\n'

        else:
            print('Deposito indisponivel no momento!!')
    
    elif opcao == '2':
          valor = float(input('Informe o valor que deseja sacar: '))

          exedeu_saldo = valor > saldo

          exedeu_limite = valor > limite

          exedeu_saques = numero_saques >= LIMITE_SAQUES

          if exedeu_saldo:
              print('Operação falho. Saldo insuficiente!!')
          
          elif exedeu_limite:
              print('Operação falhou. Limite insuficiente!!')

          elif exedeu_saques:
              print('Operação falho. Quantidades de saques exedidas!!')
          
          elif valor > 0:
              saldo -= valor
              extrato += f'Saque: R$ {valor:.2f}\n'
              numero_saques += 1

          else:
              ('Saque Indisponivel. Tente novamente mais tarde!!')

    elif opcao == '1':
        print('\n============Extrato===============')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'\n Saldo: R$ {valor:.2f}\n')
        print('=====================================')
    
    elif opcao == '0':
        break

    else:
        print('Operação Invalida. Selecione novamente a operação indesejada!!')

