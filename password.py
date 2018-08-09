if __name__ == '__main__':
	lines = open('besede.txt').read().splitlines()
	stats = {}
	words = []
	max_bes = ""
	for word in lines:
		letter=len(word.decode("utf-8"))
		if letter == 4 and word.isalpha():
			words.append(word)


import random
for x in range(20):
	print "%s%d%s" % (random.choice(words), random.randint(0,9), random.choice(words))

