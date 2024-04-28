"""

#Desafio 1

C = int(input()) 
for i in range (C): 
   N = int(input())

   if N > 8000:
      print("Mais de 8000!")
   
   else:
      print("Inseto!")
      
"""

"""
#Desafio 2

T = int(input())

for i in range(T):
    N, K = input().split(' ')
    K = int(K)
    N = int(N)

    if N<K:
        print(f"{N}")

    else:
        n_garrafas = N//K
        n_garrafas += N%K

        print(n_garrafas)

"""
"""

 

#Desafio 3


c1=input()
c2=input()
c3=input()
if (c1=="vertebrado"):
    if (c2=="ave"):
        if(c3=="carnivoro"):
            print("aguia")
        elif(c3=="onivoro"):
            print("pomba")
    elif(c2=="mamifero"):
        if(c3=="onivoro"):
            print("homem")
        elif(c3=="herbivoro"):
            print("vaca")
elif(c1=="invertebrado"):
    if(c2=="inseto"):
        if(c3=="hematofago"):
            print("pulga")
        elif(c3=="herbivoro"):
            print("lagarta")
    elif(c2=="anelideo"):
        if(c3=="hematofago"):
            print("sanguessuga")
        elif(c3=="onivoro"):
            print("minhoca")


"""
