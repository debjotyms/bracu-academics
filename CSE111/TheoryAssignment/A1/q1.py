tpl = []
for i in range(11):
    tpl2=[]
    tpl2.append(i)
    tpl2.append(i**2)
    tpl.append(tuple(tpl2))
tpl = tuple(tpl)
print(tpl)