n = int(input())
def hanoi(n, a, b, c):
    if n == 0: # 옮길 디스크가 없을 경우
        print("Nothing to move.")
    elif n == 1: # 옮길 디스크가 1개일 경우, 그냥 바로 옮겨주기만 하면 됨 (source -> target)
        print("Move %d to %d" % (a, c))
    else: # 그 외의 경우에는
        hanoi(n-1, a, c, b) # source rod에 있는 디스크 중 맨 밑에꺼 빼고 전부를 (source -> spare) 로 옮겨줌
        print("Move %d to %d" % (a, c)) # 그럼 source rod에 있는 맨 마지막꺼는 바로 target으로 옮겨줌
        hanoi(n-1, b, a, c) # 그럼 spare rod에 있는 것들을 다 target으로 옮겨줌
        # 어처피 재귀니까 큰 구조만 생각하고, 세세하게 생각할꺼 없음
        # 이런식으로 코드 짜면 맨처음 source rod에 있던 디스크들이 크기 순서대로 차례로 source에서 target으로 옮겨짐

hanoi(n, 1, 2, 3)
print("Moving %d dists from the source rod to the target rod takes %d movements." % (n, 2**n-1))