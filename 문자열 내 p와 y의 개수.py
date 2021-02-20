#프로그래머스 LEVEL1 코딩테스트 연습 "문자열 내 p와 y의 개수"

def solution(s):
    low=s.lower()
    p_num,y_num=low.count("p"),low.count('y')

    if p_num==y_num:
        answer=True
    elif p_num!=y_num:
        answer=False
    elif p_num==0 and y_num==0:
        answer=True
    return answer
