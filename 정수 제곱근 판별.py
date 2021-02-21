#프로그래머스 LEVEL1 코딩테스트 연습 "프로그래머스 LEVEL1 코딩테스트 연습"

import math
def solution(n):
    x=math.sqrt(n)
    if int(x)==x:
        return (x+1)**2
    elif int(x)!=x:
        return -1
