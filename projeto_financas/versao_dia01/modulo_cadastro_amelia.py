"""
Nome do Projeto: Finanças Dev v1.0
Módulo: Cadastro 
Autor: [Nome]
Data: AAAA/MM/DD
Descrição: [O que faz e para que serve]
"""

#🚀 DESAFIO DIÁRIO DO PROJETO:
#Módulo Cadastro (Finanças Dev):

#Receber nome do job/projeto

#Receber valor bruto em reais

#Validar que o valor é do tipo float

#Exibir o tipo de dado coletado na tela

'''
Objetivo: Criar módulo básico de cadastro

Declarar variáveis com tipos primitivos
Criar estrutura básica para receber dados do usuário
Armazenar informações do primeiro job (nome, valor, tipo de pagamento, data)
'''
# Coletar nome do job/projeto
nome_job = input("Digite o nome do job/projeto: ")

# Coletar valor bruto em reais
valor_bruto = float(input("Digite o valor bruto em reais: "))

# Coletar tipo de pagamento
tipo_pagamento = input("Digite o tipo de pagamento (ex: à vista, parcelado): ")

# Coletar data do job
data_job = input("Digite a data do job (formato: AAAA/MM/DD): ")

# Exibir o tipo de dado coletado na tela
print(f"Tipo de dado do nome do job: {type(nome_job)}")
print(f"Tipo de dado do valor bruto: {type(valor_bruto)}")
print(f"Tipo de dado do tipo de pagamento: {type(tipo_pagamento)}")
print(f"Tipo de dado da data do job: {type(data_job)}")