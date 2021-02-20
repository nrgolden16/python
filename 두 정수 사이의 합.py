#프로그래머스 LEVEL1 코딩테스트 연습 "두 정수 사이의 합"

def solution(a, b):
    tot=0
    if a>b:
        for k in range(a,b-1,-1):
            tot=tot+k
    elif a<=b:
        for i in range(a,b+1):
            tot=tot+i
    return tot
