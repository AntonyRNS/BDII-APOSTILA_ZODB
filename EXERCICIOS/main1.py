from persistent import Persistent
from persistent.list import PersistentList
from datetime import date, datetime

class Produto(Persistent):
    def __init__(self, nome, validade, estoque):
        self.nome = nome
        self.validade = validade
        self.estoque = estoque

    def aumentar_estoque(self, quantidade):
        self.estoque += quantidade
            
    def diminuir_estoque(self, quantidade):
        self.estoque -= quantidade
        
    def verificar_validade(self):
        data_validade = datetime.strptime(self.validade, '%d/%m/%Y')
        validade_timestamp = round(data_validade.timestamp())
        agora_timestamp = round(datetime.now().timestamp())
        oitodias = 86400 * 8
        dias_ate_vencimento = (validade_timestamp - agora_timestamp) / 86400

        
        # if (validade_timestamp + oitodias) < agora_timestamp:
        if dias_ate_vencimento > 8:
            return 'Produto dentro da validade.'
        else:
            return f'Produto fora da validade há {abs(dias_ate_vencimento):.0f} dias.'
        
        

class Lista_de_produtos(Persistent):
    def __init__(self):
        self.produtos = PersistentList()
    def adicionar_produto(self, produtoP):
        produto = Produto(produtoP.nome, produtoP.validade, produtoP.estoque)
        self.produtos.append(produto)
        self._p_changed = 1

    def remover_produto(self, produto):
        self.produtos.remove(produto)
        self._p_changed = 1

    def listar_produtos(self):
        for produto in self.produtos:
            print(produto.nome, produto.validade, produto.estoque)

        

produto_teste1 = Produto("teste", "10/10/2023", 10)
produto_teste2 = Produto("teste2", "10/10/2024", 10)
produto_teste3 = Produto("teste3", "10/02/2025", 10)

lista = Lista_de_produtos()
lista.adicionar_produto(produto_teste1)
lista.adicionar_produto(produto_teste2)
lista.adicionar_produto(produto_teste3)

lista.listar_produtos()


for i in lista.produtos:
    print(i.verificar_validade())

