# This program does the shelving so I can reused the settings or values next time I run this program,

import shelve
shelf_file = shelve.open('mydata')

shelf_file['cats'] = ['Zophie', 'Pooka', 'Simon']

shelf_file.close()

print(shelf_file)


shelf_file = shelve.open('mydata')

print(type(shelf_file))

print(shelf_file['cats'])
shelf_file.close()

shelf_file = shelve.open('mydata')
list(shelf_file.keys())
print(list(shelf_file.keys()))

print(list(shelf_file.values()))

shelf_file.close()


