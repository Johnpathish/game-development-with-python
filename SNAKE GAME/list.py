a=[1,2,3,4,5]

print(a)

for i in range(6,21,2):
    a.append(i)
print(a)

print(len(a))


for i in range(len(a)-1,0,-1):
    print(a[i])