"""
# 關係運算
k=10
i='T' > 'C'
j=((7+i)==k)
m=8+(10<55)*3+(30!=89)*4

print(f"Display as str: i={i} j={j} m={m}")
print(f"Show as int: i={int(i)} j={int(j)} m={int(m)}")
"""

# 邏輯運算
a=5
b=9
i=(b==7) and (a>4)
j=(a+b==14) or (b<3)
k=not((a<=b) and (a<b) or ('A' > 'C'))
print(f"i={i} j={j} k={k}")