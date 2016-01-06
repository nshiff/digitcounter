#self-referencial number solver
# based on James Grime's puzzle
# https://www.youtube.com/watch?v=K6Qc4oK_HqY
#------------------------------------------------------------------------------
from time import sleep
import random

def countdigits(numberstring):
	counter = [0,0,0, 0,0, 0,0,0, 0,0]

	for i in range(0, len(numberstring)):
		somedigit = int(numberstring[i])
		counter[somedigit] += 1
	return counter

def generateguess(counter):
	guess = ''
	for i in range(0, len(counter)):
		digit_as_string = str(counter[i])
		guess += digit_as_string
	return guess

if __name__ == '__main__':
	
	guess_prev = '5487454874'
	guess = '5487454873'
	while( guess != guess_prev ):
		guess_prev = guess
		counter = countdigits(guess_prev)
		guess = generateguess(counter)

		print('')
		print(guess_prev)
		print(counter)
		print(guess)
		print(guess == guess_prev)
		sleep(0.2)
