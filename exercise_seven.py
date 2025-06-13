while True:
    try:
        value = int(input("Tamanho da pirâmide? "))
        if value < 0:
            print("O valor não pode ser negativo!")
        else:
            break
    except ValueError:
        print("Valor inválido! Digite um número válido.")

for i in range(value):
    print("*" * i)