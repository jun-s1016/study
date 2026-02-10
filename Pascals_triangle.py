T = int(input())

for tc in range(1,T+1):
    N = int(input())

    triangle = [[0] * N for _ in range(N)]
           # 1 0 0 0 
           # 1 1 0 0
           # 1 2 1 0
           # 1 3 3 1 라고 생각하면 2 기준. 왼쪽위, 바로위.2개니까 [i-1][j-1],[i-1][j]
    for i in range(N):
        for j in range(i+1):
            # 근데 첫번째는 1이고, 대각선으로 1이 올라가므로 j=1 도 1이다.
            if i==0 or j==i :
                triangle[i][j] = 1 
            else:
                triangle[i][j] = triangle[i-1][j]+ triangle[i-1][j-1]
    

    print(f'#{tc}')
    for i in range(N):
        answer = print(*triangle[i][:i+1])
    

