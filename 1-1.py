'''
print("My python journey with TAI\n")
name="elias"
age=19
float_num=0.444
print(name)
print(age)
print(float_num)
print(f"\nmy name is {name}, i'm {age} years old")
'''

"""
# 算術運算子
length=10
print("圓計算")
print("圓半徑:",length)
print("圓面積:",length**2 * 3.14)
print("圓周長:",round(length * 2 * 3.14,2))
print("圓球體積:",round((4/3)*3.14 * length**3,2))
"""

"""
print("自動型別轉換")
b,i,f = True, 2, 3.4
print(b+i,b+f,i+f)
print(b-i,b-f,i-f)
print(b*i,b*f,i*f)
"""

"""
print("強制型別轉換")
i1=10
f1=float(i1)
num=5.544
num_int=int(num)
print(i1,f1,type(f1))
print(num,num_int,type(num_int))

numbers=123456
numbers_text=str(numbers)
print(numbers,numbers_text,type(numbers_text))
bool_value=bool(numbers)
print(bool_value)
"""

"""
print("print函式")
print("Python",2.7)
print('Japan','Taiwan','French',sep=',')
print("Hsinchu","Taipei",sep='\t\t')
print("Price",end=':')
price=90
print("hamburger",price,"dollar")
"""

"""
print("%c%s先生"%('張','無忌'))
wt,price=30,20.5
print("香蕉%d斤,共%.1f元"%(wt,wt*price))
"""

"""
print("\n混合運算")
n1=18
n2=7
n3=12.9
t=(n1%n2*21)//2.0**3.0-n2
print(t)
"""

"""
print("\n字串練習")
n1="Hello"
n2="World"
strSum=n1+n2
repeat="hi"
print(strSum)
print(repeat * 10)
"""

print("\ninput函式")
userName = input("Please enter username: ")
age = int(input("Please enter age: "))
print('\nName: %s\tage: %d'%(userName,age))