#Factorial
#计算1+2！+...+10!
sum, temp = 0, 1
for i in range(1,11):
    temp*=i
    sum+=temp
print("运算结果是：{}".format(sum))
