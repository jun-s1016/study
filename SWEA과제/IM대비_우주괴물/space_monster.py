T = int(input())

# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(1,T+1):
    N = int(input())

    arr = [list(map(int,input().split()))for _ in range(N)]

    # 괴물의 위치 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                sr = i
                sc = j
                continue

    safety_zone = 0 
    
    for d in range(4):
        nr = sr + dr[d]
        nc = sc + dc[d]
        while 0<= nr < N and 0<= nc < N and arr[nr][nc] != 1:
                arr[nr][nc] = 1
                nr += dr[d]
                nc += dc[d]
                
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0 :
                safety_zone +=1 

    print(f'#{tc} {safety_zone}')
    # 괴물의 위치를 찾고, 상하좌우 모두 벽 or 끝에 다다를때까지
    # 0 을 1로 만들어버리고
    # arr에서 0의 개수 = 답 