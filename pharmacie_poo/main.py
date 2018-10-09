# -*- coding: utf-8 -*-

# Main class
# Interface with the others program classes

from client import *
from drug import *
from drugstore import *

def main():
	print("\n 1 : Achat de medicament \n \
2 : Approvisionnement en medicaments \n \
3 : Etats des stocks et des credits \n \
4 : Liste des médicaments et des clients enregistrés \n \
5 : Quitter")

	question()

def question():

	try:
		choose_number = input('Choisissez un nombre : ')
		choose_number = int(choose_number)

		assert ((choose_number >= 0) and (choose_number <= 4))
	except(NameError,ValueError) as error:
		print("Vous n'avez pas saisi un nombre. Veuillez recommencer.")
		choose_number=main()
	except AssertionError:
		print("Veuillez saisir un nombre entre 0 et 4. Veuillez recommencer.")
		choose_number=main()

	'''Switch to choose the class correspond to the choose
	choose_number = {
		1 : drug(),
		2 : drugstore(),
		3 : drugstore(),
		4 : exit(),
	}
	choose_number.get(argument, "Invalid response")
	'''

	#=== CHOICE NUMBER 2 :  PROVISION A STOCK'S DRUGS ===

	if choose_number == 2:
		drugFind=False

		while(not drugFind):
			nameDrug = input('Nom du medicament ?:')
			drugFind=drugstore._checkDrug(nameDrug)
			if(not drugFind):
				print("Le nom du medicament indiqué n'a pas été trouvé. Veuillez recommencer.")

		while(True):
			try:
				quantity = input('Donner la quantite :')
				quantity = int(quantity)

			except(ValueError) as error:
				print("Vous n'avez pas saisi une quantité, veuillez recommencer.")
				continue
			break

		drugstore._provision(nameDrug,quantity)

	#=== CHOICE NUMBER 3 : 

	if choose_number == 3:
		print("Affichage des stocks")
		drugstore._stockDisplay()


	#=== CHOICE NUMBER 4 : DRUGS AND CLIENTS LIST ===

	if choose_number == 4:
		print("Liste des drogues enregistrés")
		drugstore1._displayDrugsList()
		print("Liste des clients enregistrés")
		drugstore1._displayClientList()



drugstore1 = Drugstore()

aspiron=Drug("Aspiron",10)
rhinoplexil=Drug("Rhinoplexil",10)
efferalgan=Drug("Efferalgan",10)

#Je n'ai pas trouvé d'autres méthodes... J'aurais souhaité pour chaque instanciation de médicament l'ajouter directement à une liste d'ojects "Médicament" (différent du stock)
drugstore1._addInDrugsList(aspiron)
drugstore1._addInDrugsList(rhinoplexil)
drugstore1._addInDrugsList(efferalgan)


client1=Client("VERSTRAETE Jeremy",100)
client2=Client("MARTIN Thibaut",850)
client3=Client("DOERLER Celian",600)

drugstore1._addInClientList(client1)
drugstore1._addInClientList(client2)
drugstore1._addInClientList(client3)




main()