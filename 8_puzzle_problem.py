state = [1, 2, 3, 4, 5, 6 ,7, 8, 0]
target = [1, 2, 3, 4, 5, 6, 7, 0, 8]

def misp(s,t):
    m=0
    for i in s:
        if s[i]!=0 and s[i]!=t[i]:
            m=m+1
    
    return m,s

m=misp(state,target)

def up(i):
    return i-3

def down(i):
    return i+3 

def right(i):
    return i+1
    
def left(i):
    return i-1

def move(s,t):
    i=int(s.index(0))
    print(i)
    if i==0:
        o1=o2=s
        o1[i],o1[down(i)]=o1[down(i)],o1[i]
        o2[i],o2[right(i)]=o2[right(i)],o2[i]
        
    elif i==1:
        o1=o2=o3=s
        o1[i],o1[down(i)]=o1[down(i)],o1[i]
        o2[i],o2[right(i)]=o2[right(i)],o2[i]
        o3[i],o3[left(i)]=o3[left(i)],o3[i]

    elif i==2:
        o1=o2=o3=s
        o1[i],o1[down(i)]=o1[down(i)],o1[i]
        o2[i],o2[left(i)]=o2[left(i)],o2[i]
    
    elif i==3:
        o1=o2=o3=s
        o1[i],o1[down(i)]=o1[down(i)],o1[i]
        o2[i],o2[right(i)]=o2[right(i)],o2[i]
        o3[i],o3[up(i)]=o3[up(i)],o3[i]
    
    elif i==4:
        o1=o2=o3=o4=s
        o1[i],o1[down(i)]=o1[down(i)],o1[i]
        o2[i],o2[right(i)]=o2[right(i)],o2[i]
        o3[i],o3[left(i)]=o3[left(i)],o3[i]
        o4[i],o4[up(i)]=o4[up(i)],o4[i]
    
    elif i==5:
        o1=o2=o3=s
        o1[i],o1[down(i)]=o1[down(i)],o1[i]
        o2[i],o2[up(i)]=o2[up(i)],o2[i]
        o3[i],o3[left(i)]=o3[left(i)],o3[i]

    elif i==6:
        o1=o2=s
        o1[i],o1[up(i)]=o1[up(i)],o1[i]
        o2[i],o2[right(i)]=o2[right(i)],o2[i]
    
    elif i==7:
        o1=o2=o3=s
        o1[i],o1[up(i)]=o1[up(i)],o1[i]
        o2[i],o2[right(i)]=o2[right(i)],o2[i]
        o3[i],o3[left(i)]=o3[left(i)],o3[i]
        print(o1,o2,o3)
    
    elif i==8:
        o1=o2=s
        o1[i],o1[up(i)]=o1[up(i)],o1[i]
        o2[i],o2[left(i)]=o2[left(i)],o2[i]

    if i==0 and i==2 and i==6 and i==8:
        a,b=misp(o1,t)
        p,q=misp(o2,t)

        if a<=p:
            move(b,t)
        else:
            move(q,t)

    if i==1 and i==3 and i==5 and i==7:
        a,b=misp(o1,t)
        c,d=misp(o2,t)
        e,f=misp(o3,t)

        if a<=c and a<=e:
            move(b,t)
        else:
            move(q,t)

    print(state)
    
move(state,target)
