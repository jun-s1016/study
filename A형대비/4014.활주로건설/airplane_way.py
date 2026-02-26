T = int(input())

for tc in range(1,T+1):
    N, X = map(int,input().split())

    land = [list(map(int,input().split())) for _ in range(N)]

    success = 0 
    for i in range(N):
        built = 0 
        
        for j in range(N-X+1):
            height = land[i][j]
            final_check = land[i][j]
            # 활주로를 깔 수있는 한계에 다다랐을때 
            if j == (N-X):
                for x in range(N-X,N-1):
                    final_check += land[i][x]
     
                if final_check % height == 0:
                    success += 1
                    continue 

                
            if built == 0:
                # 현위치와 (활주로를 깔았다고 전제했을때)도착위치가 다를 때(높이차이가 1) 까지 진행
                if land[i][j] - land[i][j+X] == 1:
                    for x in range(1,X):
                        height += land[i][j+x]
                    if height % land[i][j] == 0:
                        #활주로를 깔았다면, 활주로의 끝지점에서 연산을 다시 시작해야됨.
                        #for문의 j 를 X만큼 건너뛰어야하는데
                        built += X
                        continue 
                elif land[i][j] - land[i][j+X] == 0:
                    continue
                
                else: break 

            else: built -= 1 
    
    for j in range(N):
        built = 0 
        for i in range(N-X+1):
            height = land[i][j]
            final_check = land[i][j]
            # 활주로를 깔 수있는 한계에 다다랐을때 
            if i == (N-X):
                for x in range(N-X,N-1):
                    final_check += land[x][j]
     
                if final_check % height == 0:
                    success += 1
                    continue 
            
            if built == 0:
                # 현위치와 (활주로를 깔았다고 전제했을때)도착위치가 다를 때(높이차이가 1) 까지 진행
                if land[i][j] - land[i+X][j] == 1:
                    for x in range(1,X):
                        height += land[i+x][j]
                    if height % land[i][j] == 0:
                        #활주로를 깔았다면, 활주로의 끝지점에서 연산을 다시 시작해야됨.
                        #for문의 j 를 X만큼 건너뛰어야하는데
                        built += X
                        continue 
                elif land[i][j] - land[i+X][j] == 0:
                    continue
                
                else: break 

            else: built -= 1

    print(f"#{tc} {success}")