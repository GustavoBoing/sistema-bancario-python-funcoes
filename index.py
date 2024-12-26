import time
import textwrap

def depositar(contas):
    numero_conta = int(input("\nDigite o numero da conta para deposito: "))
    verifica_conta = existe_conta(numero_conta, contas)
    if verifica_conta:
        valor = float(input("\nDigite um valor para depósito(apenas números):  "))
        while(valor < 0):
            print("\nValor inválido pois é um valor negativo. Tente novamente")
            time.sleep(2)
            valor = float(input("\nDigite um valor para depósito(apenas números): "))
        verifica_conta["saldo"] += valor
        print("Depositando...")
        time.sleep(2)
        print("Depósito concluído!!!")
        time.sleep(2)
        verifica_conta["extrato"] += f"\n\t\t\tVocê depositou R${valor}"
    else:
        print("O numero de conta digitado não existe!")
    

def saque(*,contas):
    LIMITE = 500
    LIMITE_SAQUE = 3 
    numero_conta = int(input("\nDigite o numero da conta para deposito: "))
    verifica_conta = existe_conta(numero_conta, contas)
    if(verifica_conta["saque_diario"] < LIMITE_SAQUE):
        valor = float(input("\nDigite um valor para saque(apenas números): "))
        if(valor > verifica_conta["saldo"]):
            print("\nValor inválido pois seu saldo é menor do que o valor que deseja sacar. Tente novamente")
        elif(valor > LIMITE):
            print("\nValor inválido pois seu limite por saque é menor. Tente novamente")
        else:
            verifica_conta["saldo"] -= valor
            print("Sacando....")
            time.sleep(2)
            print("Saque concluído!!")
            time.sleep(2)
            verifica_conta["extrato"] += f"\n \t\t\tVocê sacou R$ {valor}" 
            verifica_conta["saque_diario"] += 1
    else:
        print("\nVocê ja fez a qtd maxima de saques diários")


def extrato_func(saldo,/,*,extrato):
        print("\nImprimindo extrato....\n")
        time.sleep(2)
        print(extrato)
        print(f"\n Seu saldo é de R$ {saldo}")
        time.sleep(2)

def criar_usuario(usuarios):
    cpf = input("Informe o CPF do user: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if (usuario != None):
        print("\nJá existe um usuario com esse CPF!!!")
        return

    nome = input("Digite o nome do usuario: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    saldo = 0

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco, "saldo": saldo})

    print("Usuario criado com sucesso!!!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o cpf do user: ")
    usuario = filtrar_usuario(cpf, usuarios)
    saldo = 0
    saque_diario = 0

    if (usuario != None):
        print("Conta criada com sucesso!")
        return {"agencia":agencia, "numero_conta":numero_conta, "usuario": usuario, "saldo": saldo, "saque_diario": saque_diario, "extrato": ""}
    
    print("\nUsuario não encontrado, fluxo de criação de conta encerrado")

def existe_conta(num_conta, contas):
    for conta in contas:
        if conta["numero_conta"] == num_conta:
            return conta
    return None

def listar_contas(contas):
    for conta in contas:
        #print(f"CPF : {conta["usuario"]}\nNome : {conta["numero_conta"]}")
        linha = f"""
        Agência: \t{conta["agencia"]}
        C/C: \t\t{conta["numero_conta"]}
        Titular: \t{conta['usuario']['nome']}
        Saldo: \t\t{conta['saldo']} 
        Qtde. Saques hj: {conta['saque_diario']} 
        extrato: \t\t{conta['extrato']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

#def criar_conta(agencia, numero_conta, usuarios):

extrato = """ """
saldo = 0
AGENCIA = "0001"
usuarios = []
contas = []

menu = """
Digite uma opção: 

[1] Depositar
[2] Sacar
[3] Extrato
[4] Novo Usuario
[5] Nova conta
[6] Listar conta
[7] Sair

"""

while True:
    opcao = input(menu)

    if opcao == "1":
        depositar(contas)
    elif opcao == "2":
       saque(contas = contas)
    elif opcao == "3":
        extrato_func(saldo, extrato=extrato)
    elif opcao == "4":
        criar_usuario(usuarios)
    elif opcao == "5":
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)
        if conta:
            contas.append(conta)
    elif opcao == "6":
        listar_contas(contas)
    elif opcao == "7":
        print("\nVocê apertou na opção de sair!!\nVolte Sempre!!")
        break
    else:
        "A opção digitada é inválida"