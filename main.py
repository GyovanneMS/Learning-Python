from postNewUser import cadastrar_usuario

# Lista para armazenar os usuários
lista_usuarios = []

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
