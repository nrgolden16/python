#프로그래머스 LEVEL1 코딩테스트 연습 "문자열 다루기 기본"

def solution(s):
    if len(s) in([4,6]):
        for i in s:
            if i not in([str(k)for k in range(0,10)]):
                answer=False
                break
            else:
                answer=True
    else:
        answer=False
    return answer
