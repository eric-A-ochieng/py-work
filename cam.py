#program to calculate bonus


salary= int(input("Enter salry:"))
years = int(input("Enter year of service:"))
if years<6:
    bonus=salary*0.08
    netsalary =salary + bonus
    print("bonus",bonus)
    print("netsalary",netsalary)


elif years >=6 and years <=10:
    bonus=salary*0.01
    netsalary =salary + bonus
    print("bonus",bonus)
    print("netsalary",netsalary)


elif years >10 :
    bonus=salary*0.12
    netsalary =salary + bonus
    print("bonus",bonus)
    print("netsalary",netsalary)
    