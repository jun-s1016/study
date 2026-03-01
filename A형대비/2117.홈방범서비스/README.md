# 홈 방범 서비스

##### 정말 거지발싸개 같은 문제.
##### " 손해를 보지 않고, 가장 많은 집을 서비스할 수 있는 경우 "
##### 이런 쓰레기같은 문구를 그대로 받아들여야한다. 이 회사는 회사의 존망과 상관없이 최대한의 서비스를 제공하고자하는 병123신같은 회사다. 수익이 0 이어도 고객이 많이 사용한다면 OK 인 회사다.수익을 바라보면 넌 인간이다. 넌 컴퓨터가 되어야 한다.
```
T = int(input())

for tc in range(1,T+1):
    # N : 도시크기 M : 하나의 집이 지불하는 비용
    N, M = map(int,input().split())

    town = [list(map(int,input().split()))for _ in range(N)]

    # 서비스 영역 k 는 내가 정하는것?
    # 크기 k 짜리 마름모서비스
    # k = 운영비용 , 마름모 크기
    # 마름모는 맵 밖을 나가도 된다. 그렇다해도 운영비용은 고정
    
    houses = []

    best_count = 0
    #모든 좌표에서 #모든 k의탐색을해야겠지
    for x in range(N):
        for y in range(N):
            if town[x][y] == 1:
                houses.append((x,y))
            # 집이 존재하는 좌표만 모으기 
        #일단 k 별 크기를 정하는 공식을 써야겠지?
            # 맵 별 최대 k = 2N-1
```

## 여기가 핵심 코드
```
        K_price = 0
    best_price = 0
    max_count = 0   
    for x in range(N):
        for y in range(N):  
            # 왜 2N - 2?
            for K in range(1,2*N):
                count = 0
                for (hx,hy) in houses:
                    if abs(hx-x)+abs(hy-y) < K:
                        count += 1
                K_price = K**2 + (K-1)**2
                ans = count * M - K_price
                if count > max_count and ans >= 0:
                    max_count = count

                #if best_price < ans:
                #    best_price = ans
                #    best_count = count

                # ㅅㅂ 손해를 보지 않는다,,??
                # count를 세고 마지막에 지불비용 곱하기
                # max 가 확정된 순간의 K 도 저장 
    print(f'#{tc} {max_count}')
```