"""
Nome do Projeto: Finanças Dev v1.0
Módulo: Módulo de cadastro básico
Autor: Ana Rachel Rodrigues da Costa
Data: 2026/02/06
Descrição: Esse módulo tem por objetivo coletar informações simples através da função input()
para coletar os dados necessários para essa primeira etapa do cadastro, usando os tipos primitivos, podendo ser:
tipo string: str() texto, Olá, mundo!
tipo inteiro: int() numero inteiro, 65
tipo ponto flutuante: float() número decimal, 65.00
tipo booleano: bool() True/False, valor lógico

"""

# Registrar o nome do projeto.
nome_projeto = input("Digite o nome do projeto: ")

# Registrar o valor do projeto em reais.
valor_projeto = float(input("Digite o valor total do projeto: "))

# Registrar qual foi a forma de pagamento pelo projeto.
pag_projeto = input("Digite a forma de pagamento: ")

# Registrar quando ocorrerá o pagamento do projeto.
pagamento = input("Digite a data do pagamento: ")

# Exibindo na tela todos os dados e o tipo de cada um.
print(type(nome_projeto))
print(type(valor_projeto))
print(type(pag_projeto))
print(type(pagamento))