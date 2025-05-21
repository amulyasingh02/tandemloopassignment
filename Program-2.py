x = int(input("enter X  "))
for a in range(1,x+1):
    for i in range (a):
        print (2*i+1 , end="" if i==a-1 else ",")
        
    print("")
