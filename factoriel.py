def factoriel(n):
    if n == 1:
        return 1
    return n * factoriel(n-1)

print(factoriel(5))