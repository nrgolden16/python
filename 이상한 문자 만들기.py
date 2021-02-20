#프로그래머스 LEVEL1 코딩테스트 연습 "이상한 문자 만들기"

def solution(s):
    index=0
    tran_s=""
    for i in s:
        if i!=" ":
            if index%2==0:
                tran_s+=i.upper()
                index+=1
            elif index%2!=0:
                tran_s+=i.lower()
                index+=1
        elif i==" ":
            index=0
            tran_s+=" "
    return tran_s
