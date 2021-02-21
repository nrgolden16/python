#프로그래머스 LEVEL1 코딩테스트 연습 "행렬의 덧셈"

def solution(arr1, arr2):
    ans=[]
    for i in range(0,len(arr1)):
        lst=[]
        for j in range(0,len(arr1[i])):
            r1=arr1[i][j]+arr2[i][j]
            lst.append(r1)
        ans.append(lst)
    return ans
