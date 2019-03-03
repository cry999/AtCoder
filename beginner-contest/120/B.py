A, B, K = [int(s) for s in input().split()]

count = 0
answer = -1
for i in range(min(A, B), 0, -1):
    if A % i == 0 and B % i == 0:
        count += 1

        if count == K:
            answer = i
            break

print(answer)
