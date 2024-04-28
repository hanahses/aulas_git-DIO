def msg ():
    mensagem = """ Insira qual operação a ser realizada:
(1) Depósito
(2) Saque
(3) Extrato
(4) Novo usuário
(5) Nova conta
(6) Listar contas 
(7) Sair

=>"""

    return input(mensagem)


def depositar (saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósitos: R${saldo:.2f} \n"
        print("Depósito realizado com sucesso")
        
    else:
        print("Valor informado é inválido! \n")
            
    return saldo, extrato
    

def sacar (*, saldo, valor, extrato, limite, num_saque, limite_saques):
        
    sem_saldo = valor > saldo
    sem_lim = valor > limite
    sem_saque = num_saque > limite_saques
        
    if sem_saldo:
            print("SALDO INSUFICIENTE! OPERAÇÃO NÃO REALIZADA ")
            
    elif sem_lim:
            print("LIMITE INSUFICIENTE! OPERAÇÃO NÃO REALIZADA ")
            
    elif sem_saque:
            print("LIMITE DE SAQUES EXCEDIDO! OPERAÇÃO NÃO REALIZADA ")
            
    elif valor > 0:
            
            saldo -= valor
            num_saque += 1
            extrato += f"Saques: R${valor:.2f}\n"
            print("Saque realizado com sucesso!")
            
    else:
            print("ENTRADA INVÁLIDA! OPERAÇÃO NÃO REALIZADA ")

    return saldo, extrato


def ver_extrato (saldo, /, *, extrato):
    print("____________EXTRATO____________ ")
    print("Não foram realizadas operações" if not extrato else extrato)
    print(f"Saldo: R${saldo:.2f}\n ")
    print("_______________________________ \n")


def novo_usuario (usuarios):
    cpf = input("Insira o cpf (apenas números)")
    usuario = usuario_existente(cpf, usuarios)
    if usuario:
        print("Já existe um usuário com esse cpf cadastrado")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")
          

def usuario_existente (cpf, usuarios):
      existe_usuario = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
      return existe_usuario[0] if existe_usuario else None


def nova_conta(agencia, n_conta, usuarios):
    cpf = input("Insira o cpf (apenas números)")
    usuario = usuario_existente(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": n_conta, "usuario": usuario}
    
    print("Usuário não encontrado! Favor cadastrar um usuário para criar a conta!")

def ver_contas(contas):
     for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("="*100)
        print(linha)


def main():
    
    LIMITE_SAQUE = 3
    AGENCIA = "0001"
    saldo = 0
    limite = 500
    extrato = ""
    num_saque = 1
    usuarios = []
    contas = []

    while True:
        op = int(msg())
        if op == 1:
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif op == 2:
             valor = float(input("Informe o valor do saque: "))

             saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                num_saque=num_saque,
                limite_saques=LIMITE_SAQUE,
            )
 
        elif op == 3:
             ver_extrato(saldo, extrato=extrato)

        elif op == 4:
             novo_usuario(usuarios)

        elif op == 5:
            numero_conta = len(contas) + 1
            conta = nova_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif op == 6:
             ver_contas(contas)

        elif op == 7:
             break
        
        else:
             print("Operação inválida, por favor insira a opção desejada. \n")


main ()