class Cliente:
    nome = ""
    salario = 0,0
    senha_cartao = 0
    

class Conta:
    saldo = 0,0
    deposito = 0,0
    saque = 0,0


def Menu():

    print("-"*30)
    print("1 - Saldo:")
    print("-"*30)
    print("2 - Deposito:")
    print("-"*30)
    print("3 - Saque:")
    print("-"*30)

# Informação do Cliente

Cliente.nome = input("Informe seu nome:")
Cliente.salario = float(input("Salario:"))
Cliente.senha_cartao = int(input("Crie uma senha secreta:"))

# Informação da Conta do Cliente

# conta = sum(Conta.saldo, Cliente.salario)



# Lógica do programa.

senha = int(input('Digite sua senha:'))
while True:
    if senha == Cliente.senha_cartao:
        print('Senha correta')        
        Menu()
        break
    else:
        print('Senha está incorreta')
        # for senha in range(3):
        #     print('Digite sua senha novamente:')
        break

opc = int(input('Escolha uma opção:'))    

if opc == 1:
    print('Saldo em Conta R$ {}'.format(Cliente.salario))
if opc == 2:
    valor_deposito = float(input('Digite o valor do deposito:'))
    calculo_deposito = (Cliente.salario + valor_deposito)  
    print('Valor depositado R$ {}'.format(valor_deposito))
    print("{}, sua conta tem R$ {}".format(Cliente.nome,calculo_deposito))

if opc == 3:
    saque = float(input("Valor do Saque:"))
    valor_saque = (Cliente.salario - saque)
    print("Saldo em conta R$ {}".format(valor_saque))
   



