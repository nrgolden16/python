#프로그래머스 LEVEL1 코딩테스트 연습 "[1차] 다트 게임"

def solution(dartResult):
    score_lst=[]
    dart_type=[]
    for v,i in enumerate(dartResult):
        if i in [str(i) for i in range(1,10)]:
            if i=="1" and dartResult[v+1]=="0":
                score=int(dartResult[v:v+2])
                score_lst.append(score)
            else:
                score=int(i)
                score_lst.append(score)
        elif i=="0":
            try:
                if dartResult[v-1]=="1":
                    continue
                else:
                    score_lst.append(0)
            except:
                score_lst.append(0)
        elif i in ["S","D","T"]:
            try : 
                if dartResult[v+1] in ["*","#"]:
                    dart_type.append(dartResult[v:v+2])
                else:
                    dart_type.append(i)
            except:
                dart_type.append(i)
    # print("영역:",dart_type)
    # print("처음점수:",score_lst)        
    tot_score_lst=[]
    for m,n in zip(score_lst,dart_type):
        if n.startswith("S"):
            tot_score_lst.append(m**1)
        elif n.startswith("D"):
            tot_score_lst.append(m**2)
        elif n.startswith("T"):
            tot_score_lst.append(m**3)
    # print("영역 별 점수:",tot_score_lst)
    for j,k in enumerate(dart_type):
    #     print(tot_score_lst)
    #     print("index:",j,"디트 영역:",k)
        if k.find("*")!=-1:
            tot_score_lst[j]=tot_score_lst[j]*2
            if j==0:
                continue
            else:
                tot_score_lst[j-1]=tot_score_lst[j-1]*2
        if k.find("#")!=-1:
            tot_score_lst[j]=(tot_score_lst[j]*(-1))
    #     print(tot_score_lst)
    # print("최종점수:",tot_score_lst)            
    answer=sum(tot_score_lst)
    return answer
