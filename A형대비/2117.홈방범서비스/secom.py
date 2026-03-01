import sys

sys.stdin = open('sample_input (1).txt','r')

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