T = int(input())

dr1 = [1,-1,0,0]
dc1 = [0,0,1,-1]

dr2 = [1,-1,1,-1]
dc2 = [1,-1,-1,1]

for tc in range(1,T+1):
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    dead_flies = 0
    # 우선 + 방향으로 탐색.
    for i in range(N):
        for j in range(N):
            cross = arr[i][j]
            diag = arr[i][j]
            for d in range(4):
                for m in range(1,M):
                    nr1 = i + dr1[d]*m
                    nc1 = j + dc1[d]*m

                    nr2 = i + dr2[d]*m
                    nc2 = j + dc2[d]*m

                    if 0 <= nr1 < N and 0 <= nc1 < N:
                        cross += arr[nr1][nc1]
                    
                    if 0 <= nr2 < N and 0 <= nc2 < N:
                        diag += arr[nr2][nc2]
            if dead_flies <= cross or dead_flies <= diag:
                dead_flies = max(dead_flies, cross,diag)

    print(f'#{tc} {dead_flies}')