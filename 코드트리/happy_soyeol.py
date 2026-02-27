n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

ans = 0
def check(arr):
    global ans
    for i in range(n-m+1):
        stack = 0
        for j in range(m):
            if arr[i] == arr[i+j]:
                stack += 1
        if stack == m:
            ans += 1
            break

for i in range(n):
    arr = grid[i]
    check(arr)

for j in range(n):
    arr = [grid[i][j] for i in range(n)] 
    check(arr)

print(ans)