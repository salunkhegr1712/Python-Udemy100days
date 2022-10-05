l=[64, 25, 12, 22, 11]

# in the insertion sort in this case and we find smallest number and bring them to the front 
t=0
for i in range(len(l)):
    min1=l[i]
    print(min1)
    for j in range(i,len(l)):
        if l[j] < min1:
            t=min1
            min1=l[j]
            l[j]=t
    
        l[i]=min1

print(l)

# in each of the iteration we find smallest value and push them to end 