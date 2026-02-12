# 5일차 배열 최소 합 

---------------------
#### for문에서 재귀가 도는 방법

j 를 순회하는 화살표가 j 열을 마주치면 1 이되고, 지나치는 순간 0 이 된다.
---------------------
```
T = int(input())

def dfs(row,selected,total):
    global min_value
    # 가지치기
    if total >= min_value:
        return
    # 종료 조건
    if row == N: # 마지막 행에 다다르면 종료
        min_value=min(min_value, total)
        return
    for j in range(N): # 행 순회
        # 아직 j열을 선택하지 않았다면
        if not selected[j]:
            selected[j] = 1
            dfs(row+1,selected,total+arr[row][j])
            selected[j] = 0
```
``` 
1차 DFS 에서 0,0 을 기준. 
row0 에서 j 출발. j = 0 에서 dfs(1,0). 이 끝난 후 j = 1,2 돌아야함
row1 에서 j 출발. j = 1 에서 dfs(2,1). 이 끝난 후 j = 2 돌아야함
row2 에서 j 출발. j = 2 에서 dfs(3,2). 여기서 dfs 종료조건 마주침. 이떄 , sel[2] = 0
####### 어디로 return ?? -> row 1에서 발사한 j 로 돌아감. j = 2 
```
```
for tc in range(1,T+1):
    # 무한대의 숫자를 min_value 에 넣음으로써 안정성 올리기.
    min_value = float('inf')
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    selected = [0] * N
    # 만든 arr로 순열을 만들어야함.
    # 근데 서로 j 가 겹치지 않게 만들어야함.

    dfs(0, selected, 0)
    print(f'#{tc} {min_value}')
