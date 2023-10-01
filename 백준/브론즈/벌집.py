'''N = int(input())

num = 1

for i in range(N):
    num += i*6
    if N <= num:
        print(i+1)
        break'''


N = int(input())

goal = 1 # 벌집 개수
cnt = 1

while N > goal:
    goal += 6*cnt
    cnt += 1
print(cnt)