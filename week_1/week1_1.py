def avg(l):
    return print(f"The avergae is {sum(l)//len(l)}.")

l=list(map(int,input("Enter the list : ").split()))
avg(l)
