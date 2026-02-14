# 개구리 점프
```
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

        #점프 해야 할 횟수
        jump_continue += 1 
        
        # 점프성공후 범위가 물웅덩이를 초과한다면 물웅덩이 끝부분이 정답
        if i >= N:
            answer = N 
            break 
        # 현위치부터 최대점프까지의 거리를 순회하며 탐색
        for _ in range(K):
            # 그중 나뭇잎이 존재한다면 점프해서  도착한 곳 == 1
            if leaf[i] ==1:
                jump_max[i] = 1
                # 실제로 점프한 횟수 +1 
                jump += 1 
                break
            else : i -= 1 
        
        # 점프해야할 횟수 와 실제로 점프한 횟수 비교 
        if jump_continue != jump:
            jump_max[i+K] = 1
            # 아니라면 현위치에서 점프해서 0으로 빠진곳이 정답. 근데 배열형태니까 +1 
            answer = i+K+1
            # 점프해서 도착한 곳이 물웅덩이를 초과했다면 N으로 정답처리 
            if answer >= N:
                answer = N
            break 
    print(f'#{tc} {answer}')