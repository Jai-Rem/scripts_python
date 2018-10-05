# -*- coding: utf8 -*-

from random import randrange
from math import ceil

repeat=True
restart=True

moneyWin=0
numberBet=0

while restart :

	while repeat :

		try:
			# DANS LA CORRECTION : Il a utilisé deux boucles while (nombre misé et argent) avec directement les conditions à respecter
			# DANS LA CORRECTION : Il part avec 1000 euros d'argent et vérifie à chaque fois s'il y assez d'argent
			numberBet=input("Veuillez mise une somme d'argent s'il vous plait : \n")
			numberBet=float(numberBet)

			numberChoose=input("Veuillez saisir un nombre compris entre 0 et 49 s'il vous plait : \n")
			numberChoose=int(numberChoose)

			if numberBet <= 0:
				print ("Vous n'êtes pas sérieux ? Vous devez miser plus que zéro ! \n")
				repeat=True

			elif numberChoose>=0 and numberChoose<=49:
				repeat=False

			else:
				print "Vous n'avez pas saisie un nombre compris entre 0 et 49. \n"
				repeat=True

		except (NameError,ValueError) as error:
			print "Vous n'avez pas saisi un nombre. Veuillez recommencer."
			repeat=False
			# DANS LA CORRECTION : Il a utilisé continue


	randomNumber=randrange(50)

	print "Le nombre aléatoire obtenu est : ",randomNumber

	if numberChoose==randomNumber:
		moneyWin=numberBet*3
		# Round the value in whole numbers
		moneyWin=ceil(moneyWin)
		print "Vous avez gagné ! Vous avez misé sur le nombre exact ! \n Vous remportez : ",moneyWin 

	elif ((numberChoose % 2 == 0) and (randomNumber % 2 == 0)) or ((numberChoose % 2 != 0) and (randomNumber % 2 != 0)):
		# CORRECTION : Au lieu de vérifier si c'est négatif ou positif, comparer directement : numberChoose % 2 == randomNumber % 2
		moneyWin=numberBet*0.5
		moneyWin=ceil(moneyWin)
		print "Le nombre que vous avez misé est de la même couleur que le nombre obtenu. \n Vous remportez : ",moneyWin 

	else:
		print "Dommage pour vous, ce n'est pas la bonne couleur ! Vous perdez votre mise ! \n"

	while True :
		responseRestart=input("Voulez vous recommencer ? (reponse : y/n) \n")
		if responseRestart=="n":
			print("Ok. On arrête la partie ! :)")
			restart=False
			break
		elif responseRestart=="y":
			print("C'est reparti !")
			repeat=True
			break
		else:
			print("Mauvaise reponse ! Répondez par y ou n")			

# CORRECTION : Mettre en pause le système
# os.system("pause")