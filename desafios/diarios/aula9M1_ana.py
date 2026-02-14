# Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
#– O nome com todas as letras maiúsculas e minúsculas.
#– Quantas letras ao todo (sem considerar espaços).
#– Quantas letras tem o primeiro nome.

# Usando a função input() para capturar os nomes com a função strip() para não contar os espaços.
nome = input("Digite o seu primeiro nome: ").strip()
nome_meio = input("Digite o nome do meio: ").strip()
sobrenome = input("Digite o seu sobrenome: ").strip()

# Unindo as variáveis para aplicar a resolução solicitada.
nome_comp = nome + nome_meio + sobrenome
# Visualizando os resultados formatados
print(f'{nome.upper()} {nome_meio.upper()} {sobrenome.upper()}')
print(f'{nome.lower()} {nome_meio.lower()} {sobrenome.lower()}')
print(f'len{nome_comp}')
print(len(nome))

#Exercício Python 23: Faça um programa que leia um número de 0 a 9999
# e mostre na tela cada um dos dígitos separados.

# Usando a função input() para capturar o valor e fazer a leitura.
num = input("Digite um número entre 0 e 9999: ")

# Adicionando 4 zeros para poder mostrar on números de forma correta na tela.
num_zero = "0000" + num

# Mostrando o resultado em milhar, centena, dezena e unidade conforme solicitado.
print(f"Analisando o número: {num}")
print("Milhar:",num_zero[-4])
print("Centena:", num_zero[-3])
print("Dezena:", num_zero[-2])
print("Unidade:", num_zero[-1])

# Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

# Usando a função input() para capturar o nome.
cidade = input("Digite o nome de uma cidade: ").upper().strip()

# Mostrando os resultados na tela.
print('SANTO' in cidade[:5])
print(f'Se o retorno for True é verdade, a cidade começa com a palavra SANTO.')

# Exercício Python 25: Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

# Usando a função input() para capturar o nome.
nome = str(input("Digite o seu nome completo: ")).upper()

# Retornando True para verdadeiro e False para falso.
print('Seu nome tem Silva?','SILVA' in nome)

# Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
#  em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

# Usando o input () para capturar a frase.
frase = str(input("Digite uma frase: ")).upper()

# Usando o método count() para trazer a resolução correta para a pergunta.
print('Quantas letras A tem na frase que você digitou?', frase.count("A"))

# Usando o método find() para capturar a posição da letra A.
print('A letra A aparece pela primeira vez na sua frase na posição', frase.find("A"))

# Usando o método rfind() para capturar a letra A da direira para a esquerda.
print('A letra A aparece pela ultima vez na sua frase na posição', frase.rfind("A"))

# Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa, 
# mostrando em seguida o primeiro e o último nome separadamente.

# Usando a função input para capturar o nome completo da pessoa.
nome = str(input("Digite o seu nome: "))
meio = str(input("Digite o seu nome do meio: "))
sobrenome = str(input("Digite o seu sobrenome: "))

# Mostrando os resultados na tela.
print(f'Esse é o seu primeiro nome: {nome}')
print(f"Esse é o seu sobrenome: {sobrenome}")






