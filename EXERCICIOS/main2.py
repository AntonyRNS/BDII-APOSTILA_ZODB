from persistent import Persistent
from persistent.list import PersistentList


class ItemCarrinho:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def __str__(self):
        return f"Item: {self.nome}, Preço: R${self.preco:.2f}, Quantidade: {self.quantidade}"



class Carrinho(PersistentList):
    def __init__(self):
        self.itens = PersistentList()


    def adicionar_item(self, item):
        item = ItemCarrinho(item.nome, item.preco, item.quantidade)
        self.itens.append(item)
        self._p_changed = 1

  
    def remover_item(self, item):
        self.itens.remove(item)
        self._p_changed = 1
    
    def listar_itens(self):
        for item in self.itens:
            print(item)


produto_teste1 = ItemCarrinho("teste1", 10.74, 4)
produto_teste2 = ItemCarrinho("teste2", 45.34, 7)
produto_teste3 = ItemCarrinho("teste3", 5.40, 2)

carrinho_teste = Carrinho()
carrinho_teste.adicionar_item(produto_teste1)
carrinho_teste.adicionar_item(produto_teste2)
carrinho_teste.adicionar_item(produto_teste3)


carrinho_teste.listar_itens()




        