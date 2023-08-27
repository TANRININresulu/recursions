def fib(n):
    if 0 == n:
        return 0
    if 1 == n:
        return 1

    return fib(n-1) + fib(n-2)

def fibS(n):
    i = 1
    while(i < n):
        print(str(fib(i)) + " ")
        i += 1

fibS(19)