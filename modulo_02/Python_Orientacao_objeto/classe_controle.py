class ControleRemoto:

    def __init__(self, televisao, comodo):
        self.televisao = televisao
        self.comodo = comodo
        
    def avacar_canal(self):
        print('avancar canal')
    
    def voltar_canal(self):
        print('voltar canal')

    def escolher_canal(self,canal):
            print(f'Alterado para o canal: {canal} ')



controle_sala = ControleRemoto('sansung', 'sala')
print(controle_sala.comodo)
print(controle_sala.televisao)
controle_sala.avacar_canal()
controle_sala.escolher_canal(12)


controle_quarto = ControleRemoto('LG', 'quarto')
print(controle_sala.comodo)
print(controle_sala.televisao)
controle_sala.avacar_canal()
controle_sala.escolher_canal(24)