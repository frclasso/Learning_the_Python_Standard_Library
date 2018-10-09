#!/usr/bin/env python3

# importando o modulo random
import random

# random numbers
print(random.random()) # imprime um numero entre 0 e 1

decider = random.randrange(2) # 0 OU 1
if decider == 0:
    print('HEADS')
else:
    print('TAILS')
print(f'Decider is:', decider)

print("You rolled a " + str(random.randrange(1, 7)))

# random choices
megaSena = random.sample(range(61), 6) # range de 0 a 60, gerando 6 numeros
print(megaSena)

possiblePets = ['cat', 'dog', 'fish']
print(random.choice(possiblePets))

cards = ['Jack', 'Queen', 'Ace', 'King']
random.shuffle(cards)
print(cards)