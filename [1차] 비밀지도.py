#프로그래머스 LEVEL1 코딩테스트 연습 "[1차] 비밀지도"

def solution(n, arr1, arr2):
    arr=[arr1,arr2]
    arr1_new=[]
    arr2_new=[]
    for i in arr1:
        binary1=""
        q1=i
        while q1>0:
            q1,r1=divmod(q1,2)
            binary1+=str(r1)
        binary1="".join(reversed(binary1))
        binary1_new=binary1.zfill(n)
        arr1_new.append(binary1_new)
    for v in arr2:
        binary2=""
        q2=v
        while q2>0:
            q2,r2=divmod(q2,2)
            binary2+=str(r2)
        binary2="".join(reversed(binary2))
        binary2_new=binary2.zfill(n)
        arr2_new.append(binary2_new)
    final_lst=[]
    for j,k in zip(arr1_new,arr2_new):
        final=""
        for m,n in zip(j,k):
            if (m=="0" and n=="0"):
                final+=" "
            else:
                final+="#"
        final_lst.append(final)
    return final_lst
