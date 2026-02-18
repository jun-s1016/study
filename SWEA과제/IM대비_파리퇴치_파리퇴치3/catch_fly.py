T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    dead_fly = [[0]*(N-M+1) for _ in range(N-M+1)]

    for i in range(N-M+1):
        for j in range(N-M+1):
            dead_flies = 0
            for k in range(M):
                for m in range(M):
                    dead_flies += arr[i+k][j+m]
            
            dead_fly[i][j] = dead_flies


    answer = max(map(max,dead_fly))

    print(f'#{tc} {answer}')