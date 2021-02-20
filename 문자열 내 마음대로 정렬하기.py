#프로그래머스 LEVEL1 코딩테스트 연습 "문자열 내 마음대로 정렬하기"

def solution(strings, n):
    str_list=[]
    for str in strings:
        str_list.append((str[n],str))
#     print(str_list)
    str_sort=sorted(str_list)
#     print(str_sort)
    answer=[]
    for i,j in str_sort:
        answer.append(j)
    return answer
