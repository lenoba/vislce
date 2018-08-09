import random
import win_unicode_console

def print_word(secret,guessed,mark="_"):
	return " ".join([ letter if letter in guessed else mark for letter in secret ])

def get_word():
	try:
		lines = open('besede.txt').read().splitlines()
		return random.choice(lines).decode("utf-8")
	except:
		return "banana"

def solved(secret, guessed):
	return sum([1 if letter in guessed else 0 for letter in secret]) == len(secret)

if __name__ == '__main__':
	secret = get_word().upper()
	max_guesses = 10
	n_guesses = 0
	guessed = [] 
	win_unicode_console.enable()

	while n_guesses < max_guesses:
		false_guesses = [letter for letter in guessed if letter not in secret]
		nots = "  [ "+",".join(false_guesses)+" ]" if false_guesses else ""

		print "[%d/%d] %s %s"%(n_guesses, max_guesses, print_word(secret, guessed), nots)
		
		if solved(secret,guessed):
			print "congratulations!"
			break

		guess = raw_input()

		if len(guess)>1 or not guess.isalpha():
			print "you're guessing letters."
			continue

		guess = guess.upper()

		if guess in guessed:
			print "already tried that."
			continue

		guessed.append(guess)
		if guess not in secret:
			n_guesses+=1
	else:
		print "better luck next time!"

	print "solution:",secret
