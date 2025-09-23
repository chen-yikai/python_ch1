import random
import os

low=int(input("請輸入亂數範圍的下限: "))
high=int(input("請輸入亂數範圍的上限: "))

while True:
    ran=random.randint(low, high)
    print(f"產生的亂數為 {ran}")
    q=input("請位是否再次產生亂數?(y/n) ")
    if q == "n": break
    
os.system('cls')