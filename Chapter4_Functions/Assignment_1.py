# Write your code here :-)


def collatz(number):

        if number % 2 == 0:
            print('The number is EVEN and divisible by 2!, The actual Number is ' + str(number))
            number = 10 * number
            print('The result of the EVEN number manipulation is, ' + str(number))


        elif number % 2 == 1:
            print('The number is ODD and indivisible by 2!, The actual Number is ' + str(number))
            number = 3 * number +1
            print('The result of the ODD number manipulation is, ' + str(number))



collatz(5)
