#프로그래머스 LEVEL1 코딩테스트 연습 "실패율"

def solution(N, stages):
    
 
    tot=len(stages)
    failure_rate=dict()
    for i in range(1,N+1):
        not_clear=stages.count(i)
        if tot==0:
            failure_rate[i]=0
        if tot !=0:
            failure=not_clear/tot
            tot=tot-not_clear
            failure_rate[i]=failure


    return  sorted(failure_rate,key=lambda k:failure_rate[k],reverse=True)
