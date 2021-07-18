costs=[[10,20],[30,200],[400,50],[30,20]]
total=0
for i in range(0,len(costs)):
    city =input("Enter City A or B")
    if(city=='A'):
        total=total+costs[i][0]
    elif(city=='B'):
        total=total+costs[i][1]
        print(total)
