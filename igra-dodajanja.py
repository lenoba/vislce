import pprint
import time

def je_anagram(alfa,beta):
	return sorted(alfa.lower()) == sorted(beta.lower())
	
def je_ok(alfa,beta):
	if len(beta) != len(alfa)+1:
		return False
	if len(set(beta)-set(alfa)) == 1:
		if je_anagram(alfa, "".join(letter for letter in beta if letter in alfa)):
			return True
	return False

def najdi_plus1(trenutno, seznam):
	global lines
	if trenutno in seznam:
		return
	for word in lines:
		if je_ok(trenutno, word):
			if trenutno not in seznam:
				seznam[trenutno] = []
			seznam[trenutno].append(word)
	else:
		if trenutno not in seznam:
			seznam[trenutno] = [""]
	
if __name__ == '__main__':
	import sys
	lines = open('besede.txt').read().splitlines()
	trenutno = sys.argv[1]
	variante = {}

	print "priprava baze..."
	start = time.time()
	najdi_plus1(trenutno, variante)

	while True:
		temp = {}
		for word in variante:
			for wordplus in variante[word]:
				if wordplus == "":
					break
				if wordplus not in variante:
					najdi_plus1(wordplus, temp)

		variante2 = {}
		variante2.update(variante)
		variante2.update(temp)
		if len(variante2.keys()) == len(variante.keys()):
			break
		else:
			variante.update(variante2)

	print ""
	end = time.time()
	print "Trajalo:",end-start,"s"
	#pprint.pprint(variante)
		
	#pprint.pprint(sorted(variante.keys(), key=lambda x: len(x)))

	def izpis(key,depth=1):
		global variante
		if key == '':
			return
		filter = []
		for word in variante[key]:
			if word != '' and word not in filter:
				print depth*"\t", word
				filter.append(word)
				izpis(word,depth+1)


	print "priprava izpisa..."
	print sys.argv[1]
	while True:
		for key in sorted(variante.keys(), key=lambda x: len(x)):
			if variante[key] == [""]:
				continue
			izpis(key)
		else:
			break


#walk_dict(variante)




