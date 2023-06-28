# from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         password_input = QLineEdit(self)
#         password_input.setEchoMode(QLineEdit.Password)

#         self.setCentralWidget(password_input)

# if __name__ == "__main__":
#     app = QApplication([])
#     window = MainWindow()
#     window.show()
#     app.exec()

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

class LibraryApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Biblioteca Digital')
        self.setMinimumSize(300, 200)

        # Criar widgets
        self.label_email = QLabel('Email:')
        self.label_senha = QLabel('Senha:')
        self.input_email = QLineEdit()
        self.input_senha = QLineEdit()
        self.input_senha.setEchoMode(QLineEdit.Password)
        self.button_login = QPushButton('Login')
        self.button_cadastro = QPushButton('Cadastro')

        # Definir layout
        layout = QVBoxLayout()
        layout.addWidget(self.label_email)
        layout.addWidget(self.input_email)
        layout.addWidget(self.label_senha)
        layout.addWidget(self.input_senha)
        layout.addWidget(self.button_login)
        layout.addWidget(self.button_cadastro)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Conectar sinais de clique dos botões
        self.button_login.clicked.connect(self.login)
        self.button_cadastro.clicked.connect(self.cadastro)

        # Lista para armazenar as credenciais cadastradas
        self.credenciais = []

    def login(self):
        email = self.input_email.text()
        senha = self.input_senha.text()

        # Verificar credenciais
        for credencial in self.credenciais:
            if email == credencial['email'] and senha == credencial['senha']:
                QMessageBox.information(self, 'Sucesso', 'Login realizado com sucesso!')
                return

        QMessageBox.warning(self, 'Erro', 'Credenciais inválidas.')

    def cadastro(self):
        email = self.input_email.text()
        senha = self.input_senha.text()

        # Verificar se o email já está cadastrado
        for credencial in self.credenciais:
            if email == credencial['email']:
                QMessageBox.warning(self, 'Erro', 'Email já cadastrado.')
                return

        # Cadastrar nova credencial
        self.credenciais.append({'email': email, 'senha': senha})
        QMessageBox.information(self, 'Cadastro', 'Novo login criado com sucesso!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LibraryApp()
    window.show()
    sys.exit(app.exec())


