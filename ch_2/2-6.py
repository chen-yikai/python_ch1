# %% Before execute
import matplotlib.pyplot as plt # 匯入繪圖模組

font = {"family": "DFKai-SB"} # 設定中文字型
plt.rc("font", **font) # 全域套用字型設定
# %% chart demo
listX = [2015, 2016, 2019, 2023]
listY = [50000, 10000, 20000, 100000]
# 繪製listX與listY的折線圖，設定顏色、線寬、線型、標籤、標記形狀及大小
plt.plot(listX, listY, color="r", lw=4, ls="--", label="銷售業績", marker="s", ms=6)
plt.legend() # 顯示圖例
plt.show() # 顯示圖表

# %% chart demo
listX = [2014, 2017, 2019]
listY = [0, 50000, 100000]

# 繪製listX與listY的折線圖，設定顏色、線寬、線型、標籤、標記形狀及大小
plt.plot(listX, listY, color="b", lw=2, ls="-.", label="歷年銷售量", marker="*", ms=8)
plt.legend() # 顯示圖例
plt.show() # 顯示圖表
#%%  iphones chart
x=[2017,2018,2019,2020,2021,2022] # X軸資料
y=[43000,25000,70000,68000,85000,23000] #Y軸資料
# 繪製listX與listY的折線圖，設定顏色、線寬、線型、標籤、標記形狀及大小
plt.plot(x, y, color="c", lw=2, ls="--", label="iPhone歷年銷售量", marker="*", ms=13)
plt.xlim(2016,2023) # x軸最大、最小值
plt.ylim(0,100000) # y軸最大、最小值
plt.grid(True) # 顯示格線
plt.title("手機歷年銷售量") # 圖表標題
plt.xlabel("年度") # x軸標題
plt.ylabel("銷售量") # y軸標題
plt.legend()
#%% 折線圖
year=[2017,2018,2019,2020,2021,2022] # X軸資料
iPhone=[43000,31000,70500,68000,85000,24000]
asus=[23000,36000,40500,58000,65000,44000]
mi=[13000,26000,50500,68000,75000,54000]
lines=[[iPhone,"IPhone",'b','o','-'],[asus,"ASUS",'r','*','-.'],[mi,"小米",'g','s','-']]
# 繪製listX與listY的折線圖，設定顏色、線寬、線型、標籤、標記形狀及大小
for item in lines:
    plt.plot(year, item[0], color=item[2], lw=2, ls=item[4], label=item[1], marker=item[3], ms=10)
plt.xlim(2016,2023) 
plt.ylim(0,100000) 
plt.grid(True) 
plt.title("手機歷年銷售量") 
plt.xlabel("年度") 
plt.ylabel("銷售量") 
plt.legend()
#%% 長條圖
year=[2017,2018,2019,2020,2021,2022]
data=[43000,31000,70500,68000,85000,24000]
plt.bar(year,data,width=0.5,color='g',label='iPhone歷年銷售量')
plt.ylim(0,100000)
plt.xlim(2016,2023)
plt.title("手機歷年銷售量")
plt.xlabel("年度")
plt.ylabel("銷售量")
plt.grid(True)
plt.legend()
#%% 折線轉長條圖
year=[2017,2018,2019,2020,2021,2022] # X軸資料
iPhone=[43000,31000,70500,68000,85000,24000]
asus=[23000,36000,40500,58000,65000,44000]
mi=[13000,26000,50500,68000,75000,54000]
# 繪製listX與listY的折線圖，設定顏色、線寬、線型、標籤、標記形狀及大小
plt.bar(year,iPhone,label="IPhone")
plt.bar(year,asus,label="ASUS",bottom=iPhone)
mi_bottom=[]
for i in range(6): # 計算小米長條圖的底部位置
    mi_bottom.append(iPhone[i]+asus[i])
plt.bar(year,mi,label="小米",bottom=mi_bottom)
    
plt.xlim(2016,2023) 
plt.ylim(0,300000)
plt.grid(True) 
plt.title("手機歷年銷售量") 
plt.xlabel("年度") 
plt.ylabel("銷售量") 
plt.legend()
#%% 圓餅圖
listPrecent=[15.5,18,34.5,7,25]
listBooks=['七龍珠','火影人者','航海王','第一神拳','多啦A夢']
listColor=['red','green','pink','purple','yellow']
listExplode=(0,0,0.2,0,0.1)
# 繪製圓餅圖 (標籤，顏色，突起部分，標籤距圓心距離，百分比顯示，百分比距圓心距離，起始角度，陰影)
plt.pie(listPrecent,labels=listBooks,colors=listColor,explode=listExplode,labeldistance=1.1,autopct='%3.1f%%',pctdistance=0.8,startangle=180,shadow=True)
plt.axis("equal") # 使圓餅圖為正圓形
plt.legend(loc="center left") # 自訂圖例位置