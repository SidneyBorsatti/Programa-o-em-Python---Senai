print("... Sistema de Reservas de Hotel ...")

# Listas para guardar as informações
nomes = []
idades = []
tipos = []
dias = []
totais = []

# Cliente 1
nome = input("\nDigite o nome do primeiro cliente: ")
idade = int(input("Digite a idade: "))

print("Tipos de quarto:")
print("1 - Simples (R$100 por dia)")
print("2 - Duplo (R$150 por dia)")
print("3 - Luxo (R$250 por dia)")
tipo = int(input("Escolha o tipo de quarto (1, 2 ou 3): "))

if tipo == 1:
    preco = 100
    tipo_quarto = "Simples"
elif tipo == 2:
    preco = 150
    tipo_quarto = "Duplo"
else:
    preco = 250
    tipo_quarto = "Luxo"

dia = int(input("Quantos dias de estadia: "))
total = preco * dia


nomes.append(nome)
idades.append(idade)
tipos.append(tipo_quarto)
dias.append(dia)
totais.append(total)

# Cliente 2
nome = input("\nDigite o nome do segundo cliente: ")
idade = int(input("Digite a idade: "))

print("Tipos de quarto:")
print("1 - Simples (R$100 por dia)")
print("2 - Duplo (R$150 por dia)")
print("3 - Luxo (R$250 por dia)")
tipo = int(input("Escolha o tipo de quarto (1, 2 ou 3): "))

if tipo == 1:
    preco = 100
    tipo_quarto = "Simples"
elif tipo == 2:
    preco = 150
    tipo_quarto = "Duplo"
else:
    preco = 250
    tipo_quarto = "Luxo"

dia = int(input("Quantos dias de estadia: "))
total = preco * dia

nomes.append(nome)
idades.append(idade)
tipos.append(tipo_quarto)
dias.append(dia)
totais.append(total)

# Cliente 3
nome = input("\nDigite o nome do terceiro cliente: ")
idade = int(input("Digite a idade: "))

print("Tipos de quarto:")
print("1 - Simples (R$100 por dia)")
print("2 - Duplo (R$150 por dia)")
print("3 - Luxo (R$250 por dia)")
tipo = int(input("Escolha o tipo de quarto (1, 2 ou 3): "))

if tipo == 1:
    preco = 100
    tipo_quarto = "Simples"
elif tipo == 2:
    preco = 150
    tipo_quarto = "Duplo"
else:
    preco = 250
    tipo_quarto = "Luxo"

dia = int(input("Quantos dias de estadia: "))
total = preco * dia

nomes.append(nome)
idades.append(idade)
tipos.append(tipo_quarto)
dias.append(dia)
totais.append(total)

# Mostrar resultado
print("\n... RESUMO DAS RESERVAS ...")
print(nomes[0], "-", idades[0], "anos -", tipos[0], "-", dias[0], "dias - Total: R$", totais[0])
print(nomes[1], "-", idades[1], "anos -", tipos[1], "-", dias[1], "dias - Total: R$", totais[1])
print(nomes[2], "-", idades[2], "anos -", tipos[2], "-", dias[2], "dias - Total: R$", totais[2])
