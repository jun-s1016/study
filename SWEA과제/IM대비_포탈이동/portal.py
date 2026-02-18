T = int(input())

for tc in range(1,T+1):
    N = int(input())
    portal = list(map(int,input().split()))

    visited = [0] * N 
    moved = 0

    j = 0
    while True:
        # 탈출 조건 ( 끝에 다다랐을때 )
        if j == N-1 : 
            break
        
        
        # 이동 후 어느 포탈로 가야하는지 판단
        # j = (visited[j]-1)

        # 이미 방문한 포탈일 시 
        if visited[j] != 0:
            j += 1 

        elif visited[j] == 0:
            visited[j] += 1 

            if portal[j] == 0 :
                j+=1
            else: 
                j = portal[j] - 1

        moved += 1

        
    print(f'#{tc} {moved}')