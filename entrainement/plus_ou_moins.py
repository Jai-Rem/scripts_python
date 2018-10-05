# -*- coding: utf-8 -*-

import random

flag_error=0

def get_random_nber():
	rand_nber = random.randint(0,100)
	print "Le nombre mystère est : ", rand_nber
	return rand_nber

def question():
	try:
		numberPropose = input('Quel est le nombre mystère ?  ')
		numberPropose = int(numberPropose)
		return numberPropose
	except (NameError,ValueError) as error:
		print("Vous n'avez pas saisi un nombre. \n Veuillez saisir de nouveau un nombre.")
		numberPropose=question()

mystery_number = get_random_nber()
numberPropose = question()

while numberPropose != mystery_number : 

	if numberPropose < mystery_number :
		print ("C'est trop petit !")
		numberPropose = question()

	elif numberPropose > mystery_number : 
		print ("C'est trop grand !")
		numberPropose = question()

print('Félicitation, vous avez trouvé le nombre mistère !')
