notas = []
soma = 0
media = 0
acima_media = 0
abaixo_sete = 0

while True:
    nota = float(input("Digite uma nota: "))
    if nota == -1:
        break
    notas.append(nota)
    soma += nota

print("Quantidade de valores lidos:", len(notas))
print("Valores na ordem em que foram informados:", notas)

print("Valores na ordem inversa à que foram informados:")
for nota in reversed(notas):
    print(nota)

print("Soma dos valores:", soma)

media = soma / len(notas)
print("Média dos valores:", media)

for nota in notas:
    if nota > media:
        acima_media += 1
print("Quantidade de valores acima da média calculada:", acima_media)

for nota in notas:
    if nota < 7:
        abaixo_sete += 1
print("Quantidade de valores abaixo de sete:", abaixo_sete)

print("Programa encerrado.")