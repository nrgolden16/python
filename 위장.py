#프로그래머스 LEVEL2 코딩테스트 연습 "위장"

def solution(clothes):
    clothes_type_lst=[]
    for i,v in clothes:
        clothes_type_lst.append(v)
        clothes_type_set=set(clothes_type_lst)
    clothes_cnt=[]
    for j in clothes_type_set:
        clothes_cnt.append(clothes_type_lst.count(j)+1)
    def multi(lst):
        tot=1
        for i in lst:
            tot*=i
        return tot
    return multi(clothes_cnt)-1
