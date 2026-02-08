""" 
Daily referente ao dia 03/02/2026 da aula 07 - Operadores aritméticos
Objetivo: 
- Testar cada um dos operadores ensinados no vídeo do Guanabara.
- Testar a ordem da precedencia para os calcúlos serem corretos.
- Fixar conceitos básicos de python.

Conceitos:

|     Operaçao     |  Símbolo  |
| ---------------- | --------- |
|       Adição     |     +     |
|    Subtração     |     -     |
|   Multiplicação  |     *     |
| Divisão inteira  |    //     |
|  Divisão float   |     /     |
|      Módulo      |     %     |
|  Exponenciação   |    **     |

Raiz quadrada n **(1/2)
n representa o número que eu quero obter a raiz quadrada.

🫨 Dificuldade encontrada na execução do código?
- Formatar a saída em duas casas decimais: 
print(f'O resultado é: {'%.2f' % variável}')

"""
# Adição
# Usando a função input() para capturar os números inteiros.
valor1 = int(input("Digite um número inteiro qualquer: "))
valor2 = int(input("Digite outro número inteiro: "))

# Realizando a soma dos números que foram digitados.
soma = valor1 + valor2

# Visualizando na tela o resultado da soma formatado.
print(f'A soma dos números que você digitou é: {soma}!')

# Subtração
# Usando a função input() para capturar os números inteiros.
num1 = int(input("Digite um número inteiro qualquer: "))
num2 = int(input("Digite outro número inteiro: "))

# Realizando a subtração dos números que foram digitados.
subtracao = num1 - num2

# Visualizando o resultado formatado da multiplicação.
print(f'O resultado da subtração é:{subtracao}!')

# Multiplicação
# Usando a função input() para capturar os números inteiros.
mult1 = int(input("Digite um número qualquer: "))
mult2 = int(input("Digite outro número inteiro qualquer: "))

# Realizando a multiplicação entre os números digitados.
produto = mult1 * mult2

# Visualizando o resultado formatado dos números digitados.
print(f'A multiplicação com os dois números que você digitou {mult1} x {mult2} é igual a:{produto}!')

# Divisão inteira
# Usando a função input() para capturar os números inteiros.
div_int = int(input("Digite um número inteiro qualquer: "))
div_int2 = int(input("Digite um número inteiro menor do que o primeiro: "))

# Realizando a divisão entre os números digitados.
quociente = div_int // div_int2

# Visualizando o resultado formatado da divisão inteira.
print(f'A parte inteira do resultado da divisão é: {quociente}!')

# Divisão 
# Usando a função input() para capturar os números digitados.
div1 = float(input("Digite um número inteiro: "))
div2 = float(input("Digite outro número, menor do que o primeiro: "))

# Realizando a divisão entre os números digitados.
div_quociente = div1 / div2

# Visualizando o resultado da divisão com retorno float.
print(f'O resultado da divisão é: {'%.2f' % div_quociente}!')

# Módulo
# Usando a função input() para capturar os números inteiros.
modulo = int(input("Digite um número inteiro: "))
modulo1 = int(input("Digite outro número inteiro menor do que o primeiro: "))

# Realizando a divisão entre os números digitados.
resto = modulo % modulo1

# Visualizando o resultado formatado do resto da divisão.
print(f'O resto da divisão dos números que você digitou é: {resto}!')

# Raiz quadrada
# Usando a função input() para capturar o número inteiro para a raiz quadrada.
n = int(input("Digite um número inteiro qualquer: "))

# Fórmula simples de realizar a raiz quadrada sem usar a função nativa do python.
raiz = n ** (1/2)

# Visualizando o resultado formatado da raiz quadrada.
print(f'O resultado da raiz quadrada é: {'%.2f' % raiz}!')
