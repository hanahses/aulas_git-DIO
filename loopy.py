#LOOP GAME
print("\nBem vindo ao LOOP GAME: caso queira jogar, você estará preso até descobrir a senha! \nBOA SORTE!!\n") #mensagens iniciais ao usuario
print("Para jogar, pressione 'P' \nPara sair, pressione 'L' \n")

while True:
    entrar = str(input("Aceita esse desafio? ")) #entrar no jogo ou n

    if entrar.lower() == "p" : #verifica se o usuario entra no jogo
        senha = 12 #gera a senha
        
        while True: #cria o loop infinito
            
            res  = int(input("Insira a senha (número inteiro): ")) #recebe a entrada do usuario
       
            if res == senha: #confere se a entrada eh igual a senha correta
                print("Você desvendou a senha, parabéns! Voltarei mais forte da próxima vez! \n")
                exit() #sai do jogo caso o usuario acerte a senha
            else: #exibe a mensagem antes de reiniciar o loop
                print("Tente novamente")
    
    elif entrar.lower() == 'l':
        exit() #sai do jogo caso o usuario responda qualquer outra coisa

    else:
        print("Entrada inválida, por favor insira uma entrada válida \n")


#update ideas:
#add count, mostra uma dica após 5 jogadas, outra após 10, outra após 20 (using count and if)
#add quente ou frio: compara a resposta do usuário, caso esteja cerca de 3 casas abaixo ou acima mostra que está perto
#add niveis: primeiro nível (1 digito), segundo nível (2 digitos), terceiro nivel (3 digitos), quarto nivel (4 digitos), quinto nivel (5 digitos)
#aprender a usar o random, definir senhas como multiplos e divisores usando o % 
    
    
    
     
       
