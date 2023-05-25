n = int(input("Quantos elementos da sequência de Fibonacci você deseja ver?"))
n1 = 0
n2 = 1
i = 0

while i != n:
    print(n1, end=" -> ")
    n1 = n2 + n1
    i += 1
    if i == n:
        break
    print(n2, end=" -> ")
    n2 = n1 + n2
    i += 1

print("\033[35mFim\033[0m")
