T = int(input())

for tc in range(1,T+1):
    #N: 물웅덩이길이, K: 최대 점프
    N,K = map(int,input().split())
    leaf = list(map(int,input().split()))
    
    # K 부터 현위치까지 순회해서 1을 찾아야함
    i = 0
    jump_max = [0] * (N+K)
    jump_max[0] = 1 
    jump = 0
    jump_continue = 0 
    while True:
        # 최대점프범위~ 현재 +1 위치까지 탐색
        # 초기에는 무조건 jump 
        i += K
        # 현위치~점프후까지 순회
        jump_continue += 1 
        if i >= N:
            answer = N 
            break 
        for _ in range(K):
            
            if leaf[i] ==1:
                jump_max[i] = 1
                jump += 1 
                break
            else : i -= 1 
        
        if jump_continue != jump:
            jump_max[i+K] = 1
            answer = i+K+1
            if answer >= N:
                answer = N
            break 
    print(f'#{tc} {answer}')