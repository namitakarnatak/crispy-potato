strArr=["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
v=set(map(int,strArr[0].split(',')))
print(v)
q=set(map(int,strArr[1].split(',')))
print(q)
c=sorted(list(v&q))
print(c)
if len(c)==0:
    print('false')
d=""""""
for i in range(len(c)):
    d+=str(c[i])
    if i<len(c)-1:
        d+=","
print(d)
