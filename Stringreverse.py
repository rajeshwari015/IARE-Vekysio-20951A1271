import time
start=time.time()
s=input()
o=reversed(s)
l=[]
for i in o:
    l.append(i)
print(*l)
end=time.time()
seconds=end-start
print(seconds)