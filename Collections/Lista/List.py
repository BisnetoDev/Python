### Lista
# É uma coleção ordenada e modificável. Permite elementos duplicados
print()

print("="*80)
print("List")
print("="*80)
Lista0 = ["Maçã", "Banana", "Pera"]
print(Lista0)

### Lista com mesmo valor e índices diferentes
Lista0 = ["Maçã", "Banana", "Pera", "Banana"]
print(Lista0)

### Lista com mesmo valor e índices diferentes
Lista0 = ["Maçã", "Banana", "Pera"]
print(Lista0)
print(len(Lista0))

### Listas com tipos de entrada diferentes
Lista0_STR = ["Maçã", "Banana", "Pera"]
Lista0_INT = [1, 11, 23, 5]
Lista0_BOOL = [True, True, False]
print(Lista0_STR)
print(Lista0_INT)
print(Lista0_BOOL)
# Lista com tipos de entrada diferentes
Lista0 = ["Abacaxi", 32, True, "Rua 23", 35.7]
print(Lista0)

### Lista nova usando o construtor "list()"
Lista0 = list(("Const0", "Const1", "Const2"))
print(Lista0)
print("="*80)


def Main():
    Lista1 = ['a', 'b', 'd', 'e', 'i', 'j', 'o']
    Lista2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    Lista3 = []

    for i in Lista1:
        if i in Lista2:
            print(i, "está na Lista2")
        else:
            print(i, "Não está na Lista2, então vamos add na Lista3")
            Lista3.append(i)

    print(f'Lista1: {Lista1}')
    print(f'Lista2: {Lista2}')
    print(f'Lista3: {Lista3}')
