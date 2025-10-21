sum=0
for i in range(11):
    sum+=i

print(f"1~10累加的結果為:{sum}")

#%% 累加範圍
print("計算整數數列的累加值")
start=int(input("請輸入數列的初值: "))
end=int(input("請輸入數列的終值: "))
ans=0
for i in range(start,end + 1):
    ans+=i
print(f"{start}~{end}的累加結果為: {ans}")

#%% 逐行顯示字串字元
string="Python"
for i in string:
    print(i)
#%% 4~207範圍內可被7整除的數字
for i in range(4,208):
    if i%7==0:
        print(i,end=" ")
#%% 6x6 字元
for i in range(6):
    for j in range(6):
        print("A",end="")
    print("")
#%% 三角形
for i in range(6):
    for j in range(6-i):
        print("A",end="")
    print()
#%% 九九乘法表
for i in range(9):
    i +=1
    for j in range(9):
        j+=1
        print(f"{i} * {j} = {i*j}",end="\t")
    print("")
#%% 身分證字號
id=input("請輸入身分證字號: ")
for char in id:
    for i in range(9):
        if char == str(i):
            print(char,end="")
print("是你的數字部分")
#%% Password
right_password="123"
while True:
    user=input("請輸入密碼: ")
    if user == right_password:
        print("密碼正確!")
        break;
    else:
        print("密碼錯誤!")
#%% for...else
text="Python"
for char in text:
    print(char)
    #break;
else:
    print("輸出完成!")
#%% timer
import time

count=10
while count > 0:
    print(count)
    count-=1
    time.sleep(1)
print("時間到!")