def shopping_list():
    groceries = {}
    question = ''
    thing = ''
    quant = ''
    while True:
        question = input('Would you like to ADD items, REMOVE items, SHOW your current list, or QUIT? ').lower()
        if question == 'quit': break
        elif question == 'add':
            thing = input('What item would you like to add? ').lower()
            if thing == 'quit': break
            try:
                quant = int(input('How many of the item would you like to add? Please answer only using numerical digits. '))
                if quant == 'quit': break
                if thing not in groceries:
                    groceries[thing] = quant
                    print(f'Added {quant} {thing} to your shopping list!')
                else:
                    groceries[thing] += quant
                    print(f'Added {quant} more {thing} to your shopping list!')
            except ValueError: print('Bruh. I asked ya to just give me digits. Cut me a break here. Let\'s take it from the top.')
        elif question == 'remove':
            if groceries == {}: print('You don\'t have a list to remove from yet. Silly goose.')
            else:
                thing = input('What item would you like to remove? ').lower()
                if thing == 'quit': break
                if thing not in groceries:
                    print('Please try again, that item is not on your shopping list.')
                else:
                    try:
                        quant = int(input('How many of the item would you like to remove? Please answer only using numerical digits. '))
                        if quant == 'quit': break
                        if groceries[thing] - quant <= 0:
                            del groceries[thing]
                            print(f'Removed all {thing} from your shopping list!')
                        else:
                            groceries[thing] -= quant
                            print(f'Removed {quant} {thing}')
                    except ValueError: print('Bruh. I asked ya to just give me digits. Cut me a break here. Let\'s take it from the top.')
        elif question == 'show':
            if groceries == {}: print('You haven\'t added anything to your shopping list yet.')
            else:
                print('Your current shopping list is:')
                print('------------------------------')
                for item, amount in groceries.items():
                    print(f'{item}: {amount}')
                print('')
        else: print('Invalid input. Please type ADD, REMOVE, SHOW, or QUIT.')

    if groceries == {}: print('No shopping list for you :(')
    else:
        print('Your finalized shopping list is:')
        print('------------------------------')
        for item, amount in groceries.items():
            print(f'{item}: {amount}')

def square_footage(length, width):
    return (length * width)

def circumference(radius):
    from math import pi
    return (2 * pi * radius)