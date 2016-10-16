#! /usr/local/bin/python3
import random, logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.DEBUG)
logging.debug('Start of program')

guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.randint(0, 1) # 0 is tails, 1 is heads
logging.debug(toss)

if toss == 1:
    toss_str = 'heads'
elif toss == 0:
    toss_str = 'tails'

if toss_str == guess:
    print('You got is!')
else:
    print('Nope! Guess again!')
logging.debug('End of program')
