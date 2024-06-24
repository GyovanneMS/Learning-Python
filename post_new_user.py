from datetime import datetime
from assistance import traduzir_mes

# Função para coletar dados de um único usuário
def cadastrar_usuario():
    print('Olá, esse é o sistema XYZ, vamos te cadastrar, OK?')

    nome = input('Vamos começar com o seu nome, qual é o seu nome e sobrenome? ')
    idade = int(input('Por favor, qual a sua idade? '))
    peso = float(input('Para nós, o seu peso é necessário, por favor, poderia dizê-lo? '))

    resposta = input("Você gostaria de um apelido? Se sim, é só dizer, se não só dê enter: ").strip()
    if resposta:
        apelido = resposta
        apelidoBool = True
        print(f"Apelido definido: {apelido}")
    else:
        apelido = None
        apelidoBool = False
        print("Nenhum apelido foi definido.")

    while True:
        try:
            nascimento_str = input("Digite o dia que você nasceu no formato DD/MM/AAAA: ")
            nascimento = datetime.strptime(nascimento_str, "%d/%m/%Y")
            dia = nascimento.day
            mes = nascimento.month
            mes = traduzir_mes(mes)
            ano = nascimento.year
            break  # Se a data for válida, saia do loop
        except ValueError:
            print("Formato inválido. Por favor, tente novamente.")

    # Criando o dicionário de usuário com os dados coletados
    usuario = {
        'nome': nome,
        'idade': idade,
        'peso': peso,
        'apelidoBool': apelidoBool,
        'apelido': apelido,
        'dataNascimento': '{0} de {1} de {2}'.format(dia, mes, ano)
    }
    
    return usuario