class MinhaClasse:

    def __init__(self, atibuto):
        self.meu_atributo = 'Ola Mundo'
        self.meu_atributo2 = atibuto

    def meu_metodo(self):  # self significa que está no contexto da classe
        print( 'Estou no metodo! ')
        print(self.meu_atributo2)


    def meu_metodo2(self, num, mult):
        return num * mult
    
objeto = MinhaClasse('meu atributo')
atributo = objeto.meu_atributo2
print(atributo)
objeto.meu_metodo()