def make_string(arr):
	s=""
	for e in arr:
		s = s + e
	return s

def add_to_index(index, keyword, url):
	for entry in index:
		if entry[0] == keyword:
			entry[1].append(url)
			return
	index.append([ keyword, [url] ] )

def make_big_index(size):
	index = []
	letters = ['a','a','a','a','a','a','a','a']
	while len(index) < size:
		word = make_string(letters)
		add_to_index(index, word, 'fake')  # Stop the while loop
		for i in range(len(letters) -1, 0, -1):
			print i
			if letters[i] < 'z':
				letters[i] = chr(ord(letters[i]) + 1)
				break  #break out the for loop
			else:
				letters[i] = 'a'
	return index

make_big_index(3)