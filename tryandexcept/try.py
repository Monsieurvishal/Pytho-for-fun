x=input("\n")
l=[]
for t in x.split(' '):
    try:
        l.append(int(t))
    except ValueError:
        pass    
print(sum(l))
