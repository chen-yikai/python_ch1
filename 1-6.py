import random

rank=[0,0,0] #safe win lose
typeText=["剪刀","石頭","布"]
stateText=["平手","你贏了","你輸了"]
while True:
    print(f"勝負統計:你贏了{rank[1]}次，你輸了{rank[2]}次，平手{rank[0]}次")
    user=int(input("請選擇:(1)剪刀 (2)石頭 (3)布 (4)結束:"))
    npc=random.randint(1,3)
    state=0 # 0:safe 1:win 2:lose
    if user==4: break
    if npc==user: state=0
    elif user==1: 
        if npc==3: state=1 
        else: state=2
    elif user==2:
        if npc==1:state=1
        else: state=2
    elif user==3:
        if npc==2: state=1
        else: state=2
    rank[state]+=1
    print(f"電腦出了:{typeText[npc-1]}，{stateText[state]}!!\n")