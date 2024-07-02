def MinMax(l):
    max=l[0]
    min=l[0]
    for i in range(0,len(l)):
        if l[i]>max:
            max=l[i]
        elif l[i]<min:
            min=l[i]
    return print(f"Maximum and minimum values of the list {l} are {max} and {min}.")

l=list(map(int,input("Enter the list : ").split()))
MinMax(l)