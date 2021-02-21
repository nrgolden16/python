#프로그래머스 LEVEL1 코딩테스트 연습 "프로그래머스 LEVEL1 코딩테스트 연습"

def solution(arr):
    if len(arr)==1:
        return [-1]
    
    if len(arr)>=1:
        n=min(arr)
        arr.remove(n)
        return arr
