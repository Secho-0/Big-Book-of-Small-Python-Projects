"""Birthday Paradox Simulation, by Al Sweigart al@inventwithpython.com
Explore the surprising probabilities of the "Birthday Paradox".
More info at https://en.wikipedia.org/wiki/Birthday_problem
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: short, math, simulation"""

import datetime as dt, random as r


def getBirthdays(numberOfBirthdays):
    """Get a list of random birthdays """
    newBirthdays = []
    for k in range(numberOfBirthdays):
        yearStart = dt.date(1994, 1, 1)  # Set start date
        someDays = dt.timedelta(r.randint(0, 364))  # add some days
        bday = yearStart + someDays  # now you have a birthday

        newBirthdays.append(bday)  # add birthday to the list

    return newBirthdays


def getMatch(birthdayList):
    """Get birthdays that are shared in the list"""
    matchingBirthdays = []
    if len(birthdayList) == len(set(birthdayList)):
        return matchingBirthdays  # All birthdays Unique

    for a, birthdayA in enumerate(birthdayList):
        for b, birthdayB in enumerate(birthdayList[a + 1:]):
            if birthdayA == birthdayB:
                if birthdayA not in matchingBirthdays:
                    matchingBirthdays.append(birthdayA)
    return matchingBirthdays  # return the matching birthday


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
        if i != 0:
            print(", ", end='')
        mName = MONTHS[birthday.month - 1]
        dateText = f'{mName} {birthday.day}'
        print(dateText, end='')
    print()
    print()

    match = list()
    match.extend(getMatch(birthdays))

    print("In this simulation, ", end='')

    if len(match) != 0:
        for i, matchedBDay in enumerate(match):
            if i != 0:
                print(", ", end='')
            mName = MONTHS[matchedBDay.month - 1]
            dateText = f'{mName} {matchedBDay.day}'
            print(dateText, end='')
    else:
        print("There are no matching birthdays")
    print()

    # Run through 100k simulations
    print("Generating a new batch of ", numBdays, "Random Birthdays 100,000 times...")
    input('Press Enter to begin')

    simMatch = 0  # how many simulations had a matching birthday in them
    numMatches = 0  # how many matches there were across all simulations
    simNum = 100_000 * numBdays
    for i in range(100_000):
        # progress report every 10k
        if i % 10_000 == 0:
            print(i, 'simulations run so far.')

        birthdays = getBirthdays(numBdays)

        match = list()

        match.extend(getMatch(birthdays))

        # add to match counter
        if len(match) != 0:
            for m in match:
                numMatches += 1
            simMatch += 1
    print('Done Running Simulations')

    # Display Results
    totalBDaysMade = numBdays * 100_000
    probability_oneRound = round((simMatch / 100_000) * 100, 2)
    probability_allSims = round(numMatches/totalBDaysMade * 100, 2)
    print(f'''\tOut of 100,000 simulations there was a matching birthday in each group of {numBdays} people {simMatch} times. 
    This means that out of {numBdays} people have a {probability_oneRound}% chance of having a matching birthday in the group each round.
    That\'s probably more than you would think!
    
    In total there were {numMatches} matching birthdays found out of the {simNum} simulations run!
    Which means you have a {probability_allSims}% chance of sharing a birthday in a group {totalBDaysMade} people big!
    ''')
    print('Would you like to run another simulation? Y/N')
    user_choice = input('> ')
    if not user_choice.lower().startswith('y') or user_choice.lower().startswith('n'):
        user_choice = input("Enter a valid option\n> ",)

    elif user_choice.lower().startswith('y'):
        continue
    elif user_choice.lower().startswith('n'):
        break

