# -*- coding: utf-8 -*-

class Drugstore:

	listDrugs=[]
	listClients=[]

	def __init__(self):
		self.drug_dictionary=dict()

	def _provision(self,drugObject,quantity):
		#Get quantity of name's drug in stock and add new quantity

		#If object Drug is present yet, add quantity
		if (drugObject in self.drug_dictionary):
			self.drug_dictionary[drugObject]+=quantity
			print("Mise à jour => Médicament : ",drugObject.nameDrug," - Quantité :",self.drug_dictionary[drugObject])
		#else object not present, so add this new object Drug
		else:
			self.drug_dictionary[drugObject]=quantity
			print("Nouveau médicament renseigné : ",drugObject.nameDrug," - Quantité :",quantity)


	def _stockDisplay(self):
		for key,value in self.drug_dictionary.items():
			print("Medicament {} ; prix : {} ; Quantité : {}".format(key.nameDrug,key.priceDrug,value))

	def _checkDrug(self,nameDrug):
		drugFind=""

		for key,value in self.drug_dictionary.items():
			if key.nameDrug.lower()==nameDrug.lower():
				drugFind=key

		if(not drugFind):
			print("Le nom du médicament n'a pas été trouvé. Veuillez recommencer.")
		return drugFind

	def _buyDrug(self,drugObject,quantity,nameClient,paymentClient):

		leftToPay=0

		if (drugObject in self.drug_dictionary):
			if self.drug_dictionary[drugObject]<quantity:
				print("Désolé, mais nous n'avons plus assez de médicaments en stock... Veuillez recommencer.")
				buyDrug=True
			else:
				self.drug_dictionary[drugObject]-=quantity
				print("Mise à jour => Médicament : ",drugObject.nameDrug," - Quantité :",self.drug_dictionary[drugObject])	

				totalPrice=drugObject.priceDrug*quantity
				print("Somme totale de : ",drugObject.priceDrug," x ",quantity," = ",totalPrice)

				leftToPay=totalPrice-paymentClient

				if leftToPay>0:
					print("Il vous reste à payer ",leftToPay," euros. Je vous propose de payer la somme de ",leftToPay," euros à partir de votre crédit...")
				elif leftToPay<0:
					print("Vous avez donner plus que le prix à payer. Nous ajoutons le restant de",-leftToPay," euros à votre crédit...")
				else:
					print("Vous venez de donner la somme exacte pour le paiement, on ne touche pas à votre crédit.")

				for elt in self.listClients:
					if elt.nameClient.lower()==nameClient.lower():
						elt.creditClient=elt.creditClient-leftToPay


	def _addInClientList(self,clientObject):
		#Add object Client in a list
		self.listClients.append(clientObject)

	def _displayClientList(self):
		#For each object Client in the list, display name and credit
		for elt in self.listClients:
			print("Nom du client : ",elt.nameClient, ", credit : ",elt.creditClient)

	def _checkClient(self,nameClient):
		clientFind=""

		for elt in self.listClients:
			if (elt.nameClient).lower()==nameClient.lower():
				clientFind=elt
		
		if(not clientFind):
			print("Le nom du client indiqué n'a pas été trouvé. Veuillez recommencer.")

		#Return object correspond to nameClient
		return clientFind





