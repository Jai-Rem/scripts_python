# -*- coding: utf8 -*-

flagError=True
bissextile=False

while flagError :
	
	try:
		flagError=False
		yearEnter = input("Veuillez saisir une année s'il vous plait : \n")
		yearEnter = int(yearEnter)
	except (NameError,ValueError) as error:
		print "Vous n'avez pas saisi un nombre. Veuillez recommencer."
		flagError=True

if yearEnter % 400 == 0:
	bissextile=True

elif yearEnter % 100 == 0:
	bissextile=False

elif yearEnter % 4 == 0:
	bissextile=True
	
else:
	bissextile=False

if bissextile :
	print yearEnter," est une année bissextile."
else :
	print yearEnter," n'est pas une année bissextile."
