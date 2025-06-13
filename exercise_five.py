while True:
    try:
        male = int(input("Quantidade de homens: "))
        fem = int(input("Quantidade de mulheres: "))

        if male < 0 or fem < 0:
            print("Os valores não podem ser negativos!")
        else:
            break
    except ValueError:
        print("Valor inválido! Digite um número válido.")

amount = male + fem

print(f"Total de alunos {amount}")

while True:
    choice = int(input("Deseja visualizar em porcentagem qual opção? \n1) Homem\n2) Mulher\n3) Ambos\n"))

    match choice:
        case 1:
            print(f"Homens respresentam {((male * 100) / amount):.0f}%")
            break
        case 2:
            print(f"Mulheres respresentam {((fem * 100) / amount):.0f}%")
            break
        case 3:
            print(f"Homens : {((male * 100) / amount):.0f}%\nMulheres : {((fem * 100) / amount):.0f}%")
            break
        case _:
            print("Inválido, tente novamente.")