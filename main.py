import array

# Create Array
temperatureArray = array.array('i', [])

#Prompt user for number of days
while True:
    numDays = input('Please enter a number representing the number of days: ')
    if numDays.isdigit():
        confirm = input(f'You entered {numDays}, is this correct y / n? ').upper()
        if confirm == 'Y':
            numDays = int(numDays)
            False
            break
        else:
            continue
    else:
        print('Invalid, please enter a number')

day = 1
while day <= numDays:
    temperature = input(f'Enter the temperature for day {day}: ')
    if temperature.isdigit():
        temperatureArray.append(int(temperature))
        day += 1
    else:
        continue

average = 0
daysAbove = 0
for temp in temperatureArray:
    average += temp

average = round(average / numDays, 2)

for temp in temperatureArray:
    if temp > average:
        daysAbove += 1

print(f'Average Temperature: {average} \nDays above average: {daysAbove}')