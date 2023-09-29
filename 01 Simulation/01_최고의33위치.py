N = int(input())
dxs, dys = [1, -1, 0, 0, 1, -1, 1, -1], [0, 0, 1, -1, 1, -1, -1, 1]

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

max = 0

for i in range(N):
    for j in range(N):
        sum = arr[i][j]
        for dx, dy in zip(dxs, dys):
            nx, ny = i + dx, j + dy
            if 0 <= nx < N and 0 <= ny < N:
                sum += arr[nx][ny]
        if sum > max:
            max = sum

print(max)
        

