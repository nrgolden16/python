#프로그래머스 LEVEL1 코딩테스트 연습 "자연수 뒤집어 배열로 만들기"

def solution(n):
    lst=list(str(n))
    lst.reverse()
    return [int(i) for i in lst]
