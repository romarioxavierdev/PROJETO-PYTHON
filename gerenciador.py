# SISTEMA DE CONTROLE DE ESTOQUE
# Este projeto simula um sistema simples de estoque.
#
# Funcionalidades:
# - Cadastrar produtos
# - Listar produtos
# - Buscar produtos
# - Repor estoque
# - Registrar vendas
# - Gerar relatório do estoque
#
# O projeto utiliza conceitos básicos de Python, como:
# listas, dicionários, funções, estruturas condicionais,
# loops, tratamento de erros e manipulação de dados.


# Importamos o módulo datetime para registrar a data e o horário
# em que uma venda foi realizada.
from datetime import datetime



produtos = [
    {
        "id": 1,
        "nome": "Teclado",
        "preco": 89.90,
        "estoque": 12
    },
    {
        "id": 2,
        "nome": "Mouse",
        "preco": 49.90,
        "estoque": 8
    },
    {
        "id": 3,
        "nome": "Headset",
        "preco": 129.90,
        "estoque": 5
    }
]


# FUNÇÃO PARA ENCONTRAR UM PRODUTO
def encontrar_produto(id_produto):
    # Percorremos todos os produtos cadastrados.
    for produto in produtos:

        # Verificamos se o ID do produto atual é igual ao ID que estamos procurando.
        if produto["id"] == id_produto:

           
            return produto

    # Caso nenhum produto tenha o ID informado retornamos None para indicar que não encontramos.
    return None

# FUNÇÃO PARA CADASTRAR PRODUTO

def cadastrar_produto():
    print("\n========== CADASTRAR PRODUTO ==========")

    nome = input("Nome do produto: ").strip()


    if nome == "":
        print("O nome do produto não pode ficar vazio.")
        return

    try:
        preco = float(input("Preço do produto: "))

    # Se o usuário digitar algo que não seja um número lançará um ValueError.
    except ValueError:
        print("Digite um preço válido.")
        return

    if preco <= 0:
        print("O preço deve ser maior que zero.")
        return

    try:
        estoque = int(input("Quantidade inicial: "))

    # Tratamos o erro caso o usuário digite algo inválido.
    except ValueError:
        print("Digite uma quantidade válida.")
        return

    if estoque < 0:
        print("A quantidade não pode ser negativa.")
        return

    # Criamos um novo ID.
    # Se já existem produtos, pegamos o maior ID existente e adicionamos 1.
    # Caso a lista esteja vazia, o primeiro ID será 1.
    if produtos:
        novo_id = max(produto["id"] for produto in produtos) + 1
    else:
        novo_id = 1

    # dicionário para novo produto.
    novo_produto = {
        "id": novo_id,
        "nome": nome,
        "preco": preco,
        "estoque": estoque
    }

    # Adicionamos o novo produto à lista.
    produtos.append(novo_produto)

    print(f"\nProduto '{nome}' cadastrado com sucesso!")
    print(f"ID do produto: {novo_id}")


# FUNÇÃO PARA LISTAR PRODUTOS
 
def listar_produtos():
    print("\n==================== PRODUTOS ====================")

    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    # Criamos o cabeçalho da tabela.
    print(f"{'ID':<5} {'PRODUTO':<20} {'PREÇO':<12} {'ESTOQUE':<10}")
    print("-" * 50)

    # Percorremos cada produto da lista.
    for produto in produtos:

        # Mostramos as informações de cada produto.
        # O :.2f faz o preço aparecer com duas casas decimais.
        print(
            f"{produto['id']:<5} "
            f"{produto['nome']:<20} "
            f"R$ {produto['preco']:<9.2f} "
            f"{produto['estoque']:<10}"
        )



# FUNÇÃO PARA BUSCAR PRODUTO

def buscar_produto():
    print("\n========== BUSCAR PRODUTO ==========")

    # Pedimos ao usuário o nome ou parte do nome do produto.
    termo = input("Digite o nome do produto: ").strip().lower()

    # Verificamos se o usuário digitou alguma coisa.
    if termo == "":
        print("Digite um nome para realizar a busca.")
        return

    # Criamos uma variável para controlar se encontramos pelo menos um produto.
    encontrou = False

    # Percorremos todos os produtos.
    for produto in produtos:

        # O operador "in" verifica se o termo digitado está presente no nome do produto.
        # Usamos lower() para tornar a busca independente de letras maiúsculas ou minúsculas.
        if termo in produto["nome"].lower():

            print("\nProduto encontrado:")
            print(f"ID: {produto['id']}")
            print(f"Nome: {produto['nome']}")
            print(f"Preço: R$ {produto['preco']:.2f}")
            print(f"Estoque: {produto['estoque']}")

            # Informamos que encontramos pelo menos um produto.
            encontrou = True

    # Se nenhum produto foi encontrado, mostramos uma mensagem.
    if not encontrou:
        print("Nenhum produto encontrado.")


# FUNÇÃO PARA REPOR ESTOQUE

