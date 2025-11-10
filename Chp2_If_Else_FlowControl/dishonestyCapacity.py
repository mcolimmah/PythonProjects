### A Program to calculate the Dishonesty Capacity of Manufacturers :-)

print('Enter TB or GB for the Advertised unit:')
unit = input('>>>>>>')


## Calculate the amount that the advertised capacity lies:
if unit == 'TB' or unit == 'tb' or unit == 'Tb':
    discrepancy = 1000000000000 / 1099511627776
elif unit == 'GB' or unit == 'gb' or unit == 'Gb':
    discrepancy = 1000000000 / 1073741824



print ('Enter the Advertised Capacity:')
advertised_capacity = input('>>>>>>')
advertised_capacity = float(advertised_capacity)

## Calculate the Real Capacity, round it to the nearest Hundredths,
## and convert it to a string so it can concatenate:

real_capacity = str(round(advertised_capacity * discrepancy, 2))

print ('The actual Capacity is ' + real_capacity + ' ' + unit)


