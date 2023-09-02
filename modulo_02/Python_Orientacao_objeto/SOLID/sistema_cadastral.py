# class SistemaCadastral:

#     def cadastrar(self, nome:str, idade:int) -> None:
#         if isinstance(nome, str) and isinstance(idade, int):
#             print('acessando o banco de dados ...')
#             print(f'cadastra o usuario: {nome}, Idade: {idade}')

#         else:
#             print('dados invalidos')



# usando padrão solid

class SistemaCadastral:

    def cadastrar(self, nome:str, idade:int) -> None:
        if self.__verificar_dados(nome, idade):
            self.__armazernar_usuario(nome,idade)
        else:
            self.__indicar_erro()


    def __verificar_dados(self, nome:str, idade:int) -> bool:
        if isinstance(nome, str) and isinstance(idade, int):
            return True
        return False
    
    def __armazernar_usuario(self, nome:str, idade: int) -> None:
        print('acessando o banco de dados ...')
        print(f'cadastra o usuario: {nome}, Idade: {idade}')

    def __indicar_erro(self) -> None:
        print('dados invalidos')


sis = SistemaCadastral()
sis.cadastrar('jonas',32)

