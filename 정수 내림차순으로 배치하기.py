#프로그래머스 LEVEL1 코딩테스트 연습 "정수 내림차순으로 배치하기"

def solution(n):
    return int("".join(sorted([i for i in str(n)],reverse=True)))
