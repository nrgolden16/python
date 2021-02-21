#프로그래머스 LEVEL1 코딩테스트 연습 "하샤드 수"

def solution(x):
    sum_t=0
    num_s=str(x)
    for i in num_s:
        sum=int(i)
        sum_t=sum+sum_t

    if x%sum_t==0:
        answer =True
    else:
        answer =False
    return answer
solution(10)
solution(12)
solution(11)
solution(13)
