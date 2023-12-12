# ATM Project by Python:
lo = int(input("1. Login or 2. Create Account: "))
# if user select 2
if lo == 2:
    #Create a account
    name = input("Enter Your name: ")
    age = int(input("Enter Your age: "))
    nid = int(input("Enter Your NID Number: "))
    username = input("Enter Your Username: ")
    pasw = int(input("Set your 4 Digit pin: "))
    print("Your account has been successfully created!\n Thanks for trusting us!")

# if user select 1  
else:
    pin = int(input("Enter Your Pin: "))
    print("1. Check Balance \n2. Withdraw Money \n3. Change Pin \n4. Log Out")
    ent = int(input("Enter: "))
    if ent == 1:
        print("Your current balance is $1000")
    elif ent == 2:
        pin1 = int(input("Amount: "))
        print("Please Collect your money and check")
    elif ent == 3:
        prepin = int(input("Enter Your Present Pin: "))
        if prepin == pin:
            newpin = int(input("Enter your new pin: "))
            print("Your pin is updated!!")
        else: 
            pass
    else:
        print("Thanks your time!!")    
        
        # Today - 12/12/2023 "End Here, Other Work next day..."
