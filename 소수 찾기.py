#프로그래머스 LEVEL1 코딩테스트 연습 "소수 찾기"

def solution(n):
    lst_1=list(range(3,n+1,2))
    len_f=len(lst_1)
    if n==2:
        return 1
    lst_2=[]
    while True:
        x=lst_1[0]
        if x**2 > n:
            break
        for i in lst_1:
            if x*i > n:
                break
            lst_2.append(x*i)
        lst_1.pop(0)
    return len_f-len(set(lst_2))+1
