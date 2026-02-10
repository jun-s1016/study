T = int(input())

# 우하, 좌하, 좌상, 우상 -> 이 순서도 중요하다.
di = [1, 1, -1, -1]
dj = [1, -1, -1, 1]

def dfs(i, j, d, cnt):
    global ans, si, sj

    for nd in range(d, d+2):   # 방향은 현재 방향 이상만
        
        #우리가 고려해야할 사항
        # 1. 회전을 다 했는가?
        # 2. 이동후에 위치가 벽 밖인가?
        # 3. 이동한위치의 디저트가 이미 먹은 디저트인가? 
        # 4. 성공의 조건 이후 탈출은 어떻게?

        # 1. 아직 회전을 끝내지 않았다면 계속해라 
        if nd>= 4:
            continue 

        ni = i + di[nd]
        nj = j + dj[nd]

        # 2. 이동해도 벽 안이라면 진행시켜라
        if ni < 0 or nj < 0 or ni >= N or nj >= N:
            continue

        # 4.시작점으로 돌아온 경우 (성공)
        if ni == si and nj == sj and nd==3 : # 시작점이고, 회
            ans = max(ans, cnt)
            return

        # 이미 먹은 디저트면 못 감
        if dessert[ni][nj] in eaten:
            continue

        eaten.add(dessert[ni][nj]) 
        dfs(ni, nj, nd, cnt+1)
        eaten.remove(dessert[ni][nj])



for tc in range(1, T + 1):
    N = int(input())
    dessert = [list(map(int, input().split())) for _ in range(N)]

    ans = -1

    for i in range(N):
        for j in range(N):
            si, sj = i,j # 현위치
            eaten = {dessert[i][j]}
            dfs(i, j, 0, 1)

    print(f'#{tc} {ans}')
