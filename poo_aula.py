class Veiculo:
    def __init__(self, cor, n_rodas, placa):
        self.cor = cor
        self.n_rodas = n_rodas
        self.placa = placa
        
    def freiar (self):
        print("Freiando")
        

class Moto(Veiculo):
    pass

class Bike:
    
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor 
        self.modelo = modelo
        self.ano = ano
        self.valor = valor 
         
    
    def buzinar(self):
        print("Plim plim")
    
    def parar(self):
        print("Parando bicicleta...")
        print("Parou")
        
    def correr(self):
        print("Vruuuummmm...")
        
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"



b1 = Bike("vermelha", "mountain", 2020, 799)
b1.buzinar()
b1.correr()
b1.parar()

print(b1.cor)
print(b1)

moto1 = Moto("preta","2","aab-1122")
print(moto1.cor)
#Bike.buzinar() necessitaria de um argumento (objeto), ficando Bike.buzinar(b1) - (Bike é a classe, necessita um argumento)
#já b1.buzinar() funciona pois o self chama o próprio objeto (b1) como argumento

