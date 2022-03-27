#exemplo básico de classes em python

#a palavra class é uma keyword
class Nomecompleto:
    def __init__(self):
        self.nome = "sergio"
        self.sobrenome = "roberto"
#método para o nome completo
    def nome_completo(self):
        print("meu nome é :",self.nome,self.sobrenome)

n1 = Nomecompleto()
#acessando os atributos a partir da criação do objeto
print(n1.nome)
print(n1.sobrenome)
#chamando o método nome_completo
n1.nome_completo()
