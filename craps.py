from random import randint

print('come-out')
r1 = randint(1, 6)#rename variable to firstDice
r2 = randint(1, 6)#rename variable to secondDice
v = r1 + r2 #rename variable v to comeOutValue
print(v)
if v == 7 or v == 11: #add constants to replace magic numbers 7 and 11
    print('You win!')
elif v == 2 or v == 3 or v == 12: #change magic numbers again
    print('Craps, you lose.')
else:
    print('The point is', v)
    r1 = randint(1, 6)
    r2 = randint(1, 6)
    w = r1 + r2 #change w to current roll
    print(w)
    while w != v and w != 7: 
        r1 = randint(1, 6)
        r2 = randint(1, 6)
        w = r1 + r2
        print(w)
    if w == 7:
        print('Seven out, you lose.')
    else:
        print('Pass, you win!')
