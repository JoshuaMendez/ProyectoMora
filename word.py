f= open("lista.txt","w")
L=range(2300)
m=[]
for i in L:
    m.append(i)

f.write(str(m))
f.close()
