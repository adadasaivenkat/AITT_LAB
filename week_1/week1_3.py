def Reverse(l):
    print(f"Reverse of the list is {l[::-1]}.")
    
l=list(map(int,input("Enter the list : ").split()))
Reverse(l)