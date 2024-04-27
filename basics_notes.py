#Codigo de cola, todo comentado, aprendendo o basico do basico de python
#Se comenta usando o #, primeiramente

#Em python, n eh necessario declarar o tipo da variavel junto com ela (int,float,string) na maioria das vezes

i = 17 #(int)
f = 12.03 #(float se marca com ponto, NAO virgula)
s_d = "Isso eh uma string" 
s_s = 'Isso tambem eh uma string' #(em python, n importa se são aspas duplas ou só as aspas simples)
c = "s" #isso eh uma string de tamanho 1 que possui apenas um caracter, em python, n temos o tipo "char"
s_l = '''Isso eh uma string que pode ocupar varias linhas como essa 11
e essa 12, para isso utilizam 3 aspas simples, ou 3 aspas duplas'''

#para converter tipo: 

#FLOAT PARA INT

c_i = int(f)

#INT PARA FLOAT

c_f = float(i)

#STRING NUMERICA (char com numeros: valores por exemplo) PARA FLOAT

valor = "172.50"

c_fv = float(valor)

#print(c_fv) para teste

#INT PARA STRING

c_is = 1

c_s = str(c_is)

#para concatenar (juntar) duas strings: f"(texto opcional){str1}{str2}"

conc = f"concatenando valor {valor} e c_s {c_s} (string exemplo de conversao)"

#print (conc) - teste de funcionamento 

#funcoes de entrada e saida

#ent_s = str(input("Insira a entrada em str \n")) #recebe um valor que ja eh convertido em str/input permite escrever mensagens ao usuario sem usar print (\n p quebra de linha)
#ent_i = int(input("Insira a entrada em int \n")) #recebe um valor que ja eh convertido em int
#ent_f = float(input("Insira a entrada em float \n")) #recebe um valor em float

#print("A string foi:", ent_s) #exibe ao usuario o que foi coletado em string/ necessario por a "," para separar a mensagem do valor a ser exibido 
#print("O inteiro foi:", ent_i) #exibe ao usuario o que foi coletado em int
#print("O float foi:", ent_f) #exibe ao usuario o que foi coletado em float


#Operadores aritmeticos (+ - * /)

#soma
soma1 = 7 + 1
soma2 = 8 + 1 

soma = soma1+soma2

#subtracao 

sub1 = 8 - 1
sub2 = 9 - 1

sub = sub1-sub2

#multiplicacao

mul1 = 7*2
mul2 = 2*5

mul = mul1*mul2

#potenciacao

pot1 = 3**2
pot2 = 2**2

pot = pot1**pot2

#divisao

div1 = 18/3
div2 = 4/2

div = div1/div2

#modulo (resulta o resto de uma divisao)

mod = 25%2

#resultado inteiro de uma divisao

div_int = 25//2


#OPERADORES DE COMPARACAO (>,<,>=,<=,==,!=)/igual C, n vou escrever n, preguica

#OPERADORES DE ATRIBUICAO

#adicao

at_ad = 12
at_ad += 3

#subtracao

at_sub = 10
at_sub -= 1

#divisao

at_div = 10
at_div /= 2

#divisao inteira 

at_div_int = 25
at_div_int //= 2

#modulo

at_mod = 10
at_mod %= 3

#potencia

at_pot = 12
at_pot **= 2

#OPERADORES LOGICOS

#AND (todos tem que ser verdadeiros)

op_and = (at_ad > at_sub) and (at_ad < at_sub)

#OR (pelo menos um tem que ser verdadeiro)

op_or = (at_ad > at_sub) and (at_ad < at_sub)

#NOT (caso seja falso: retorna verdade/caso seja verdadeiro: retorna falso)

not_op = not op_or

#OPERADORES DE IDENTIDADE (is, is not)/ verificam se ocupam o mesmo espaço na memoria
op_id = 2
op_id1 = op_id
op_id1 is op_id 

#OPERADORES DE ASSOCIACAO (in, not in) /verifica se algo esta presente em uma string, vetor ou matriz

op_ass = "Teste"

op_as = "e" in op_ass

#ESTRUTURAS CONDICIONAIS (if,else,elif)

e_if = 1
e_if2 = 2

if e_if > e_if2: #para abrir o laco eh necessario usar ":"
    e_if = e_if2

elif e_if == e_if2: #eh utilizado quando se tem mais de um caso, mais de um if
    e_if += e_if2

else: #como nao tem mais condicionais, se utiliza o ":" no proprio else
    e_if2 = e_if

#ESTRUTURAS DE REPETICAO (for, while) E BUILT IN (range)

#for

texto = "HANAH"
comp = "ABC"

for nome in texto:
    nome.upper()
    if nome in comp:
        v_char = nome.upper()

#for/else
texto = "xxx"
comp = "ABC"

