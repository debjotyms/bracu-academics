para = input()
def capital(st):
    new=''
    for i in range(len(st)):
        if i==0 and 'a'<=st[i]<='z':
            new=new+chr(ord(st[i])-32)
        elif st[i]=='i' and st[i+1]==st[i-1]==' ':
            new=new+chr(ord(st[i])-32)
        elif st[i]=='i' and (st[i+1]=='.' or st[i+1]=='?' or st[i+1]=='!') and st[i-1]==' ':
            new=new+chr(ord(st[i])-32)
        elif i>2 and (st[i-2]=='.' or st[i-2]=='?' or st[i-2]=='!'):
            new=new+chr(ord(st[i])-32)
        else:
            new=new+st[i]
    return new
print(capital(para))