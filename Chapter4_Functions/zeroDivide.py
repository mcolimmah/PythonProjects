# Write your code here :-)

def spam(divideBy):
    try:
        # Any code in this block that causes ZeroDivisionError won't crash the program:
        return 42 / divideBy
    except ZeroDivisionError:
    # If ZeroDivisionError happened, the code in this block runs:
        print('Error: Invalid argument.')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
