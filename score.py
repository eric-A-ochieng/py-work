# calculting the average score

marks1= int(input("enter marks1:"))
marks2= int(input("enter marks2:"))
marks3= int(input("enter marks3:"))

average  = ((marks1+marks2+marks3)/3)

if average  >=70 and average <=100:
    print("A")

elif average  >=60 and average <=69:
    print("B")
    

elif average  >=50 and average <=59:
    print("C")


elif average  >=40 and average <=49:
    print("D")


elif average  >=0 and average <=39:
    print("Fail")
    
    