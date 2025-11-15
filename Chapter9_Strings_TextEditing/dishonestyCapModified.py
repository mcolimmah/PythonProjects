# Write your code here :-)
### A Program to calculate the Dishonesty Capacity of Manufacturers :-)

while True:
    print('Enter TB or GB for the Advertised unit:')
    unit = input('>>>>>>')

    if unit == 'exit' or unit == 'Exit':
        break

    elif unit.upper() == 'TB':
        discrepancy = 1000000000000 / 1099511627776

    elif unit.upper() == 'GB':
        discrepancy = 1000000000 / 1073741824

    print ('Enter the Advertised Capacity:')
    advertised_capacity = input('>>>>>>')


    ''' Calculate the amount that the advertised capacity lies: '''

    advertised_capacity = float(advertised_capacity)

    ''' Calculate the Real Capacity, round it to the nearest Hundredths,
    and convert it to a string so it can concatenate:'''

    real_capacity = str(round(advertised_capacity * discrepancy, 2))

    print ('The actual Capacity is ' + real_capacity + ' ' + unit)

    continue












