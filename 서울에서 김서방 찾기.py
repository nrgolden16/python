#프로그래머스 LEVEL1 코딩테스트 연습 "서울에서 김서방 찾기"

seoul=["Jane","Kim"]

def solution(seoul):
    x=seoul.index("Kim")
    answer=f"김서방은 {x}에 있다"
    return answer
    
solution(seoul)
