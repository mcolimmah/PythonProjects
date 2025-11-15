# Write your code here :-)

## This code converts a given list to a Tuple

spam = ['apples', 'bananas', 'tofu', 'cats']


def listconvert(items):
    while True:
        if not items:  ## Checks if the list is empty
            return 'This is an Empty List'

        elif len(items) == 1:  ### Only one items
            return tuple(items)

        else:
        ## Join all items except the last with ',' , then add 'and' before the last
        #return ' , '.join(items[:-1]) + ', and ' + items[-1]
            list_main = (tuple(items))
            return ' , '.join(list_main[:-1]) + ', and ' + list_main[-1]

        continue


#listconvert(spam)
