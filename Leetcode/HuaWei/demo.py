import sys
# 多行
data=sys.stdin.read()
lines=data.strip().split("\n")
# 
n=int(lines[0])
numbers=[int(lines[i] for i in range(1,n+1))]
result=sum(numbers)
print(result)
# 第一行
x=input()


