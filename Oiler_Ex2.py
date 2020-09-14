x=1
y=2
z=[]

z.append(x+y)
z.append(z[0]+y)
for d in range(29):
    d=d-1
    z.append(z[d+1]+z[d+2])
s=[]
sum=2
for n in z:
    if n%2==0:
        sum=sum+n

    
    
#This is a comment
print(sum)
