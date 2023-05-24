age = int(input("Enter your age: "))


if age < 13:
    print("You are child")

elif age >= 13 and age <18:
    print("You are teenager") 
    
elif age >18 and age <65: 
    print("You are adult")

elif age >= 65:     
    print("You are elder age")