#프로그래머스 LEVEL1 코딩테스트 연습 "x만큼 간격이 있는 n개의 숫자"

def solution(x, n):
    ans=[]
    if x>0:
        ans=[i for i in range(x,x*n+1,x)]
    elif x<0:
        ans=[i for i in range(x,x*n-1,x)]
    elif x==0:
        while n>0:
            ans.append(0)
            n=n-1
    return ans
