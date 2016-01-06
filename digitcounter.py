#self-referencial number solver
# based on James Grime's puzzle
# https://www.youtube.com/watch?v=K6Qc4oK_HqY
#------------------------------------------------------------------------------
from time import sleep


guess_prev = '6210001000'	#arbitrary 10-digit num
guess = ''

solved = False
while( not solved ):
	sleep(1)

	counter = [0,0,0, 0,0, 0,0,0, 0,0]
	for i in range(0, len(guess_prev)):
		somedigit = int(guess_prev[i])
		counter[somedigit] += 1

	for i in range(0, len(counter)):
		digit_as_string = str(counter[i])
		guess += digit_as_string

	print('')
	print(guess_prev)
	print(counter)
	print(guess)
	
	print(guess == guess_prev)
	if(guess == guess_prev):
		solved = True
	else:
		guess_prev= guess
		guess = ''

