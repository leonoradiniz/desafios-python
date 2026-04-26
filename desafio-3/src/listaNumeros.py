listaNumeros = []

listaNumeros.append(7)
listaNumeros.append(2)
listaNumeros.append(5)
listaNumeros.append(9)
listaNumeros.append(1)

print(f"Lista de números empilhada: {listaNumeros}")

ultimoNumero = listaNumeros.pop()
print(f"Elemento desempilhado: {ultimoNumero}")
print(f"Lista após desempilhar o último número: {listaNumeros}")

print(f"Tamanho da lista de números: {len(listaNumeros)}")

listaNumeros.sort()
print(f"Lista de números ordenada: {listaNumeros}")

listaNumeros.reverse()
print(f"Lista de números invertida: {listaNumeros}")