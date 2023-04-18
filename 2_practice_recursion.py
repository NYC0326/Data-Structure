n = int(input())
def hanoi(n, a, b, c):
    if n==1:
        print("Move %d to %d" % (a, c))
    else:
        hanoi(n-1, a, c, b)
        print("Move %d to %d" % (a, c))
        hanoi(n-1, b, a, c)

hanoi(n, 1, 2, 3)
print("Moving %d dists from the source rod to the target rod takes %d movements." % (n, 2**n-1))