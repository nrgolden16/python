#프로그래머스 LEVEL1 코딩테스트 연습 "예산"

def solution(d, budget):
    d.sort()
    tot=0
    lst=[]
    for i in d:
        tot+=i
        if tot>budget:
            tot=tot-i
        elif tot<=budget:
            lst.append(i)
    return len(lst)
