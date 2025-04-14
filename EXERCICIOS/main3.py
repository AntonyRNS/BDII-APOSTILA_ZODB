from persistent import Persistent
from persistent.list import PersistentList
from datetime import datetime


class Livro(Persistent):
    def __init__(self, nome, autor):
        self.nome = nome
        self.autor = autor

    def __str__(self):
        return f'Nome: {self.nome}, Autor: {self.autor}'

class Biblioteca(PersistentList):
    def __init__(self):
        self.livros = PersistentList()

    def adicionar_livro(self, livro):
        livro = Livro(livro.nome, livro.autor)
        self.livros.append(livro)
        self._p_changed = 1

    def remover_livro(self, livro):
        self.livros.remove(livro)
        self._p_changed = 1

    def listar_livros(self):
        for livro in self.livros():
            print(livro)
class Usuario(Persistent):
    def __init__(self, nome_usuario, matricula):
        self.nome_usuario = nome_usuario
        self.matricula = matricula

    def __str__(self):
        return f'Nome do Aluno: {self.nome_usuario}, Matrícula do aluno: {self.matricula}'



class Emprestimo(Persistent):
    def __init__(self, livro, usuario):
        self.livro = livro.nome
        self.usuario = usuario.matricula
        self.data_emprestimo = datetime.now()

    def __str__(self):
        return f'Livro emprestado: {self.livro}, Usuario que pegou: {self.usuario}, data do empréstimo: {self.data_emprestimo}'


usuario1 = Usuario('Antony', 20250001)
livro1 = Livro('Como ser rico', 'Jubileu')

emprestimo1 = Emprestimo(livro1, usuario1)
print(emprestimo1)