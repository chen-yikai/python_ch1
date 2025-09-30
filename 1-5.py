import random;

bottom=1
top=100
ans=random.randint(bottom, top)
user=0
count=1

print(ans)

while True:
    user=int(input(f"猜猜{bottom}~{top}的數字: "))
    if user < bottom or user > top: 
        print("賣鬧阿~ 請輸入符和範圍的整數!")
        continue
    elif user > ans: 
        print(f"再小一點，你總共猜了{count}次")
        top=user-1
    elif user < ans:
        print(f"再大一點，你總共猜了{count}次")
        bottom=user+1
    elif user == ans:
        print(f"恭喜猜對~ 答案是{ans} 讚!!")
        print(f"你總共猜了{count}次")
        break
    count+=1