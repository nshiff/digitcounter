#self-referencial number solver
# based on James Grime's puzzle
# https://www.youtube.com/watch?v=K6Qc4oK_HqY




guess = 4873498745 # any 10-digit number

guess_str = str(guess)

print(guess_str)


counter = [0,0,0, 0,0, 0,0,0, 0,0]

for i in range(0, len(guess_str)):
	somedigit = int(guess_str[i])
	counter[somedigit] += 1

print(counter)




