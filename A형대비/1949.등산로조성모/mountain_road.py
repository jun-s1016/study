import sys

sys.stdin = open('sample_input.txt','r')

T = int(input())

# 반드시 상하 좌우로 이동해야하므로 델타 사용
dr = [0,1,0,-1]
dc = [1,0,-1,0]

#dfs로 길을찾는데 어떤 변수가 들어가야할까?
# 1.현재위치(r,c), 2.공사여부 3. 현재위치의 높이 4.현재까지 길이
def dfs(r,c,used,cur_h, length):
    global ans
    if length > ans :
        ans = length
    # 상하좌우 탐색
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        # 이 문제의 경우 '벽'으로 지정된 곳이 없기 떄문에 나가는걸 방지하는 코드 생성
        # 이동 후의 위치가 맵 안이고, 이미 방문한 곳이 아니라면.
        if  0 <= nr < N and 0<= nc < N and not visited[nr][nc]:
            nh = mountain[nr][nc]

        # 어떻게 내려갈거냐? 1. 그냥내려간다. 2.공사로를 깎아서 내려간다.
            if nh < cur_h: # 다음에 내려갈 곳이 더 낮은 곳이라면.(이동조건에 충족한다면)
                visited[nr][nc] = 1 # 방문횟수 +
                # 방문 이후 다시 길찾기 시작. # 길의 거리는 +1 
                dfs(nr,nc,used,nh,length+1)
                # 돌아왔을 때 방문횟수 - 
                visited[nr][nc] = 0

    #가로막혔을떈 공사를한다.
            elif used == 0 and nh-K < cur_h:
                cut_h = cur_h - 1 
                visited[nr][nc] = 1
                dfs(nr,nc,1,cut_h,length+1)
                visited[nr][nc] = 0 

for tc in range(1,T+1):
    # N : NxN 맵 # K : 공사가능깊이
    N,K = map(int,input().split())

    mountain = [list(map(int,input().split())) for _ in range(N)]

    # N x N 맵을 순회 하면서 가장 높은 곳 찾기
    top = mountain[0][0]
    for i in range(N):
        for j in range(N):
            if mountain[i][j] > top:
                top =mountain[i][j] # 가장 높은 봉우리의 높이 
    
    starts = []
    for i in range(N):
        for j in range(N):
            if mountain[i][j] == top:
                starts.append((i,j))    # 가장 높은 봉우리 들의 위치를 starts에 등록
    

    # 방문한 등산로는 다시 못가므로 visited 생성
    visited = [[0]*N for _ in range(N)]
    # 등산로의 길이 : 0으로 시작
    ans = 0

    for sr, sc in starts:
        visited[sr][sc] = 1
        dfs(sr,sc,0,mountain[sr][sc], 1)
        visited[sr][sc] = 0
    
    print(f'#{tc} {ans}')

