#STRINGS
nome = "hanah"

#maiuscula, minuscula, titulo
caps = nome.upper() #deixa todas as letras maiusculas
minusculo = nome.lower() #deixa todas as letras minusculas
prim_letra = nome.title() #deixa a primeira letra maiúscula

#tirando espaços em branco

space = "               espaco     "
no_space = space.strip() #remove todos os espacos em branco
no_leftspace = space.lstrip() #remove os espacos em branco da esquerda
no_rightspace = space.rstrip() #remove os espacos da direita

#juncoes e centralizacao

central = "centro"

meio = centro.center(10,"_") #mostra o conteudo da variavel centralizado com 10 caracteres ao todo, e ocupa os espacos em branco com _
#.center(X,"Y") X = quantidade de caracteres no total, Y = caracter a ser utilizado para preencher os espaços em branco

entre = "*".join(central) #insere o caracter entre os caracteres do parametro
#"x".join(y) x = caracter a ser inserido, y = a variavel que vai receber esses caracteres


#APRESENTAR VARIAVEIS NA STRING (INTERPOLAÇÃO DE STRINGS)

#dado = 2024

string = f"Olá, estamos em {nome}" #o "f" nos permite inserir uma variavel dentro da string sem precisar alterar a string completamente
print(string)
#dado -= dado

string2 = f"Olá, estamos em {nome}"


#STRING TRIPLA
#para gerar uma string com várias linhas, basta usar aspas simples ou duplas 3x, ex:
string_longa = """Olá,
esse é um exemplo de como escrever uma string
utllizando varias linhas. Esse método mantem as quebras de linha
presentes na declaração da string, sem necessitar o '\n'"""
