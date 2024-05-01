class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self._nome = nome
        self.ano_nascimento = ano_nascimento
        
    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        _ano_atual = 2024
        return _ano_atual - self.ano_nascimento
    
    
pessoa = Pessoa("Hanah", 2003)
print(f"Nome: {pessoa.nome} | Idade: {pessoa.idade}")
