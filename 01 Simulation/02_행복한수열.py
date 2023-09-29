'''N, M = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

cnt = 0

for i in  range(N):
    for j in range(N-M+1):
        if all(arr[i][i+k] == arr[i][j] for k in range(M)):
            cnt += 1
        if all(arr[j+k][i] == arr[j][i] for k in range(M)):
            cnt += 1
    
print(cnt)'''


n, m = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
seq = [0 for _ in range(n)]

def is_happy_sequence():
    # 주어진 seq가 행복한 수열인지 판단하는 함수
    consecutive_count, max_ccnt = 1, 1
    for i in range(1, n):
        if seq[i - 1] == seq[i]:
            consecutive_count += 1
        else:
            consecutive_count = 1
    return max_ccnt >= m

num_happy = 0
for i in range(n):
    seq = grid[i][:]
    if is_happy_sequence():
        num_happy += 1


# 세로로 행복한 수열의 수를 셉니다.
for j in range(n):
    # 세로로 숫자들을 모아 새로운 수열을 만듭니다.
    for i in range(n):
        seq[i] = grid[i][j]
        
    if is_happy_sequence():
        num_happy += 1

print(num_happy)
