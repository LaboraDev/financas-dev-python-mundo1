"""
Este arquivo faz parte do projeto de rever e solidificar a base na linguagem de python.
Material utilizado: Vídeos do curso em vídeo Guanabara. Mundo1 python.
Aula: 07 Operadores aritméticos.
Esta entrega é referente ao dia 03/02/2026.
Meta: Realizar em um mês cada módulo (mundo).
08/02/2026

"""
# Exercício Python 5: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.
# Capturando o dado com o input()
num = int(input("Digite um número inteiro: "))

# Aplicando o calculo para antecessor.
ante = num - 1

# Aplicando o calculo para o sucessor.
suces = num + 1
#Visualizando o resultado formatado.
print(f'Você digitou o número {num}, sendo o antecessor dele: {ante} e o sucessor: {suces}!')

# Exercício Python 6: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
# Capturando o dado com a função input()
numero = int(input("Digite um número inteiro: "))

# Aplicando o calculo para obter o dobro.
dobro = numero * 2

# Aplicando o calculo para o bter o triplo.
triplo = numero * 3

# Aplicando o calculo para obter a raiz quadrada.
raiz = numero ** (1/2)

# Visualizando o resultado formatado.
print(f'VocÊ digitou o número {numero}, sendo o dobro dele {dobro}, o triplo {triplo} e a sua raiz quadrada {raiz}!')

# Exercício Python 7: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
# Capturando o dado através da função input()
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Aplicando o calculo para a média das notas.
media = (nota1 + nota2) / 2

# Visualizando o resultado formatado.
print(f'A média das suas duas notas foi: {media}. Parabéns!!!')

# Exercício Python 8: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
# Utilizando a função input() para capturar o dado.
metro = float(input("Digite um valor em metros: "))
# Aplicando o calculo para coversão de metro em centimetro.
cm = metro * 100

# Aplicando o calculo para conversão de metro em milimetros.
mm = metro * 1000

# Visualizando o resultado formatado.
print(f'Foi digitado o valor {metro} metros, a conversão em centímetros é: {'%.0f' % cm} e em milímetros é: {'%.0f' % mm} ')

# Exercício Python 9: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.
# Utilizando a função input() para capturar o dado.
num = int(input("Digite um número inteiro: "))

# Visualizando a tabuada formatada do número digitado.
print(f'Abaixo está tabuada do número {num} que você digitou!')
print(f'{num} x 1 = {num * 1}')
print(f'{num} x 2 = {num * 2}')
print(f'{num} x 3 = {num * 3}')
print(f'{num} x 4 = {num * 4}')
print(f'{num} x 5 = {num * 5}')
print(f'{num} x 6 = {num * 6}')
print(f'{num} x 7 = {num * 7}')
print(f'{num} x 8 = {num * 8}')
print(f'{num} x 9 = {num * 9}')
print(f'{num} x 10 = {num * 10}')

# Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# dolár = R$ 3.24

# Utilizando o input() para capturar o dado e o float() para números com casas decimais.
real = float(input("Digite quanto reais você tem na sua carteira: "))

# valor do dolár para conversão no dia de hoje.
dolar = 3.24
# Aplicando o calculo para compra de dolár.
compra = real / dolar

# Visualizando o resultado formatado.
print(f'Com o dinheiro que você tem na cateira: R${real} consegue comprar em dolár: U${'%.2f' % compra}')

# Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros, 
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

# Utilizando a função input() para capturar a informação.
largura = float(input("Digite a largura da parede em metros: "))
altura = float(input("Digite a altura da parede em metros: "))

# Aplicando o calculo para área da parede.
area = largura * altura

# Aplicando o calculo para saber a quantidade de tinta usada na pintura.
litro = 2
tinta = area / litro

# Visualizando o resultado formatado.
print(f'Para pintar a área de: {area} m² você vai precisar de {tinta}L de tinta.')

# Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
# Utilizando o input() para capturar o valor.
preco = float(input("Digite o preço do produto: "))

# Aplicando o calculo para o novo preco do produto com desconto.
desconto = preco - (5/100)

# Visualizando o produto com o novo preço de maneira organizada.
print(f'O produto custa: R${preco}, seu novo preço com o desconto de 5% é: R${'%.2f' % desconto}!')

# Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
# Utilizando as funçoes float e input, para capturar o valor de um número decimal.
salario = float(input("Digite o seu salário:R$ "))

# Aplicando o calculo para aumento do salário.
aumento = salario * 0.15
total = salario + aumento
# Visualizando o novo salário.
print(f'O seu salário atual é de R${salario} e com o aumento de 15% passará para o valor de: R${'%.2f' % total}!')

# Exercício Python 14: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
# Fórmula para resolução do exercício. F = (C*9/5) + 32
# Utilizando as funções float e input para capturar o valor com casa decimal.
temp = float(input("Digite a temperatura em graus celsius: "))

# Aplicando o calculo para a conversão.
fahrenheit = (temp * 9/5) + 32

# Visualizando a temperatura convertida e formatada.
print(f'Você digitou {temp}°C covertendo para fahrenheit fica {fahrenheit}°F')

# Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias
#  pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

# Utilizando as funçoes float e input para capturar as informações necessárias.
km = float(input("Digite quantos Km você percorreu com o carro alugado: "))
dias = float(input("Digite quantos dias você ficou com o carro alugado: "))
# Aplicando o calculo para pagamento do aluguel do carro.
pag_dia = dias * 60
pag_km = km * 0.15
pag_total = pag_dia + pag_km

# Visualizando o valor a ser pago no carro alugado de forma estruturada.
print(f'Você ficou com o carro alugado por {dias} dias e rodou {km} km, devendo pagar o valor total de: R${pag_total}')






