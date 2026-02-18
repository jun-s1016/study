T = int(input())

for tc in range(1,T+1):
    # N : 떨어트릴 구슬의 갯수 , W,H : W x H 배열의 벽돌
    N,W,H = map(int,input().split)

    bricks = [list(map(int,input().split())) for _ in range(H)]

    # 1. 구슬을 떨어트리는 로직
    
    # 2. 벽돌의 숫자만큼 가로세로 배열이 0이되고, 추락하는 로직.

    # 3. 남은 벽돌의 수를 더하는 로직.