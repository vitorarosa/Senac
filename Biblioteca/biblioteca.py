import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QListWidget

class LibraryApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Biblioteca')
        self.setMinimumSize(300, 200)

        # Criar widgets
        self.label_titulo = QLabel('Título:')
        self.label_autor = QLabel('Autor:')
        self.input_titulo = QLineEdit()
        self.input_autor = QLineEdit()
        self.button_cadastrar = QPushButton('Cadastrar')
        self.button_buscar = QPushButton('Buscar')
        self.lista_livros = QListWidget()

        # Definir layout
        layout = QVBoxLayout()
        layout.addWidget(self.label_titulo)
        layout.addWidget(self.input_titulo)
        layout.addWidget(self.label_autor)
        layout.addWidget(self.input_autor)
        layout.addWidget(self.button_cadastrar)
        layout.addWidget(self.button_buscar)
        layout.addWidget(self.lista_livros)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Conectar sinais de clique dos botões
        self.button_cadastrar.clicked.connect(self.cadastrar_livro)
        self.button_buscar.clicked.connect(self.buscar_livros)

        # Lista para armazenar os livros cadastrados
        self.livros = []

    def cadastrar_livro(self):
        titulo = self.input_titulo.text()
        autor = self.input_autor.text()

        # Verificar se o livro já está cadastrado
        for livro in self.livros:
            if titulo == livro['titulo'] and autor == livro['autor']:
                QMessageBox.warning(self, 'Erro', 'Livro já cadastrado.')
                return

        # Cadastrar novo livro
        self.livros.append({'titulo': titulo, 'autor': autor})
        QMessageBox.information(self, 'Cadastro', 'Livro cadastrado com sucesso!')
        self.input_titulo.clear()
        self.input_autor.clear()

    def buscar_livros(self):
        titulo = self.input_titulo.text()
        autor = self.input_autor.text()

        # Limpar lista de livros
        self.lista_livros.clear()

        # Buscar livros
        for livro in self.livros:
            if titulo and titulo.lower() not in livro['titulo'].lower():
                continue
            if autor and autor.lower() not in livro['autor'].lower():
                continue
            self.lista_livros.addItem(f"{livro['titulo']} - {livro['autor']}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LibraryApp()
    window.show()
    sys.exit(app.exec())
