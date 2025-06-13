while True :
    try:
        value = float(input("Digite seu salário: "))
        if value < 0:
            print("O valor não pode ser negativo!")
        else:
            break
    except ValueError:
        print("Valor inválido! Digite um número válido.")

if 1500 <= value < 1750:
    percentage = 12
elif 1750 <= value < 2000:
    percentage = 10
elif 2000 <= value < 3000:
    percentage = 7
elif value >= 3000:
    percentage = 5
else:
    percentage = 15

up = (value * (percentage/100))
print(f"Salário atual: R${value:.2f} \nPorcentagem de aumento: {percentage}% \nAumento de: R${up:.2f}\nNovo salário: R${(value + up):.2f} ")
