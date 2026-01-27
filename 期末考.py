# %% 串列應用
print("=======輸入並顯示串列值=========")
length=int(input("請輸入資料個數："))
list=[]
for i in range(length):
    index = i + 1
    list.append(int(input(f"請輸入第{index}個整數：")))
    
print("\n你輸入的串列值為：",end='')
for item in list:
    print(item,end='\t')

list_sum=sum(list)
print(f"\n此串列數值總和為：{list_sum}")

list_avg=list_sum/len(list)
print(f"此串列數值平均為：{list_avg:.2f}")

list_max=max(list)
list_min=min(list)
print(f"串列中最大值為{list_max}，最小值為{list_min}")

sorted_list=sorted(list,reverse=True)
print("此串列資料由大到小排序後為：",end='')
for item in sorted_list:
    print(item,end='\t')
# %% 費氏數列
print("\n=======計算費氏數列係數值=========")
while True:
    fibi_index=int(input("\n請問要計算費氏數列的第幾項係數值："))
    def calc_fibi(i):
        if i == 0:
            return 0
        elif i == 1:
            return 1
        else:
            return calc_fibi(i-1) + calc_fibi(i-2)
    fibi=calc_fibi(fibi_index)
    print(f"\n費氏數列第{fibi_index}項的係數值為{fibi}")
    will_continue=input("\n請問是否再次計算(Y/N)?")
    if will_continue=="y" or will_continue=="Y":
        continue
    else:
        break
# %% 期中考及格名單
print("=======集合的應用=========")
math_pass={"長山","小玉","花輪","永澤","小丸子"}
english_pass={"永澤","花輪","丸尾","野口","美環"}
print("兩科目都及格的名單為：",math_pass&english_pass)
print("有其中一科不及格的名單為：",math_pass^english_pass)
print("全部學生的名單為：",math_pass|english_pass)
# %% 檔案處理
print("=======檔案處理=========")
append_text="資訊科, 50, 王順賢\n資訊科, 51, 李漢泰"
with open("./stu.txt",'a+',encoding='big5') as file:
    file.write(append_text)
    file.seek(0)
    first_six=file.read(6)
    print(first_six)
    print(file.read())
# %% 繪製線條圖
import matplotlib.pyplot as plt
font={"family" : 'DFKai-SB'}
plt.rc('font',**font) 

ee=[500,450,430,480,490,530]
ec=[430,500,510,300,320,410]
cs=[330,400,600,550,650,580]
year=[2020,2021,2022,2023,2024,2025]

plt.plot(year, ee, color='blue',ls=':',marker='o',label='電子系',lw=2.5,ms=5)
plt.plot(year, ec, color='red',ls='-.',marker='*',label='電機系',lw=1.5,ms=10)
plt.plot(year, cs, color='green',ls='-',marker='s',label='資工系',lw=3,ms=7)

plt.title("松山科大歷年招生錄取分數")
plt.xlabel("年度")
plt.ylabel("分數")
plt.legend(loc='lower right')
plt.xlim(2019, 2026)
plt.ylim(0, 700)
plt.grid(True)
plt.show()