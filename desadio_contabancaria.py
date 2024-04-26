#Definindo os valores iniciais e limites

saldo = 0
limite = 500
extrato = ""
num_saque = 1
LIMITE_SAQUE = 3

#Apresentando o menu ao usuário
 
msg = """
Insira qual operação a ser realizada:
(1) Depósito
(2) Saque
(3) Extrato 
(4) Sair

=> """






while True:
    
    #recebendo a entrada do usuário
    print(msg)
    op = int(input())
    
    
    #analisando qual valor foi recebido
    if op == 1:
        valor = float(input("Insira o valor do valor do depósito: "))
        
        if valor < 0:
            print("Valor informado é inválido! \n")
            
        else: 
            saldo += valor
            extrato += f"Depósitos: R${saldo:.2f} \n"
            
    elif op == 2: 
        valor = float(input("Valor a ser sacado: ")) 
        
        sem_saldo = valor > saldo
        sem_lim = valor > limite
        sem_saque = num_saque > LIMITE_SAQUE
        
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
            
        else:
            print("ENTRADA INVÁLIDA! OPERAÇÃO NÃO REALIZADA ")
            
    elif op == 3:
            print("____________EXTRATO____________ ")
            print("Não foram realizadas operações" if not extrato else extrato)
            print(f"Saldo: R${saldo:.2f}\n ")
            print("_______________________________ \n")
                       
    elif op == 4:
        break
    
    else:
        print("Operação inválida, por favor insira a opção desejada. \n")