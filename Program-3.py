x = int(input("enter X  "))
for a in range(1,x+1):
    a=a-1 if a%2==0 else a
    for i in range (a):
        
        print (2*i+1 , end="" if i==a-1 else ",")
        
    print("")
