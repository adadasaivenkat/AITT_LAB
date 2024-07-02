def Prime(l):
    count=0
    p=[]
    for i in range(len(l)):
        for j in range(2,l[i]+1):
            if l[i]%j==0:
                count+=1
        if count==1:
            p.append(l[i])
        count=0
    print(f"Prime numbers list is {p}.")
    
l=list(map(int,input("Enter the list : ").split()))
Prime(l)