T = int(input())

for tc in range(1,T+1):
    N,K = map(int,input().split())

    levels = list(map(int,input().split()))
    
    
    team = 0 
    max_lst = [0] * N
    for j in range(N):
        team = 0 
        for i in range(N):
            if abs(levels[j] - levels[i]) < K :
                team += 1
        max_lst[j] = team  
    
    max_team = max(max_lst)

    print(f'#{tc} {max_team}')