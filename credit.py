'''
This code takes any number and detects if it is AMEX, Visa, Mastercard or invalid.
If the user does not input a number, it will reprompt the user.
By Ben
'''

#Variables
evenSum = 0
oddSum = 0

#Input
cardNum = input("Number: ")

while cardNum.isdigit() == False:
    cardNum = input("Number: ")

#Even Digits
for digit in range(1, len(cardNum), 2):
    evenDigit = ((int(cardNum) // (10 ** digit)) % 10)
    if evenDigit >= 5:
        evenSum = evenSum + (evenDigit * 2 - 9)
    else:
        evenSum = evenSum + evenDigit * 2

#Odd Digits
for digit in range(0, len(cardNum), 2):
    oddDigit = ((int(cardNum) // (10 ** digit)) % 10)
    oddSum = oddSum + oddDigit

cardSum = oddSum + evenSum

#Type of card
if cardSum % 10 != 0:
    print("IVALID")

elif len(cardNum) == 15 and \
     int(cardNum) // (10 ** 13) == 34 or int(cardNum) // (10 ** 13) == 37:
    print("AMEX")

elif len(cardNum) == 16 and \
     int(cardNum) // (10 ** 14) == 51 or int(cardNum) // (10 ** 14) == 52 \
     or int(cardNum) // (10 ** 14) == 53 or int(cardNum) // (10 ** 14) == 54 \
     or int(cardNum) // (10 ** 14) == 55:
    print("MASTERCARD")

elif len(cardNum) == 13 and int(cardNum) // (10 ** 12) == 4 \
     or len(cardNum) == 16 and int(cardNum) // (10 ** 15) == 4:
    print("VISA")
else:
    print("INVALID")
                   


                   
        
    
        
