while True:
    choice = input("Digite o nome de mês: ").lower()

    match choice:
        case "janeiro":
            print("Mês: 1")
            break
        case "fevereiro":
            print("Mês: 2")
            break
        case "marco" | "março":
            print("Mês: 3")
            break
        case "abril":
            print("Mês: 4")
            break
        case "maio":
            print("Mês: 5")
            break
        case "junho":
            print("Mês: 6")
            break
        case "julho":
            print("Mês: 7")
            break
        case "agosto":
            print("Mês: 8")
            break
        case "setembro":
            print("Mês: 9")
            break
        case "outubro":
            print("Mês: 10")
            break
        case "novembro":
            print("Mês: 11")
            break
        case "dezembro":
            print("Mês: 12")
            break
        case _:
            print("Inválido, tente novamente.")