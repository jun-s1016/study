T = int(input())

for tc in range(1,T+1):
    # N: 물웅덩이 길이 , K: 최대점프거리
    N,K = map(int,input().split())
    # 물웅덩이 정보 
    water_map = list(map(int,input().split()))
    # 개구리의 위치 
    frog = [0]*(N+K)
    frog[0] = 1
    
    i = 0
    # 최대 거리에 나뭇잎이 없다면
    for leaf in N:
        if frog[i+K] != 1:
            # 최대 거리까지 검색
            for j in range(K):
                # 최대 거리 안에 나뭇잎이 있다면?
                if frog[i+j] ==1:    
                    i += j
    # 이거를 순회하고 싶은데 어떻게 하지 ? 




    print(f'#{tc} {frog}')
