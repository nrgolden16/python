#프로그래머스 LEVEL1 코딩테스트 연습 "수박수박수박수박수박수?"

def solution(n):
    answer = '수박'*(n//2)+'수박'[:n%2]
    return answer

solution(3)
solution(4)
