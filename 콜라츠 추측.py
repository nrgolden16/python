#프로그래머스 LEVEL1 코딩테스트 연습 "콜라츠 추측"

def solution(n):
    rep=0
    while n>1:
        if n%2==0:
            n=n/2
            rep+=1
        else:
            n=(n*3)+1
            rep+=1
        if rep==500:
            rep=-1
            break
    return rep
