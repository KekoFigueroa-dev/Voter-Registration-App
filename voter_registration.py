#Voter Registration App
# Welcome and introduction
print('Welcome to my Voter Registration App')

# Get and store user's name
voter_name = input(str("Please enter your name: "))

# Get and validate user's age
while True:
    try:
        voter_age = int(input("What is your age: "))
        break
    except ValueError:
        print("Please enter a valid age (number).")

#Initialize party variable
valid_parties = ["Republican", "Democratic", "Independent", "Libertarian", "Green"]

#Voter Options and rejection msg
while True:
    if voter_age >= 18:
        print(f"Congratulations {voter_name.title()}! You are old enough to register vote.")
        print("\nHere is a list of political parties to join")
        print("\n\t- Republican")
        print("\n\t- Democrat")
        print("\n\t- Independent")
        print("\n\t- Libertarian")
        print("\n\t- Green\n")
        break
    else:
        print(f"Sorry {voter_name} you can't vote yet!")
        exit()

#party_choice input
while True:
    party_choice = input(str("What party would you like to Join? "))
    if party_choice.title() in valid_parties:
        break
    else:
        print("Please type a valid party name: (Republican, Democrat, Independent, Libertarian, Green) ")
        continue

     
#Success Join Message 

if party_choice.title() in ["Democrat", "Republican"]:
    print(f"Congratulations {voter_name.title()} you have joined the {party_choice.title()} party!")
    print("That is a major party")
else:
    print(f"The {party_choice} party is not a major party")

print("\nThank you for testing my app!")



