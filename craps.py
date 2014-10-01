from random import randint
#NOT COMPLETE
Win_Values =[7,11]
Lose_Values = [2,3,12]

print('come-out')
firstDice = randint(1, 6)#rename variable to firstDice
secondDice = randint(1, 6)#rename variable to secondDice
comeOutValue = firstDice + secondDice #rename variable v to comeOutValue
print(comeOutValue)
for e in Win_Values:
    if comeOutValue = e:#add constants to replace magic numbers 7 and 11
        print('You win!')
        
    elif v == 2 or v == 3 or v == 12: #change magic numbers again
        print('Craps, you lose.')
    else:
        print('The point is', comeOutValue)
        firstDice = randint(1, 6)
        secondDice = randint(1, 6)
        currrentRoll = firstDice + secondDice #change w to currentRoll
        print(currentRoll)
    while currentRoll != comeOutValue and currentRoll != 7: 
        firstDice = randint(1, 6)
        secondDice = randint(1, 6)
        currrentRoll = firstDice + secondDice
        print(currentRoll)
    if currentRoll == 7:
        print('Seven out, you lose.')
    else:
        print('Pass, you win!')
