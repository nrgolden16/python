#프로그래머스 LEVEL1 코딩테스트 연습 "최대공약수와 최소공배수"

def solution(n, m):
    n_lst=[i for i in range(1,n+1) if n%i==0]
    m_lst=[v for v in range(1,m+1) if m%v==0]
    n_set,m_set=set(n_lst),set(m_lst)
    GCD=max(list((n_set & m_set)))
    LCM=(n*m)/GCD
    return [GCD,LCM]
