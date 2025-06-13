while True :
    try:
        value = float(input("Qual o valor da compra do cliente? "))
        if value < 0:
            print("O valor não pode ser negativo!")
        else:
            break
    except ValueError:
        print("Valor inválido! Digite um número válido.")


print(f"A comissão de R${value:.2f} é : R${value * .10:.2f}" )