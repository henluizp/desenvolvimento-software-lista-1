total = 0
for i in range(10, 200):
    if i % 2 == 0:
        print(i)
        total+= 1

print(f"Total de números pares: {total}")