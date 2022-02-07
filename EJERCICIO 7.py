Multiplos_7 = 0
for n in range(1001):
    if n % 7 == 0 and n !=0:
        Multiplos_7 +=1
print(f"Los multiplos con un parametro son: {Multiplos_7}")

Multiplos_7 = 0
for n in range(7,80, 6):
    if n % 7 == 0 and n !=0:
        Multiplos_7 +=1
print(f"Los multiplos con 3 parametros son: {Multiplos_7}")