## A function file that calculates the Discrepance
# Write your code here :-)

Value = input('Input the Value ...')
Unit = input('Input the Unit....' )

def actual_capacity(Value, Unit):
    #Unit = str(Units)
    if Unit == 'TB' or Unit == 'tb' or Unit == 'Tb':
        discrepancy = 1000000000000 / 1099511627776
    elif Unit == 'GB' or Unit == 'gb' or Unit == 'Gb':
        discrepancy = 1000000000 / 1073741824

    advertised_capacity = float(Value)


    real_capacity = str(round(advertised_capacity * discrepancy, 2 ))
    real_capacity_2 = str(real_capacity )

    print('The Actual Capacity is, ' + real_capacity_2 + ' ', Unit)

    return


actual_capacity(Value, Unit)

#actual_capacity(100, 'TB')
