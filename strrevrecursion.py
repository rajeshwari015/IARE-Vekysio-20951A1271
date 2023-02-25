import time
start=time.time()
def strrev(s,i):
    if(i<0):
        return ""
    else:
        return (s[i]+strrev(s,i-1))
s=input()
print(strrev(s,len(s)-1))
end=time.time()
print(end-start)