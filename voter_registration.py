#Voter Registration App

# Welcome message
print('Welcome to my Voter Registration App')

# Prompt for user's name
voter_name = input("Please enter your name: ")

# Prompt for user's age, loop until valid integer received
while True:
    try:
        voter_age = int(input("What is your age: "))
        break
    except ValueError:
        print("Please enter a valid age (number).")


#Initialize party_list variable
valid_parties = ["Republican", "Democratic", "Independent", "Libertarian", "Green"]

# Eligibility check, print parties if old enough, else exit
while True:
    if voter_age >= 18:
        print(f"Congratulations {voter_name.title()}! You are old enough to register vote.")
        print("\nHere is a list of political parties to join")
        for party in valid_parties:
            print("\n\t- " + party)
        break
    else:
        print(f"Sorry {voter_name} you can't vote yet!")
        exit()


# Prompt for party choice, validate against list
while True:
    party_choice = input(str("What party would you like to Join? "))
    if party_choice.title() in valid_parties:
        break
    else:
        print("Please type a valid party name: (Republican, Democratic, Independent, Libertarian, Green) ")
        continue

     
# Output registration and party-specific message
if party_choice.title() in ["Democratic", "Republican"]:
    print(f"Congratulations {voter_name.title()} you have joined the {party_choice.title()} party!")
    print("That is a major party")
elif party_choice.title() == "Independent":
    print(f"Congratulations {voter_name.title()} you have joined the {party_choice.title()} party!")
    print("You are an independent person!")
else:
    print(f"The {party_choice} party is not a major party")

print("\nThank you for testing my app!")
print(r"""
      _________________________
     |                         |
     |    OFFICIAL BALLOT      |
     |-------------------------|
     |  [ ] Republican         |
     |  [ ] Democratic         |
     |  [ ] Independent        |
     |  [ ] Libertarian        |
     |  [ ] Green              |
     |_________________________|
     |  [X] Thank you for      |
     |       voting!           |
     |_________________________|
""")


