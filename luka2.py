print "dobrodosli v vislicah!"
print "pa zacnimo, imas 12 poiskusov! \n"
import random
with open("besede.txt") as text:
	besede = text.read().split()
	beseda = random.choice(besede)
pravilno = []
napacno = []
runde = 12
prazno='_'*len(beseda)
print "Izbrana beseda je: " ,prazno

while runde > 0:
	for i in range(len(beseda)):
		
		crka = raw_input ("Ugibaj sedaj: ")[:1]
		if crka in beseda:
			index = -1
			while beseda.index(crka,index+1):
				index = beseda.index(crka)
				prazno = prazno[:index] + crka + prazno[index + 1:]
			print "status besede je:" ,prazno
			pravilno.append(crka)
			print "uganjene besede: " ,pravilno
			print "napacne besede: " ,napacno
			print ""
			
		else:
			runde -=1
			print "Poskusi znova!"
			print "Ostali poiskusi: " ,runde
			print "status besede je:" ,prazno
			napacno.append(crka)
			print "uganjene besede: " ,pravilno
			print "napacne besede: " ,napacno
			print ""
			
	if '_' not in prazno:
		print "cestitamo, zmagal si! Uganil si besedo" ,beseda
		break

else:
	print "Zmanjkalo ti je poiskusov! Vec srece prihodnjic"
	
	#ZA PORAVT:
	#Nedela ce sta dve crki enaki
	#Prepreci podvojene vnose
	#Napake stejejo za zmago
	#Med crticam bi lahko bil presledek 
