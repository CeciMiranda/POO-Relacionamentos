class Historico:
  def __init__(self):
    self.__operacoes : str = []
    
  def __str__(self) -> str:
    resposta = "Transações: \n"
    for operacao in self.__operacoes:
      resposta += f"--> {operacao} \n"
      return resposta
    
  def registrar(self, operacao: str):
    self.__operacoes.append(operacao)


class Conta:
  def __init__(self, cliente:str):
    self.__cliente = cliente
    self.__saldo = 0
    self.__historico = Historico() # composição

  def sacar(self, valor):
    if (self.__saldo < valor):
      return False
    else:
      self.__saldo -= valor
      self.__historico.registrar(f"Saque de {valor}")
      return True
      
  def depositar(self, valor):
    self.__saldo += valor
    self.__historico.registrar(f"Depósito de {valor}")

  def consultarSaldo(self):
    print(f"Cliente: {self.__cliente} --> saldo: {self.__saldo}")
    self.__historico.registrar(f"Consulta de saldo: {self.__saldo}")
    
  def emitirExtrato(self):
    print(f"\nCliente: {self.__cliente}")
    print(self.__historico)