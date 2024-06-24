from post_new_user import cadastrar_usuario
from excel import postExcel
import subprocess


# Lista para armazenar os usuários
lista_usuarios = []

def program():
    # Obtendo a quantidade de usuários a serem cadastrados
    try:
        quantidade = int(input("Quantas pessoas você deseja cadastrar? "))
    except ValueError:
        print("Valor inválido. Por favor, digite um número inteiro.")
        quantidade = 0

    # Coletando dados de cada usuário
    for _ in range(quantidade):
        usuario = cadastrar_usuario()
        lista_usuarios.append(usuario)
        # Exibindo a lista de usuários cadastrados
    print("\nUsuários cadastrados:")
    for usuario in lista_usuarios:
        print(usuario)
    postExcel(lista_usuarios)
    # Abrir Excel
    subprocess.run(['excel', 'tabelaUsuarios.xlsx']) 
    # Abrir PDF
    subprocess.run(['open', 'tabelaUsuarios.pdf'])




program()