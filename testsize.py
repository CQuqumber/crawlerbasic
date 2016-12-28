def make_big_index(size):
	index = []
	letters = ['a','a','a','a','a','a','a','a']

	for i in range(len(letters) -1, 0, -1):
		print i
		if letters[i] < 'z':
			letters[i] = chr(ord(letters[i]) + 1)
			break
		else:
			letters[i] = 'a'

make_big_index(5)