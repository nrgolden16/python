#프로그래머스 LEVEL1 코딩테스트 연습 "약수의 합"

def solution(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=i
    return count
