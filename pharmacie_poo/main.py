# -*- coding: utf-8 -*-

# Main class
# Interface with the others program classes

from client import *
from drug import *
from drugstore import *

from decimal import Decimal, DecimalException

def main():
	

	question()


def question():

	while(True):

		print("\n 1 : Achat de medicament \n \
2 : Approvisionnement en medicaments \n \
3 : Etats des stocks et prix des médicaments \n \
4 : Liste des clients enregistrés \n \
5 : Quitter")

		try:
			choose_number = input('Choisissez un nombre : ')
			choose_number = int(choose_number)

			assert ((choose_number >= 0) and (choose_number <= 5))
		except(ValueError) as error:
			print("Vous n'avez pas saisi un nombre. Veuillez recommencer.")
			choose_number=main()
		except AssertionError:
			print("Veuillez saisir un nombre entre 0 et 4. Veuillez recommencer.")
			choose_number=main()

		'''COMMENT ECRIRE UN SWITCH EN PYTON :

		Switch to choose the class correspond to the choose
		choose_number = {
			1 : drug(),
			2 : drugstore(),
			3 : drugstore(),
			4 : exit(),
		}
		choose_number.get(argument, "Invalid response")
		'''

		#=== CHOICE NUMBER 1 : BUY A DRUG ===

		if choose_number == 1:
			clientFind=""
			drugFind=""

			while(not clientFind):
				nameClient = input('Nom du client ?: ')
				clientFind=drugstore._checkClient(nameClient)

			while(not drugFind):
				nameDrug = input('Nom du medicament ?: ')
				drugFind = drugstore._checkDrug(nameDrug)
			
			print("Le prix du médicament",drugFind.nameDrug,"est de :",drugFind.priceDrug,"euros.")

			while(True):
				try:
					paymentClient = input('Quelle somme d\'argent souhaitez vous avancer ?: ')
					paymentClient= Decimal(paymentClient)
					if paymentClient<0:
						raise ValueError("Vous ne pouvez pas saisir un paiement négatif")
						continue

				except(ValueError,DecimalException):
					print("Vous n'avez pas saisi une valeur de type entier ou décimale ou celle-ci est négative, veuillez recommencer.")
					continue
				break


			buyDrug=True

			while(buyDrug):
				try:
					quantity = input('Quelle est la quantite a acheter ?: ')
					quantity = int(quantity)
					if quantity<=0:
						raise ValueError("Vous ne pouvez pas saisir une quantité négative ou nulle")
						continue

				except(ValueError) as error:
					print("Vous n'avez pas saisi un nombre ou celui-ci est négatif ou nul. Veuillez recommencer.")
					continue

				drugstore._buyDrug(drugFind,quantity,nameClient,paymentClient)
				print("Credit de ",clientFind.nameClient," : ",clientFind.creditClient," euros")
				break

				


		#=== CHOICE NUMBER 2 :  PROVISION A STOCK'S DRUGS ===

		if choose_number == 2:
			drugFind=False

			while(not drugFind):
				nameDrug = input('Nom du medicament ?: ')
				drugFind=drugstore._checkDrug(nameDrug)

			while(True):
				try:
					quantity = input('Donner la quantite : ')
					quantity = int(quantity)
					if quantity<=0:
						raise ValueError("Vous ne pouvez pas saisir une quantité négative ou nulle")
						continue

				except(ValueError) as error:
					print("Vous n'avez pas saisi une quantité ou celui-ci est négatif ou nul, veuillez recommencer.")
					continue
				break

			drugstore._provision(drugFind,quantity)



		#=== CHOICE NUMBER 3 : DISPLAY STOCKS ===

		if choose_number == 3:
			print("Affichage des stocks")
			drugstore._stockDisplay()


		#=== CHOICE NUMBER 4 : CLIENTS LIST ===

		if choose_number == 4:
			print("Liste des clients enregistrés et leur crédit respectif")
			drugstore._displayClientList()


		#=== CHOICE NUMBER 5 : EXIT PROGRAM ===

		if choose_number == 5:
			print("Fermeture du programme.")
			break
			exit



drugstore = Drugstore()

aspiron=Drug("Aspiron",10)
rhinoplexil=Drug("Rhinoplexil",10)
efferalgan=Drug("Efferalgan",10)

#Je n'ai pas trouvé d'autres méthodes... J'aurais souhaité pour chaque instanciation de médicament l'ajouter directement à une liste d'ojects "Médicament" (différent du stock)
drugstore._provision(aspiron,5)
drugstore._provision(efferalgan,5)
drugstore._provision(rhinoplexil,15)

client1=Client("Jeremy",50)
client2=Client("MARTIN Thibaut",70)
client3=Client("DOERLER Celian",0)

drugstore._addInClientList(client1)
drugstore._addInClientList(client2)
drugstore._addInClientList(client3)




main()