import datetime

menu = '''
=====================
[D] Depósito
[S] Saque
[E] Extrato
[Q] Sair
=====================
'''

saldo = 0
extrato = ''
num_saques = 0
LIMITE_SAQUE = 500
MAX_SAQUES_PERMITIDOS = 3

while True:
    opcao = input(menu)

    if opcao == 'D' or opcao == 'd':
        print('Depósito')

        valor_deposito = float(input('Informe o valor que deseja depositar: R$ '))

        if valor_deposito > 0:
            data = datetime.datetime.now()
            data_deposito = data.strftime('%d/%m/%y %H:%M:%S')

            extrato += f'Depósito de R$ {valor_deposito:.2f} realizado em {data_deposito} \n'

            saldo += valor_deposito

        else:
            print('O valor informado é invalido!')

    elif opcao == 'S' or opcao == 's':
        print('Saque')

        valor_saque = float(input('Informe o valor que deseja sacar: R$ '))

        if valor_saque > 0:
            if valor_saque > saldo:
                print('Saldo insuficiente!')
                continue

            if valor_saque > LIMITE_SAQUE:
                print('O valor solicitador excede o limite, por favor escolha um valor abaixo do limite.')
                continue

            if num_saques >= MAX_SAQUES_PERMITIDOS:
                print('Números de saques diário atingindo! Você só poderá realizar novos saques amanhã')
                continue

            data = datetime.datetime.now()
            data_saque = data.strftime('%d/%m/%y %H:%M:%S')
            num_saques += 1

            extrato += f'Saque de R$ {valor_saque} realizado em {data_saque} \n'

            saldo -= valor_saque

        else:
            print("O valor informado é invalido!")

    elif opcao == 'E' or opcao == 'e':
        print('============== Extrato ==============')

        if not extrato:
            print('Ainda não foi realizada nenhuma movimentação!')
        
        extrato += f'\n\nSaldo final de R$ {saldo:.2f}'

        print(extrato)
        print('=====================================')
    
    elif opcao == 'Q' or opcao == 'q':
        print('Obrigado por usar nossos serviços, até a próxima!')
        break
    
    else:
        print('Opção inválida! Por favor, escolha uma das opções do menu...')

