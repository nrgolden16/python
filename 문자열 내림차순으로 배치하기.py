#프로그래머스 LEVEL1 코딩테스트 연습 "문자열 내림차순으로 배치하기"

def solution(s):
    lst=list(s)
    lst.sort(reverse=True)
    ans="".join(lst)
    return ans
