if __name__ == '__main__':
	print "<html><head><meta charset=\"UTF-8\"></head><body>"
	lines = open('besede.txt').read().splitlines()
	stats = {}
	print "<h3>Pogostost crk</h3>"
	for word in lines:
		for letter in word.decode("utf-8").upper():
			if letter in stats:
				stats[letter] += 1
			else:
				stats[letter] = 1
	vse = sum([v for _k,v in stats.iteritems()])
	for key, value in sorted(stats.iteritems(), key=lambda (k,v): (v,k), reverse=True):
		print "%s: %s [ %.4f%% ]<br>" % (key, value, value/float(vse)*100)

	print "<h3>Pogostost prvih crk</h3>"
	stats = {}
	for word in lines:
		letter= word.decode("utf-8").upper()[0]
		if letter in stats:
			stats[letter] += 1
		else:
			stats[letter] = 1
	vse = sum([v for _k,v in stats.iteritems()])
	for key, value in sorted(stats.iteritems(), key=lambda (k,v): (v,k), reverse=True):
		print "%s: %s [ %.4f%% ]<br>" % (key, value, value/float(vse)*100)


	print "<h3>Pogostost zadnjih crk</h3>"
	stats = {}
	for word in lines:
		letter= word.decode("utf-8").upper()[-1]
		if letter in stats:
			stats[letter] += 1
		else:
			stats[letter] = 1
	vse = sum([v for _k,v in stats.iteritems()])
	for key, value in sorted(stats.iteritems(), key=lambda (k,v): (v,k), reverse=True):
		print "%s: %s [ %.4f%% ]<br>" % (key, value, value/float(vse)*100)


	print "<h3>Pogostost dolzine besed</h3>"
	stats = {}
	max_bes = ""
	for word in lines:
		letter=len(word.decode("utf-8"))
		if letter > len(max_bes):
			max_bes = word
		if letter in stats:
			stats[letter] += 1
		else:
			stats[letter] = 1
	vse = sum([v for _k,v in stats.iteritems()])
	for key, value in sorted(stats.iteritems(), key=lambda (k,v): (v,k), reverse=True):
		print "%s: %s [ %.4f%% ]<br>" % (key, value, value/float(vse)*100)
	print vse

print "</body></html>"
