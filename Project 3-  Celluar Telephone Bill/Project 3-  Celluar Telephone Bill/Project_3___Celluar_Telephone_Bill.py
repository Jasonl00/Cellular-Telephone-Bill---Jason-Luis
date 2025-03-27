#Jason Luis 
#Profressor Ghaforyfard 
#March 10, 2024
#You will write a program that calculates and prints the bill for a cellular telephone company. 

#Variables 

answer = "R" 

answer_2 = "P"

answer_3 = "YES" 

answer_4 = "NO"

#Inputs  

while True: 

    try:
        account_num = int(input("\nPlease enter your account number: "))
        while account_num < 0:
            print("\nNegative value is not accepted.")
            account_num = int(input("\nPlease enter your account number: "))
        break
    except:
        print("\nInvalid Entry.... Please try again.")

service_code = input("\nWhat type of service do you have? Please enter "'R'" for Regular or "'P'" for Premium: ").upper() 
if service_code == "R" or "P":
    print("")
else:
    print("Invalid Input")

# Regular Service

if service_code == "R":
    print(service_code, "- Regular Service")
else:
    print(service_code, "- Premium Service") 

if service_code == "R":
    
    minutes = float(input("\nHow many minutes was the service used for?: "))

    if minutes < 0:
        print("\nNegative value is not accepted.")
        minutes = float(input("\nHow many minutes was the service used for?: "))
        
    elif minutes <= 50: 
        regular_service = 10.00
        print("\n$", regular_service)
    
    else:
        service_fee = minutes * 0.20
        regular_service = float(10.00 + service_fee)
        print("\n$",regular_service) 

        print("\n=================================================================")

        print("\nAccount Number:",account_num, "\n\nType of Service:", service_code,"- Regular Service", "\n\nNumber of Minutes used:", minutes, "minutes", "\n\nTotal Amount due:$", regular_service,"\n\n")

        print("\n=================================================================")
else: 
    time = input("\nAre the calls made during 6am - 6pm? Enter YES/NO: ").upper()

    if time == "YES":
      minutes = float(input("\nHow many minutes was the service used for?: "))

      if minutes < 0:
         print("\nNegative value is not accepted.")
         minutes = float(input("\nHow many minutes was the service used for?: "))
        
      if minutes <= 75: 
         premium_service = 25.00
         print("\n$", premium_service)
         

      elif minutes > 75:
          service_fee = minutes * 0.10
          regular_service = float(25.00 + service_fee)
          print("\n$",regular_service) 

      else:
          service_fee = minutes * 0.05
          regular_service = float(25.00 + service_fee)
          print("\n$",regular_service)


          print("\n=================================================================")

          print("\nAccount Number:",account_num, "\n\nType of Service:", service_code,"- Regular Service", "\n\nNumber of Minutes used:", minutes, "minutes", "\n\nTotal Amount due:$", regular_service,"\n\n")

          print("\n=================================================================")

#Continuing with the program
while True:
    try: 
        answer_3 = input("\nWould you like to continue with the sevice? Please enter YES / NO: ").upper()

        if answer_3 != "YES":
            print("\nInvalid Input... Please try again.")
            answer_3 = input("\nWould you like to continue with the sevice? Please enter YES / NO: ").upper()
        
        if answer_3 == "YES":
            print("\nThank you for continuing with our services. Have A Nice Day!\n")
            break
        else: 
            print("\nInvalid Input... Please try again.")
            answer_3 = input("\nWould you like to continue with the sevice? Please enter YES / NO: ").upper()

        if answer_4 != "NO":
            print("\nInvalid Input... Please try again.\n")

        if answer_4 == "NO": 
            print("\nSorry to see you leave. Hopefully we will see you back in the future.\n")
            break
        else:
            print("\nInvalid Input... Please try again.\n")
    except:
        print("\nPlease enter a valid input.")
    print("\n")


    
