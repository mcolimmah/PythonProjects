# Write your code here :-)
import re

phone_re = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phone_re.search('My number is 415-555-4242.')
 #mo.group(1) # Returns the first group of the matched text
#mo.group(2) # Returns the second group of the matched text

#mo.group(0) # Returns the full matched text

#mo.group() # Also returns the full matched text
