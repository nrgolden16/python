### 프로그래머스 LEVEL1 코딩테스트 연습 "K번째수"
```
def solution(array, commands):
    answer = []
    for i,j,k in commands:
        arr_modi=array[i-1:j]
        arr_modi.sort()
        num=arr_modi[k-1]
        answer.append(num)
    return answer
```