def repor_estoque():
    print("\n========== REPOSIÇÃO DE ESTOQUE ==========")

    # Primeiro mostra os produtos disponíveis.
    listar_produtos()

    try:
        id_produto = int(input("\nDigite o ID do produto: "))

    #  uma entrada que não seja numérica.
    except ValueError:
        print("Digite um ID válido.")
        return

    # Procuramos o produto através da função que criei.
    produto = encontrar_produto(id_produto)

    # Se o produto não existir, encerramos a função.
    if produto is None:
        print("Produto não encontrado.")
        return

    # Pedimos a quantidade que será adicionada.
    try:
        quantidade = int(input("Quantidade para adicionar: "))

    # Tratamos uma entrada inválida.
    except ValueError:
        print("Digite uma quantidade válida.")
        return

    # A quantidade precisa ser maior que zero.
    if quantidade <= 0:
        print("A quantidade deve ser maior que zero.")
        return

    # Atualizamos o estoque adicionando a nova quantidade.
    produto["estoque"] += quantidade

    # Mostramos o resultado da operação.
    print("\nEstoque atualizado com sucesso!")
    print(f"Produto: {produto['nome']}")
    print(f"Novo estoque: {produto['estoque']} unidades")



# FUNÇÃO PARA REGISTRAR VENDA

def registrar_venda():
    print("\n========== REGISTRAR VENDA ==========")

    listar_produtos()

    # pedimos o ID 
    try:
        id_produto = int(input("\nDigite o ID do produto vendido: "))
    except ValueError:
        print("Digite um ID válido.")
        return

    produto = encontrar_produto(id_produto)
    if produto is None:
        print("Produto não encontrado.")
        return
    try:
        quantidade = int(input("Quantidade vendida: "))

    except ValueError:
        print("Digite uma quantidade válida.")
        return

    if quantidade <= 0:
        print("A quantidade deve ser maior que zero.")
        return

    # Verificamos se existe estoque suficiente para realizar a venda.
    if quantidade > produto["estoque"]:
        print("Estoque insuficiente.")
        print(f"Disponível: {produto['estoque']} unidades.")
        return

    # Calculamos o valor total da venda.
    total = produto["preco"] * quantidade


    produto["estoque"] -= quantidade

    # Pegamos a data e o horário atuais.
    data_venda = datetime.now()

    # Formatamos a data para uma apresentação mais amigável.
    data_formatada = data_venda.strftime("%d/%m/%Y %H:%M")

    print("\nVenda registrada com sucesso!")
    print("-" * 40)
    print(f"Produto: {produto['nome']}")
    print(f"Quantidade: {quantidade}")
    print(f"Valor unitário: R$ {produto['preco']:.2f}")
    print(f"Total da venda: R$ {total:.2f}")
    print(f"Data: {data_formatada}")
    print(f"Estoque restante: {produto['estoque']}")
    print("-" * 40)



# FUNÇÃO DE RELATÓRIO

def gerar_relatorio():
    print("\n=============== RELATÓRIO ===============")

    # Se não houver produtos, não há relatório para gerar.
    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    # len() retorna a quantidade de elementos da lista.
    total_produtos = len(produtos)

    # sum() é utilizado para somar os valores de estoque de todos os produtos.
    total_unidades = sum(produto["estoque"] for produto in produtos)

    # Aqui calculamos o valor total armazenado no estoque.
    # Para cada produto: preço x quantidade em estoque
    # Depois somamos todos os resultados.
    valor_estoque = sum(
        produto["preco"] * produto["estoque"]
        for produto in produtos
    )

    # Contamos quantos produtos estão com estoque baixo = quantidade menor ou igual a 3.
    estoque_baixo = sum(
        1 for produto in produtos
        if produto["estoque"] <= 3
    )

    # Contamos produtos completamente sem estoque.
    sem_estoque = sum(
        1 for produto in produtos
        if produto["estoque"] == 0
    )

    print(f"Produtos cadastrados: {total_produtos}")
    print(f"Unidades em estoque: {total_unidades}")
    print(f"Valor total do estoque: R$ {valor_estoque:.2f}")
    print(f"Produtos com estoque baixo: {estoque_baixo}")
    print(f"Produtos sem estoque: {sem_estoque}")

    if estoque_baixo > 0:

        print("\nProdutos que precisam de atenção:")

        for produto in produtos:

            if produto["estoque"] <= 3:
                print(
                    f"- {produto['nome']} "
                    f"({produto['estoque']} unidades)"
                )


# FUNÇÃO DO MENU PRINCIPAL


def menu():
    # O while True mantém o sistema funcionando
    # continuamente até o usuário escolher sair.
    while True:

        # Mostramos o menu principal.
        print("\n")
        print("=" * 50)
        print("           SISTEMA DE CONTROLE DE ESTOQUE")
        print("=" * 50)
        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Buscar produto")
        print("4 - Repor estoque")
        print("5 - Registrar venda")
        print("6 - Relatório do estoque")
        print("0 - Sair")
        print("=" * 50)

      
        opcao = input("Escolha uma opção: ").strip()


        if opcao == "1":
            cadastrar_produto()

        elif opcao == "2":
            listar_produtos()

        elif opcao == "3":
            buscar_produto()

        elif opcao == "4":
            repor_estoque()

        elif opcao == "5":
            registrar_venda()

        elif opcao == "6":
            gerar_relatorio()

        elif opcao == "0":
            print("\nSistema encerrado. Até mais!")
            break

        else:
            print("\nOpção inválida. Escolha uma opção do menu.")



menu()
