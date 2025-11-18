#%% 基本函式
def avg(x,y):
    return (x+y) /2

a=int(input("Enter first num: "))
b=int(input("Enter second num: "))
print(f"The average of a and b is {avg(a,b)}")
#%% 等差數列練習
import math
a1=int(input("輸入數列的首項: "))
d=int(input("輸入數列的公差: "))
n=int(input("輸入數列的項數: "))
an=a1+(n-1)*d
sn=(n*(a1+an))/2
print(f"等差數列的末項為  {an}，和為 {sn}")