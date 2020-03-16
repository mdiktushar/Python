from math import *
num = int(input("Enter the number to be test: "))
flag = 0
for i in range(2,int(sqrt(num))):
    if(num % i == 0):
        flag +=1
        break
if(flag != 0):
    print(num,"is not Prime")

else:
    print(num,"is Prime")
