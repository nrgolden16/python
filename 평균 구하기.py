#프로그래머스 LEVEL1 코딩테스트 연습 "평균 구하기"

arr=[1,2,3,4]
def solution(arr):
    tot=0
    count=0
    for value in arr:
        tot=tot+value
        count=count+1
    answer=tot/count
    return answer
solution(arr)
