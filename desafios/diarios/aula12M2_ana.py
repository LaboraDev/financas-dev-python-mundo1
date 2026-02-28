# Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

#  Aplicando a função input() para capturar os valores.
casa = float(input("Digite o valor da casa: R$"))
salario = float(input("Digite o valor do seu salário: R$"))
meses = int(input("Digite em quantos meses quer pagar a sua casa? "))
# Aplicando o calculo para o valor da prestação.
prestacao_final = casa / meses
# Aplicando o calculo para verificar se a prestação está abaixo dos 30% do salário.
prestacao_limite = salario * 30/100
# Aplicando condição para saber se o empréstimo será ou não liberado.
if prestacao_final <= prestacao_limite:
  print("Você está apto para financiar a sua casa própria!")
else:
  print("Empréstimo negado!")  

# Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer
#  e peça para o usuário escolher qual será a base de conversão:
#  1 para binário, 2 para octal e 3 para hexadecimal.  

# Aplicando a função input() para capturar o valor.
num = int(input("Digite um número inteiro qualquer: "))
print(''' Escolha uma base para converter o número que você digitou: 
      [1] Binário
      [2] Hexadecimal
      [3] Octal
 ''')
escolha = int(input("Digite a sua escolha: "))
if escolha == 1:
  print("Você converteu o número digitado para binário:", bin(num))
elif escolha == 2:
  print("Você converteu o número digitado para hexadecimal:",hex(num))  
elif escolha ==3:
  print("Você converteu o número digitado para octal:", oct(num))
else:
  print("Escolha inválida, tente novamente!")    

# Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#– O primeiro valor é maior
#– O segundo valor é maior
#– Não existe valor maior, os dois são iguais

# Usando a função input() para capturar o valor e int() para designar que será um número inteiro.
num = int(input("Digite um número inteiro qualquer: "))
num2 = int(input("Digite outro número inteiro qualquer: "))

# Aplicando condição para resolver a questão.
if num > num2:
  print(f"O primeiro número que você digitou: {num} é maior!")
if num < num2:
  print(f"O segundo número que você digitou: {num2} é maior!")
if num == num2:
  print(f"Os dois números digitados são iguais!")    
  
# Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
#  se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.  

# Utilizando a função input () e int() para capturar o valor digitado.
ano = int(input("Digite o ano em que você nasceu: "))
idade = 2026 - ano

# Aplicando condição para saber se está no tempo do alistamento militar.
if idade == 18:
  print("Está na hora de se alistar ao serviço militar!")
if idade > 18:
  alistamento = idade - 18
  print(f"Já passou {alistamento} anos de se alistar ao servilo militar.")
  data = 2026 - alistamento
  print(f"Você deveria ter se alistado no ano: {data} ")
if idade < 18:
  alistamento = 18 - idade
  print(f"Ainda faltam {alistamento} de se alistar no serviço militar!")
  data = 2026 + alistamento
  print(f"Você deverá se alistar no ano: {data}")

#  Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, 
# mostrando uma mensagem no final, de acordo com a média atingida: 
# – Média abaixo de 5.0: REPROVADO
#– Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO

# Utilizando a função input() para capturar as notas.
nota1 = float(input("Digite a sua primeira nota: "))
nota2 = float (input("Digite a sua segunda nota: "))
media = (nota1 + nota2) /2
if media < 5.0:
  print("Reprovado(a)!")
if media > 5 and media < 6.9:  
  print("Você está de recuperação!")
if media >= 7.0:
  print("Você está aprovado(a)!")  
  
# Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia
#  o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER

# Importando o módulo específico date
from datetime import date
hoje = date.today().year

# Utilizando a função input() para capturar o ano de nascimento.
ano = int(input("Digite o ano em que você nasceu: "))

# Aplicando o calculo para responder a questão.
resultado = hoje - ano

# Aplicando a condição para categorizar os atletas de acordo com idade.
if resultado < 9:
  print("Sua categoria é Mírim!")
elif resultado > 9 and resultado == 14:
  print("Sua categoria é Infantil!")
elif resultado > 15 and resultado == 19:
  print("Sua categoria é Júnior!")
elif resultado > 20 and resultado == 25:
  print("Sua categoria é Senior!")
else:
  print("Sua categoria é Master!")    


# # Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas
#  e diga ao usuário se elas podem ou não formar um triângulo.
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes  

# Aplicando input()para capturar os valores.
reta1 = int(input("Digite o comprimento de uma reta: "))
reta2 = int(input("Digite outro comprimento de uma reta: "))
reta3 = int(input("Digite outro comprimento de uma reta: "))

# Condição para formar um triÂngulo: 
# um lado precisa menor do que a soma dos outros dois lados.
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
  print("O triângulo pode ser formado!")
  
# Aplicando a condição para informar o tipo de triÂngulo formado.
  if reta1 == reta2 and reta1 == reta3:
   print("Esse triângulo é EQUILÁTERO!")
  if reta1 == reta2 and reta1 != reta3:
   print("Esse triângulo formado é ISÓSCELES!")  
  if reta1 != reta2 and reta1 != reta3:
   print("Esse triângulo é ESCÁLENO!") 
else:
  print("Não é possível formar um triângulo!")   

# Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade

# Aplicando a função input() para capturar os valores.
peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metro: "))

# Aplicando o cálculo do IMC
imc = peso / (altura * altura)
# Visualizando o resultado formatado.
print(f"O seu IMC é de: " '%.1f' % imc)
print('''IMC abaixo de 18.5: Abaixo do peso
Entre 18.5 e 25: Peso ideal
Entre 25 e 30: Sobrepeso
Entre 30 e 40: Obesidade''')

# Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.
# importando módulo para o jogo
import random
# Visualizando as opções de escolha.
print("Escolha entre uma das opções abaixo para jogar: ")
print('''Pedra
Papel
Tesoura ''')
# Digitando a escolha da jogada.
escolha = str(input("Digite a sua opção para jogar! "))
# Usando a lista para armazenar os itens.
opcoes = ["pedra", "tesoura", "papel"]
# Aplicando a função choice para escolha aleatória dos itens.
computador = random.choice(opcoes)
# Aplicando a condição para jogar.
if escolha == computador:
  print("Empate")
if escolha == "pedra" and computador == "papel" or escolha == "papel" and computador == "tesoura":
  print("O computador venceu.") 
else:
  print("Você venceu! Parabéns!!!")  

# outra forma de fazer o joguinho do jokenpô
import random
opcoes = ["tesoura", "pedra", "papel"]
jogador = input("Digite entre tesoura, pedra ou papel: ")
computador = random.choice(opcoes)
print(f"O jogador escolheu: {jogador}")
print(f"O computador escolheu: {computador}")
if jogador == computador:
  print("Deu empate!!!")
elif computador == "tesoura" and jogador == "papel" or computador == "pedra" and jogador == "tesoura":
  print("O computador ganhou!")
else:
  print("Você ganhou!")    