for nome in texto:
    nome.upper()
    if nome in comp:
        v_char = nome.upper()
        #print(v_char)
else:
    nome = "Vazio"    
    
#RANGE
#gera uma sequencia de numeros inteiros, com o inicio inclusivo e o final exclusivo
range(5) #gera uma sequencia de 5 numeros (0,1,2,3,4)/com um unico argumento, eh parada
range(2,10,2) #o primeiro eh o numero que ela comeca, o segundo eh o numero de parada(exclusivo), o terceiro eh o salto (conta de 2 em 2)

#RANGE NO FOR
#gera uma lista que servira de parametro para percorrer o que se eh pedido
mul7 = 0
for num in range(7,71,7):
    mul7 += num
    
#WHILE
#utilizado quando nao se conhece o criterio de parada especifico
#BREAK 
#utilizado para forcar a parada do laco de repeticao

#while True:
   # whl = int(input("Insira um valor: "))
    #if whl == 0:
        #break


#listas/vetores

vet = list("hanah")

#for letra in vet:
    #print(letra)

vet.pop() #trata a lista como uma pilha e retira o ultimo elemento adicionado
#vet.pop(0) #especificando qual elemento a ser retirado
vet1 = vet.copy() #faz uma copia da lista criada que permite alterar a copia sem alterar a fonte
vet.count("a") #procura quantas vezes o parametro se repete
vet.extend("ses") #adiciona o parametro no final da lista
vet.index("h") #mostra qual a primeira ocorrencia do parametro
vet.remove("n") #remove da lista o parametro passado, caso existam dois parametros iguais, ele remove o que aparece primeiro
vet.reverse() #escreve a lista ao contrario
vet.sort() #organiza a lista em ordem alfabetica
vet.sort(reverse=True) #depois de organizar a lista em ordem alfabetica, ele vai inverter a ordem da lista
 #vet.sort(key=lambda x: len(x)) #organiza a lista em tamanho dos elementos da lista
 #vet.sort(key=lambda x: len(x), reverse=True) #organiza a lista em tamanho dos elementos da lista, e inverte a ordem para ficar decrescente
 #sorted(vet) faz as mesmas coisas do sort, só que agora em forma de funcao
len(vet) #determina o tamanho da lista

#print(vet)

#dicionario

dados = {"nome":"Hanah","idade":"20"} #nome do dicionário = {"variavel_1": "valor_da_variavel_1", "variavel_2": "valor_da_variavel_2"}
dados["nome"] #vai printar: Hanah
dados["idade"] #vai printar: 20

#para atualizar valores individualmente
dados["Nome"] = "Maria"
dados["idade"] = "20"

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

telefone = contatos["giovanna@gmail.com"]["telefone"]  # "3443-2121"

#for chave, valor in contatos.items():
    #print(chave, valor)

#contatos.clear() #limpa todos os valores do dicionario
copia_contatos = contatos.copy() #gera uma copia do dicionario
resultado = dict.fromkeys(["nome", "telefone"])  # {"nome": None, "telefone": None} #cria sem atribuir valor

resultado = dict.fromkeys(["nome", "telefone"], "vazio")  # {"nome": "vazio", "telefone": "vazio"} #adicionou o valor "vazio"
resultado = contatos.get("guilherme@gmail.com", {})  # {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"} #busca os atributos da chave
resultado = contatos.items() #vai retornar uma lista de tuplas - primeiro termo vai ser a lista, segundo vai ser a tupla com as chaves e os atributos dela
resultado = contatos.keys() #retorna as chaves do dicionario
resultado = contatos.values() #retorna apenas os valores
resultado = contatos.pop("melaine@gmail.com", "não encontrado") #remove a chave, e mostra qual valor foi removido, caso o valor n tenha sido encontrado, ele retorna a mensagem setada
contatos.popitem() #remove o ultimo item, dá erro caso não seja encontrado nenhum valor
contatos.setdefault("idade", 28) #adiciona ao dicionario caso o valor nao exista
contatos.update({"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3322-8181"}}) #caso exista ele atualiza, caso nao exista ele adiciona os valores ao dicionario
resultado = "guilherme@gmail.com" in contatos #verifica se a chave está no dicionario e retorna True ou False
resultado = "telefone" in contatos["giovanna@gmail.com"] #verifica se o valor esta nessa chave especifica do dicionario
del contatos["guilherme@gmail.com"]["telefone"] #deleta o valor dessa chave
del contatos["giovanna@gmail.com"] #deleta essa chave no dicionario


#FUNCOES
def ola ():
    print("Olá mundo")

#def - define uma função
#ola - nome da função
# () - onde ficam os parametros (nesse caso não há nenhum)

def ola_nome(nome):
    print(f"Olá {nome}!")

#name = "Usuário"
#ola_nome(name)


    


