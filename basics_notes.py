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
        print(v_char)
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

while True:
    whl = int(input("Insira um valor: "))
    if whl == 0:
        break















