Welcome_message = ' Welcome to my Python PIG LATIN Program, Written by Marshal Olimmah '
Welcome_message = Welcome_message.center(100, '*')
print(Welcome_message)
''' Enter the English message to translate into pig latin:
My name is AL SWEIGART and I am 4,000 years old.
Ymay amenay isyay ALYAY EIGARTSWAY andyay Iyay amyay 4,000 yearsyay oldyay.'''

## English to Pig Latin
print('Enter the English message to translate into pig latin: !!!! ')
message = input()

''' Define Readily known vowels since they are not a lot'''
VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')

pigLatin = [] # A list of the words in pig latin
for word in message.split():
    #Separate the non-letters at the start of this word:
    prefixNonLetters = ''
    while len(word)>0 and not word[0].isalpha():
        prefixNonLetters += word[0]
        word = word[1:]
    if len(word) ==0:
        pigLatin.append(prefixNonLetters)
        continue

    ## Separate the non-letters at the end of this word:
    suffixNonLetters = ''
    while not word[-1].isalpha():
        suffixNonLetters += word[-1] + suffixNonletters
        word = word[:-1]

    ## Remember if the word was in uppercase or title case:
    wasUpper = word.isupper()
    wasTitle = word.istitle()

    word = word.lower()  ## Make the word lowercase for translation.

    ## Separate the consonants at the start of this word:
    prefixConsonants = ''
    while len(word) > 0 and not word[0] in VOWELS:
        prefixConsonants += word[0]
        word = word[1:]

    # Add the pig latin ending to the world:
    if prefixConsonants != '':
        word += prefixConsonants + 'ay'
    else:
        word +='yay'

    ## Set the word back to uppercase or title case:
    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()

    ## Add the non-letters back to the start or end of the word.
    pigLatin.append(prefixNonLetters + word + suffixNonLetters)

    #Join all the words back together into a single string:
    print('.'.join(pigLatin))





''' End of Program '''
Goodbye_message = 'I hope you enjoyed using this software Program I wrote for you'
Goodbye_message = Goodbye_message.center(100, '=')
print(Goodbye_message)
