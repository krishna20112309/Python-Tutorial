l=[]
while True:
    c=int(input(''' 
            1 Push Element
            2 Pop Element
            3 Front Element
            4 Last Element
            5 Display Queue
            6 Exit
            '''))
    if c==1:
        n=int(input("Enter the numbers of input"))
        for a in range(1,n+1):
            m=input("Enter the value "+str(a)+":-")
            l.append(m)
        print(l)
    
    elif c==2:
        if len(l)==0:
            print("Empty Queue")
        else:
            del l[0]
            print(m)
            print(l)
        
    elif c==3:
        if len(l)==0:
            print("Empty Queue")
        else:
            print("last Queue value",l[0])
    elif c==4:
        if len(l)==0:
            print("Empty Queue")
        else:
            print("last Queue value",l[-1])
    elif c==5:
        print("Display Queue",l)
    
    elif c==6:
        break           
    else:
        print("Invalid operations")         