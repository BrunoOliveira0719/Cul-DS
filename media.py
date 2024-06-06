#colocando elementos separados
c = 1 
num = []
num_inputs = int(input("digite o número de elementos: "))
while c <= num_inputs:
  num += [int(input(f"Digite o {c}º número: "))]
  c += 1

print(num)

media = sum(num)/len(num)

print("Informaçoes: ")
print(f"A quantidade de elementos é {len(num)}")
print(f"O maior elemento é {max(num)}")
print(f"A soma dos elementos é {sum(num)}")
print(f"A média dos elementos é {media}")
