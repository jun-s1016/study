# 활주로 건설

### 2중 for문을 2개 넣는 대신 def 사용해서 각 행, 각 열마다 연산을 하게 하였다.
### 높이차를 마주치면 +1인지 -1인지를 구분하여 뒤로돌아가 활주로를 설치할지 내 앞에다 설치할지 판단을 한다.
### 만약 다음 언덕이 높다면, 활주로가 있어야 했을 길을 지나간거기 때문에 현 위치를 포함하고,
### 만약 다음 언덕이 낮다면, 그 다음부터 활주로가 있어야 하기 때문에 현 위치를 포함하지 않는다.


```
T = int(input())

for tc in range(1,T+1):
    N, X = map(int,input().split())

    land = [list(map(int,input().split())) for _ in range(N)]

    success = 0 
```
    # 한줄씩 검사하기
    def airstrip(row):
        worked = [0] * N
        for j in range(N-1):
            check = row[j] - row[j+1]
### 이 부분에서 gpt의 도움을 받음
### 한번 설치된 곳은 다시 설치되지 않는다 => visited 처럼 사용.
### 근데 이게 코드가 돌면서 어떻게 터지고 어떻게 이해해야하는지 잘 모르겠음
```
            # 높이차가 없으면 계속 진행
            if check == 0:
                continue
            # 높이가 낮아지면 앞에 +1,+2,,,+K만큼 확인 (근데 맵 밖에 나갈수있으니까 조건 넣기)
            elif check == 1:
                for k in range(X):
                    #   나가거나     k만큼의 땅의 높이가 다르면
                    if j+k+1 >= N or row[j+1] != row[j+1+k] or worked[j+1+k]:
                        return False
                    # 여기 worked 가 어떻게해서 testcase에 영향을 주는지 모르겠음;;
                    worked[j+1+k] = 1

            # 높이가 높아지면 나 포함 -1,-2,,,-k+1만큼 확인
            elif check == -1:
                for k in range(1,X):
                    if j-k <0 or row[j] != row[j-k] or worked[j-k]:
                        return False
                    worked[j-k] = 1
            # 그 외 높이차가 1이상이라면
            else: return False
        # 모든 탈락조건을 통과하면
        return True
```
    for i in range(N):
        row = land[i]
        if airstrip(row): 
            success+=1
    for j in range(N):
        col = [land[i][j] for i in range(N)]
        if airstrip(col):
            success+=1

    print(f"#{tc} {success}")