####Associação

class Interruptor:
  def __init__(self, comodo: str):
    self.__comodo = comodo

  def acender(self):
    print(f"acendendo: {self.__comodo}")
    
  def apagar(self):
    print(f"apagando: {self.__comodo}")


class Pessoa:
  def __init__(self, nome:str):
    self.__nome = nome
    
  def acenderLampada(self, interruptor: Interruptor):
    print(f"Eu sou {self.__nome} e estou ", end="")
    interruptor.acender()
    
  def apagarLampada(self, interruptor: Interruptor):
    print(f"Eu sou {self.__nome} e estou ", end="")
    interruptor.apagar()
    
  def dormir(self):
    print(f"Eu, {self.__nome}, fui dormir...")


# Testando as classes
# Criação dos objetos
maria = Pessoa("Maria")
joao = Pessoa("João")
interruptor_sala = Interruptor("sala")
interruptor_quarto = Interruptor("quarto")

# O objeto interruptor pode ser usado por joao ou maria
maria.acenderLampada(interruptor_sala)
joao.apagarLampada(interruptor_sala)
maria.acenderLampada(interruptor_quarto)
maria.apagarLampada(interruptor_quarto)
maria.dormir()
joao.dormir()
