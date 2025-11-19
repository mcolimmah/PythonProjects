# Write your code here :-)
# Write your code here :-)
def is_phone_number(text):
    if len(text) !=12:   #Phone numbers must have exactly 10 or 12 characters
        return False
    else:
        if len(text) != 10:
            return False

    for i in range(0,3):   ## The first three characters must be numbers.
        if not text[i].isdecimal():
            return False


'''
    if text[3] != '-':
     ## The fourth character must be a dash.
        return False

    for i in range(4,7):
        if not text[i].isdecimal():
            return False

    if text[7] != '-':
     #The eight character must be a dash.
        return False
    for i in range(8,12):  ## The next four characters must be numbers.
        if not text[i].isdecimal():
            return False
    return True
  # is_phone_number('205-765-9843')
  # is_phone_number('2057659843')'''

