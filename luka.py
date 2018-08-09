print "Dobrodosli v vislicah, pa zacnimo!"
import random
with open("besede.txt") as text:
  besede = text.read().split()
  beseda = random.choice(besede)
crtice = sum(c !=" " for c in beseda)
poiskusi = ''
zgodovina = []
pravilno = []
pravilno_sort = []
runde = 12
stevnik = 1
  
while runde > 0:
  napake = 0
  for char in beseda:
    if char in poiskusi:
      print char + " je pravilna crka,"
      pravilno.append(char)
      
      
  else:
        napake +=1
        
        if napake == 0:
          print "Zmagal si!"
          break
        
        print "beseda se glasi: " + "_ " *crtice
        poiskus = raw_input("Vnesi eno crko: ")[:1]
        print ""
        if poiskus not in zgodovina:
          zgodovina.append(poiskus)
          stevnik +=1
         
        poiskusi += poiskus
        if crtice < stevnik:
          print "Cestitamo, zmagal si! Skrivna beseda je bila:" ,beseda
          break
        
        elif poiskus not in beseda:
          runde -= 1
          print "Zmotil si se!"
          print "Ostali poizkusi: " ,runde
          print "Do sedajsna ugibanja: " ,zgodovina
          print "Pravilna ugibanja: " ,pravilno
          print ""
          
          if runde == 0:
            print "Vec srece prihodnjic! Tvoja ugibanja so bila: " ,zgodovina
            
            
            
#za popravt
#--------------------------------------
#uganjene crke morajo biti vnesene v crtice

#nedela ce se crka ponovi
#blokiraj ponovitve v listih z:
#for i in pravilno:
#  if i not in pravilno_sort:
#    pravilno_sort.append(i)