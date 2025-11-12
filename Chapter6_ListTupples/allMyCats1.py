# Write your code here :-)
#print('Enter the name of cat 1:')
#cat_name_1 = input()
#print('Enter the name of cat 2:')
#cat_name_2 = input()
#print('Enter the name of cat 3:')
#cat_name_3 = input()
#print('Enter the name of cat 4:')
#cat_name_4 = input()
#print('The cat names are:')
#print(cat_name_1 + ' ' + cat_name_2 + ' ' + cat_name_3 + ' ' + cat_name_4)


## A more efficient way of writing the above code is

cat_names = []

while True:

    print('Enter the name of cat ' + str(len(cat_names) + 1) +
    ' (Or enter nothing to stop.):')

    name = input('>>>>>>>>')
    if name == '':
        break

    cat_names = cat_names + [name] # List concatenation

print('The cat names are:')

for name in cat_names:
    print(' ' + ' ' + '    '+ name)
