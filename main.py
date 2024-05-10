import array

# Create Array
temperatureArray = array.array('i', [])

#Prompt user for number of days
while True:
    numDays = input('Please enter a number representing the number of days: ')
    if numDays.isdigit():
        confirm = input(f'You entered {numDays}, is this correct y / n? ').upper()
        if confirm == 'Y':
            False
            break
        else:
            continue
    else:
        print('Invalid, please enter a number')