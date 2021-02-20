#프로그래머스 LEVEL1 코딩테스트 연습 "시저 암호"

str1=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
str2=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def solution(s,n):
    pw=""
    for val in s:
        if val in str1:
            pos1=str1.index(val)+n
            if pos1>25:
                pw1=str1[pos1-26]
                pw=pw+pw1
            else:
                pw1=str1[pos1]
                pw=pw+pw1
        elif val in str2:
            pos2=str2.index(val)+n
            if pos2>25:
                pw2=str2[pos2-26]
                pw=pw+pw2
            else:
                pw2=str2[pos2]
                pw=pw+pw2
        elif val==' ':
            pw=pw+" "
    answer=pw
    print(answer)
    return answer
solution('a B z',4)
