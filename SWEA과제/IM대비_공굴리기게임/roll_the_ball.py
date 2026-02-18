T = int(input())

# 상 하 좌 우 우선권이니까 델타도 그렇게 만들어야함
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 모든 칸에서 모든 이동을 다 해보고 최대 이동칸수를 답으로?
# 그럼 dfs 문제 아닌가? 

def dfs(sr,sj,max_move):
    global max_length
    if max_length < max_move:
        max_length = max_move
    minimun_val = float('inf')
    minimun_pos = None

    for d in range(4):
        nr = sr + dr[d]
        nc = sj + dc[d]
        if 0<= nr < N and 0<= nc < N :
            if arr[nr][nc] < arr[sr][sj]:
                if arr[nr][nc] < minimun_val:
                    minimun_val = arr[nr][nc]
                    minimun_pos = (nr,nc)

    if minimun_pos is not None:
        nr, nc = minimun_pos
        dfs(nr,nc,max_move+1)

for tc in range(1,T+1):
    N = int(input())

    arr = [list(map(int,input().split())) for _ in range(N)]

    max_length=0
    for i in range(N):
        for j in range(N):
            sr = i
            sc = j
            dfs(sr,sc,1)

    
    print(f'#{tc} {max_length}')
