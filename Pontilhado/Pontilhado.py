# Pontilhado

def Vertical():
    
    Palavra = str(input(">> Digite algo: "))

    for i in Palavra:
        print(i)
        print(".")

def Horizontal(Palavra):
    Palavra = ''.join([f'{Letra}.'
                       if Letra !=' '
                       else Letra
                       for Letra in Palavra])
    return Palavra

print(Horizontal("Python"))
print(Horizontal("Olá Mundo!"))
print(Horizontal(">> Hello World"))
