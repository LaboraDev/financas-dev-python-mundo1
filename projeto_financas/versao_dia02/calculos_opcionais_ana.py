"""
Nome do Projeto: Finanças Dev v1.0
Módulo: Calcúlos aritméticos
Autor: Ana Rachel Rodrigues da Costa
Data: 2026/02/08

Descrição:
- Atividade integrante do projeto para fixar o conhecimento
adquirido na aula 7 do curso em vídeo do prof. Guanabara.

Objetivo: 
- Realizar a inserção de calculos no projeto para praticar os operadores
aritméticos.
- Desenvolver a saída formatada.
- Efetuar a ordem de precedência dos operadores aritméticos no python.

Conceito:
Tabela com os operadores aritméticos.

| Operação aritmética | Símbolo |
| ------------------- | ------- |
|       Adição        |    +    |
|      Subtração      |    -    |
|    Multiplicação    |    *    |
|      Divisão        |    /    |
|   Exponenciação     |   **    |

Tabela de precedência.

|  Precedência  | Operadores |         Descrição        |
| ------------- | ---------- | ------------------------ |
|   Primeiro    |     ()     |         Parentêses       |
|    Segundo    |     **     |       Exponenciação      |
|   Terceiro    |  *  ou  /  | Multiplicação ou Divisão |
|    Quarto     |  +  ou  -  |   Adição ou Subtração    |

🫨 Dificuldade encontrada na execução do código?
Nenhuma
 
"""
# Usando a função input() para capturar o valor do projeto.
valor_projeto = float(input("Digite o valor bruto cobrado pelo projeto: "))

# Aplicamos o imposto na alíquota de 6% para todos os clientes.
imposto = valor_projeto * 0.06

# Aplicamos a taxa fixa da plataforma para todos os clientes.
taxa_site = 0.10 * valor_projeto

# O que a empresa irá receber após descontar imposto e taxa.
valor_liquido = valor_projeto - imposto - taxa_site

# Visualizando o resultado formatado do real ganho da empresa.
print(f'O valor líquido recebido é de R${'%.2f' % valor_liquido}!')