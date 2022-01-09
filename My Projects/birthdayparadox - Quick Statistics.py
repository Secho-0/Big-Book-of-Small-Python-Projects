"""Birthday Paradox Simulation, by Al Sweigart al@inventwithpython.com
Explore the surprising probabilities of the "Birthday Paradox".
More info at https://en.wikipedia.org/wiki/Birthday_problem
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: short, math, simulation"""

import datetime as dt, random as r


def getBirthdays(numberOfBirthdays):
    """Get a list of random birthdays """
    birthdays = []
    for i in range(numberOfBirthdays):
        yearStart = dt.date(1994, 1, 1)  # Set start date
        someDays = dt.timedelta(r.randint(0, 364))  # add some days
        bday = yearStart + someDays  # now you have a birthday

        birthdays.append(bday)  # add birthday to the list

    return birthdays


def getMatch(birthdayList):
    """Get a birthday that is shared in the list"""
    matchingBirthdays = []
    if len(birthdayList) == len(set(birthdayList)):
        return None  # All birthdays Unique

    for a, birthdayA in enumerate(birthdayList):
        for b, birthdayB in enumerate(birthdayList[a + 1:]):
            if birthdayA == birthdayB:
                return birthdayA  # return the matching birthday

while True:
    print('''Birthday Paradox, by Al Sweigart al@inventwithpython.com
    
    The birthday paradox shows us that in a group of N people, the odds
    that two of them have matching birthdays is surprisingly large.
    This program does a Monte Carlo simulation (that is, repeated random
    simulations) to explore this concept.
    
    (It's not actually a paradox, it's just a surprising result.)
    ''')

    # set tuple of months
    MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

    # repeatedly ask user for proper input
    while True:
        print('How many birthdays shall i generate? (Max 365)')
        response = input("> ")
        if response.isdecimal() and (0 < int(response) <= 365):
            numBdays = int(response)
            break
    print("-"*50)

    print('Here are', numBdays, 'birthdays:')
    birthdays = getBirthdays(numBdays)
    for i, birthday in enumerate(birthdays):
        if i !=0:
            print(", ", end='')
        mName = MONTHS[birthday.month - 1]
        dateText = f'{mName} {birthday.day}'
        print(dateText, end='')
    print()
    print()

    match = getMatch(birthdays)

    print("In this simulation, ", end='')

    if match is not None:
        mName = MONTHS[birthday.month - 1]
        dateText = f'{mName} {birthday.day}'
        print("Multiple People have birthdays on, ", dateText)
    else:
        print("There are no matching birthdays")
    print()

    #Run through 100k simulations
    print("Generating a new batch of ", numBdays, "Random Birthdays 100,000 times...")
    input('Press Enter to begin')

    simMatch = 0 # how many simulations had a matching birthday in them

    for i in range(100_000):
        # progress report every 10k
        if i % 10_000 == 0:
            print(i, 'simulations run so far.')
        birthdays = getBirthdays(numBdays)

        # add to match counter
        if getMatch(birthdays) is not None:
            simMatch += 1
    print('Done Running Simulations')

    # Display Results
    probability = round((simMatch / 100_000 * 100), 2)
    print('Out of 100,000 simulations of', numBdays, 'people, there was a')
    print('matching birthday in that group', simMatch, 'times. This means')
    print('that', numBdays, 'people have a', probability, '% chance of')
    print('having a matching birthday in their group.')
    print('That\'s probably more than you would think!')
    print('\t Would you like to run another simulation? Y/N')
    user_choice = input('> ')
    if not user_choice.lower().startswith('y') or user_choice.lower().startswith('n'):
        user_choice = input("Enter a valid option\n> 80",)

    elif user_choice.lower().startswith('y'):
        continue
    elif user_choice.lower().startswith('n'):
        break

