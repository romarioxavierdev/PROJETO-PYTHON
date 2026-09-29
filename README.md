# Sistema de Controle de Estoque

Projeto desenvolvido em **Python** com o objetivo de praticar conceitos fundamentais da linguagem através da criação de um sistema simples de controle de estoque.

## Sobre o projeto

O sistema simula algumas operações básicas de uma loja, permitindo cadastrar e consultar produtos, controlar quantidades em estoque, registrar vendas e visualizar informações gerais do estoque.

O projeto foi desenvolvido como uma aplicação de terminal, com foco em organização do código, reutilização de funções e validação das entradas fornecidas pelo usuário.

## Funcionalidades

* Cadastro de produtos
* Listagem de produtos
* Busca de produtos por nome
* Reposição de estoque
* Registro de vendas
* Atualização automática do estoque após uma venda
* Validação de entradas do usuário
* Tratamento de erros com `try/except`
* Registro de data e horário das vendas
* Relatório geral do estoque
* Identificação de produtos com estoque baixo
* Identificação de produtos sem estoque

## Tecnologias utilizadas

* **Python 3**
* Biblioteca padrão `datetime`

Não foram utilizadas bibliotecas externas.

## Conceitos praticados

Durante o desenvolvimento foram utilizados conceitos fundamentais de Python, incluindo:

* Variáveis
* Listas
* Dicionários
* Funções
* Parâmetros e retornos
* Estruturas condicionais (`if`, `elif`, `else`)
* Estruturas de repetição (`for` e `while`)
* Tratamento de exceções (`try` e `except`)
* Manipulação de strings
* Operações matemáticas
* Formatação de valores
* Importação de módulos
* Entrada e saída de dados pelo terminal

## Estrutura do projeto

Atualmente, o projeto está organizado em um único arquivo:

```text
sistema-estoque/
│
├── main.py
└── README.md
```

O arquivo `main.py` contém toda a lógica da aplicação.

## Como executar

### 1. Pré-requisito

É necessário ter o **Python 3** instalado no computador.

Para verificar a instalação, execute no terminal:

```bash
python --version
```

ou:

```bash
py --version
```

### 2. Clonar o projeto

```bash
git clone URL_DO_REPOSITORIO
```

Depois, entre na pasta:

```bash
cd sistema-estoque
```

### 3. Executar

Execute:

```bash
python main.py
```

No Windows, também pode ser utilizado:

```bash
py main.py
```

## Exemplo de utilização

Ao iniciar o programa, será apresentado um menu:

```text
==================================================
           SISTEMA DE CONTROLE DE ESTOQUE
==================================================
1 - Cadastrar produto
2 - Listar produtos
3 - Buscar produto
4 - Repor estoque
5 - Registrar venda
6 - Relatório do estoque
0 - Sair
==================================================
Escolha uma opção:
```

A partir desse menu, o usuário pode realizar as operações disponíveis.

## Próximas melhorias

Algumas melhorias planejadas para versões futuras:

* Persistência dos dados utilizando arquivos JSON
* Implementação de banco de dados
* Histórico de vendas
* Separação do projeto em diferentes módulos
* Sistema de login e usuários
* Interface gráfica ou aplicação web
* Exportação de relatórios

## Objetivo

Este projeto faz parte dos meus estudos de Python e desenvolvimento de sistemas, buscando transformar conceitos básicos da linguagem em uma aplicação prática e funcional.

## Autor

Romário

Projeto desenvolvido para fins de estudo e prática em programação.
