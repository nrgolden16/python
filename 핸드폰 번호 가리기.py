#프로그래머스 LEVEL1 코딩테스트 연습 "핸드폰 번호 가리기"

def solution(phone_number):
    answer=""
    for i,v in enumerate(phone_number):
        if i<(len(phone_number)-4):
            answer+="*"
        else:
            answer+=v
    return answer
