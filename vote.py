#program  to check eligibility of voters


age = int(input("Enter age:"))
country = input("Enter your country:")
if age >= 18 and country in ["Kenya", "Uganda", "Tanzania"]:

    # Make sure the initial letters are in upper case as you enter your country
    print("Congratulations you are eligible  to vote")
    
else:
    print("Unfortunately, you are not eligible  to vote")