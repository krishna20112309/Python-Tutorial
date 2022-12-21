l=[1,2,3,[4,5,6]]
print(l[3][2])

#mixing list
l=[2,3,"hello",5.2,[10,19]]
print(len(l))
print(l[2])
print(l[4])


#list slicing
print(l[0:3])
print(l[0::2])
print(l[-1::-2])


s=[10,2,9,1,6,85]
t=len(s)
for n in range(t):
    print(s[-n-1])

d=[10,25,98,2,5,4,6,4,78,4]
for a in d:
    print(a)
    
    
# List comprehension
l=[]
for a in range(1,11):
    
    if a%2==0:
        l.append(a)

print(l)        

n=[m for m in range(1,11) if m%2==0]
print(n)



l1=[20,245,2,8,71,11]
print(l1)
#del l1[1]
#l1.pop(2)
# print(l1.remove(71))
# print(l1)
# l1.clear()
# print(l1)

l1[1]=90
l1.insert(1, 58)
n=[25,256]
l1.extend(n)
print(l1)


print("Krishna Kumar")

