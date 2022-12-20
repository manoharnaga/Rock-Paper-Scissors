from main import * 

def rule(cell_value: int,neighbors: "list[int]"):
    if(cell_value==1):
        return 1
    cnt = 0
    for n in neighbors:
        if(n==1 and cnt==3):
            return 1
        cnt+=1
    return 0
