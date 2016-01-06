


guess_prev = '4873498745'

counter = [4,8,7, 3,4, 9,8,7, 4,5]

guess = ''
for i in range(0, len(counter)):
	digit_as_string = str(counter[i])
	guess += digit_as_string



print(guess_prev)
print(guess)
print(guess_prev == guess)
