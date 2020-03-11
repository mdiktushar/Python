n = int(input("Enter the number of elements: "))
lis = list(map(int,input().strip().split()))[:n]

sum = 0
for i in range(0,n):
    sum += lis[i]

print(sum)