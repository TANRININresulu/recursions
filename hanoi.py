def move(f, t):
    print("From " + str(f) + " to " + str(t))

def hanoi(n, f, t, h):
    if n == 0:
        return
    hanoi(n-1, f, h, t)
    move(f, t)
    hanoi(n-1, h, t, f)

hanoi(19, "A", "C", "B")