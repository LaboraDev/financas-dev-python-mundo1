
# Exercício Python 16: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

# Importando a funcionalidade trunc da biblioteca math.
from math import trunc

# Utilizando a função input() para capturar o valor digitado.
num = float(input("Digite um número real qualquer: "))

# Aplicando a função para exibir somente a parte inteira do número.
num1 = trunc(num)

# Visualizando o reultado formatado.
print(num1)

# Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.

# importando a funcionalidade para calcular a hipotenusa.
from math import  hypot

# Usando a função input para capturar os valores.
cateto_oposto = int(input("Digite um número: "))
cateto_adjacente = int(input("digite um numero: "))

# Aplicando a função para calculo direto no python.
hipotenusa = hypot(cateto_oposto, cateto_adjacente)

# Visualizano os resultados.
print(hipotenusa)
print('%2.f' % hipotenusa)

# Outra forma de resolver
# # Aplicando a fórmula teorema de pitagora conforme documentação.
# Importando a funcionalidade necessária 
from math import sqrt

# Usando a função input para capturar os valores.
cat_opo = int(input("Digite um número: "))
cat_adj = int(input("Digite um número "))
# Aplicando a fórmula de pitagoras.
hipotenusa = sqrt(cat_opo * cat_opo + cat_adj * cat_adj)

# Visualizando os resultados formatados.
print(hipotenusa)
print('%.2f' % hipotenusa) 

# Exercício Python 18: Faça um programa que leia um ângulo qualquer
# e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

# Importando as funções necessarias para o exercício.
from math import radians, sin, cos, tan
# Utilizando a função input() para capturar o ângulo.
angulo = float(input("Digite um ângulo: "))

# Aplicando a função para converter o angulo em radianos conforme doc. python.
rad = radians(angulo)
seno = sin(rad) 
cosseno = cos(rad)
tang = tan(rad)

# Visualizando os resultado formatados.
print(f'seno = {'%.2f' % seno}')
print(f'cosseno = {'%.2f' % cosseno}')
print(f'tangente = {'%.2f' % tang}')

# Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

# Importando a função necessária para resolução.
from random import choice

# Utilizando o imput para capturar os nomes.
aluno1 = input("Digite o nome do primeiro aluno: ")
aluno2 = input("Digite o nome do segundo aluno: ")
aluno3 = input("Digite o nome do terceiro aluno: ")
aluno4 = input("Digite o nome do quarto aluno: ")

# Criando uma lista para o sorteio.
lista = [aluno1, aluno2, aluno3, aluno4]

# aplicando a função no sorteio.
sorteio = choice(lista)

# Visualizando o resultado formatado.
print(f'O aluno sorteado para apagar o quadro foi {sorteio}!')

# Exercício Python 20: O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
#  Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

# Importanto a função necessária para resolução.
import random

# Utilizando a função input para capturar os nomes.
aluno1 = input("Digite o nome do primeiro aluno: ")
aluno2 = input("Digite o nome do segundo aluno: ")
aluno3 = input("Digte o nome do terceiro aluno: ")
aluno4 = input("Digite o nome do quarto aluno: ")

# Criando uma lista para o sorteio.
lista = [aluno1, aluno2, aluno3, aluno4]

# Aplicando a função.
random.shuffle(lista)

# Visualizando o resultado formatado.
print(f'A ordem de apresentação do trabalho será: {lista}!')







