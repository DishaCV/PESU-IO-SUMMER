element=int(input("enter a 3 digit number:"))
e=element//100
e1=(element - e*100)//10
e2=(element - e*100 - e1*10)
print("Sum of the digis is :",e+e1+e2)
