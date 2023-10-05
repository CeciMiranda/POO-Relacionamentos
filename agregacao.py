###Agregação

class Produto:
  def __init__(self, nome: str, valor: float):
    self.__nome = nome
    self.__valor = valor

# converte o objeto produto em string com
# os valores dos atributos
  def __str__(self):
    return f"Produto: {self.__nome}; Valor: {self.__valor}"


class CarrinhoDeCompras:
  def __init__(self):
    self.__itens = [] # agregação
    
  def adicionarProduto(self, produto: Produto):
    self.__itens.append(produto)
    print(f"{produto} adicionado ao carrinho")
    
  def finalizarCompra(self):
    print(f"Compra concluída com sucesso!")
    print("Relação de produtos:")
    for item in self.__itens:
      print(item)


# Testando as classes
produto1 = Produto("Camisa", 50)
produto2 = Produto("Calça", 100)
carrinho = CarrinhoDeCompras()
carrinho.adicionarProduto(produto1)
carrinho.adicionarProduto(produto2)
carrinho.finalizarCompra()