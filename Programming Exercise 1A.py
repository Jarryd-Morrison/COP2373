#Defines the variables and thier starting amounts.
TICKETS = 20
BUYERS_COUNT = 0

print(f'{TICKETS} Tickets are remaining.')

#Runs the loop to check if the number of tickets is > 0, otherwise repeats the code.
while TICKETS > 0:
    TO_BUY = int(input("How many tickets would you like to buy? "))

    
    
#Checks if the number of tickets being purchased is too much for one buyer, or if their isn't enough tickets to purchase left.
    if (TO_BUY < 0 or TO_BUY > 4) or TO_BUY > TICKETS:
        print("Sorry, you can't buy that many.")

#Re prints the number of available tickets.
        print(f'{TICKETS} Tickets are remaining.')

#Checks if the number of tickets = 0, if true breaks loop, otherwise continues loop.
    elif TICKETS == 0:
        break

#preforms calcualtion of total number of tickets as well as total number of buyers if requirements are met.       
    else:
        TICKETS -= TO_BUY
        BUYERS_COUNT += 1
#Displays how many tickets are remaining after calculation.
        print(f'{TICKETS} Tickets are remaining.')


#Prints the total number of buyers.
print(f'The Total number of buyers was {BUYERS_COUNT}.')
