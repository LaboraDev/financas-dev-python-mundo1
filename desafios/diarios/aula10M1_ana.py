# Exercício Python 28: Escreva um programa que faça o computador “pensar” 
# em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir 
# qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

# Importando a função específica randint.
 
from random import randint

# Aplicando a função randint para gerar número inteiros aleatórios de acordo com o intervalo.
numero_pensar = randint(0,5)

#A plicando a função input() para capturar o número inteiro digitado.
numero_escolhido = int(input("Tente descobrir qual o número o computador pensou entre 0 e 5? "))

# Estabelecendo a condição para saber se o usuário acertou ou errou o número escolhido pelo computador.
if numero_pensar == numero_escolhido:
    print("PARABÉNS! Você acertou o número!")
else:
    print("Ahhh! Que pena, não foi dessa vez... ")    

# Exercício Python 29: Escreva um programa que leia a velocidade de um carro.
#  Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
#  A multa vai custar R$7,00 por cada Km acima do limite.    

# Aplicando a função input() para capturar o valor.
velocidade = float(input("Digite a velocidade do seu carro: "))

# Condição para aplicar a multa ou não no motorista.
if velocidade > 80.0:
    print("Você foi multado!")
    multa = (velocidade - 80) * 7
    print(f"A multa vai custar R${'% .2f'% multa}")   
else:
    print("Você está dentro do limite da velocidade permitida.")     

# Exercício Python 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

# Aplicando a função input() para capturar o valor.
num = int(input("Digite um número: "))

# Aplicando a condição para saber se o número é par ou ímpar.
if num % 2 == 0:
    print(f"O número {num} é par!")
else:
    print(f"O número {num} é impar!")    

# Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km.
#  Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
#  e R$0,45 parta viagens mais longas.  
    
# Aplicando a função input() para capturar o valor.
viagem = float(input("Quantos km de distância tem a sua viagem? "))

# Aplicando a condição para fornecer o preço da viagem.
if viagem <= 200:
    valor = viagem * 0.5
    print("O valor da sua viagem é: R${valor}")
else:
    viagem > 201
    valor = viagem * 0.45
    print(f"O valor da viagem é: R${valor}")      

# Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

# Aplicando o input()para capturar o valor.
ano = int(input("Digite um ano qualquer para saber se é bissexto: "))

# Aplicando a condição com modulo para saber se o ano é ou não bissexto.
if ano % 4 == 0:
    print(f"Esse ano de {ano} é bissexto.")
else:
    print(f"Esse ano de {ano} não é bissexto.")        

# Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input("Digite um número inteiro qualquer: "))
n2 = int(input("Digite o segundo número inteiro qualquer: "))
n3 = int(input("Digite o terceiro número inteiro qualquer: "))

# Criando condição para descobrir o maior número.
if n1 > n2 and n1 > n3:
    print(f"O número maior é:{n1}")
if n2 > n1 and n2 > n3:
    print(f"O número maior é:{n2}") 
if n3 > n2 and n3 > n1:
    print(f"O maior número é:{n3}")

# Testando condição para descobrir o menor número.
if n1 < n2 and n1 < n3:
    print(f"O menor número é:{n1}")
if n2 < n3 and n2 < n1:
    print(f"O menor número é:{n2}")
if n3 < n1 and n3 < n2:
    print(f"O menor número é:{n3}")   

# Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%. 

# Aplicando a função input() para capturar o valor.
salario = float(input("Digite o seu salário: "))

# Aplicando condição para aumento de salário.
if salario > 1250.00:
    aumento = salario + (salario * 10/100)  
    print(f"Esse é o seu salário R${aumento} com 10% de aumento.")
if salario <= 1250.00:
    aumento15 = salario + (salario * 15/100) 
    print(f"Esse é o seu salário R${aumento15} com aumento de 15%.")  

 # Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas
 #  e diga ao usuário se elas podem ou não formar um triângulo.   

 # Aplicando a função input() para capturar os valores.
reta1 = int(input("Digite o valor da primeira reta:"))
reta2 = int(input("Digite o valor da segunda reta: "))
reta3 = int(input("Digite o valor da terceira reta "))

# Condição para o triângulo existir: Um lado precisa ser menor que a soma dos outros dois lados.
# aplicando a condição para responder a questão.
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
  print("É possível formar um triângulo!")
else:
  print("Não é possível formar um triângulo!")           
           