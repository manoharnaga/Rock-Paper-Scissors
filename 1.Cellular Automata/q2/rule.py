from main import * 

def rule(cell_value: int,neighbors: "list[int]"):
    is_alive = 0
    for n in neighbors:
        if(n==1):
            is_alive+=1
    if(is_alive < 2 or is_alive > 3):
        return 0
    elif(is_alive == 3):
        return 1
    else:
        return cell_value # 2 or 3 neighbours so NO CHANGE 
    
