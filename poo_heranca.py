class Animal:
    
    def __init__(self, n_patas):
        self.n_patas = n_patas
        
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
    
        

class Ave(Animal):
    
    def __init__(self,cor_bico,**kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)
    
    pass

class Mamifero(Animal):
    
    def __init__(self, cor_pelo, **kw): 
        self.cor_pelo = cor_pelo 
        super().__init__(**kw)
   
    pass

class Cachorro(Mamifero):
    pass

class Gato(Mamifero):
    pass

class Leao(Mamifero):
    pass

class Ornitorrinco(Mamifero, Ave):
    pass


cachorro = Cachorro(n_patas = 4,cor_pelo="caramelo")
print(cachorro)

perry = Ornitorrinco(n_patas = 4, cor_pelo="verde", cor_bico = "laranja")
print(perry)
