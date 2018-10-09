# -*- coding: utf-8 -*-

class Drugstore:

	listDrugs=[]
	listClients=[]

	def __init__(self):
		self.drug_dictionary=dict()

	def _provision(self,nameDrug,quantity):
		#Get quantity of name's drug in stock and add new quantity
		#if nameDrug in self.drug_dictionary:
		self.drug_dictionary[nameDrug]+=quantity
		print("Nouvelle quantité pour le médicament ",nameDrug," : ",self.drug_dictionary.get(nameDrug))

		#Else add a new drug in dictionary
		#else:
		#	self.drug_dictionary[nameDrug]=


	def _stockDisplay(self):
		for key,value in self.drug_dictionary.items():
			print("Medicament {} ; Quantité : {}".format(key,value))

	def _addInDrugsList(self,drugObject):
		#Add object Drug in a list
		self.listDrugs.append(drugObject)

	def _displayDrugsList(self):
		#For each object Drug in the list, display name and price of the object
		for elt in self.listDrugs:
			print("Nom du médicament : ",elt.nameDrug, ", prix : ",elt.priceDrug)

	def _addInClientList(self,clientObject):
		#Add object Client in a list
		self.listClients.append(clientObject)

	def _displayClientList(self):
		#For each object Client in the list, display name and credit
		for elt in self.listClients:
			print("Nom du client : ",elt.nameClient, ", credit : ",elt.creditClient)

	def _checkDrug(self,nameDrug):

		drugFind=False

		for key,value in self.drug_dictionary.items():
			#print("Medicament : ",key)
			if key.lower()==nameDrug.lower():
				drugFind=True
			#	print("Trouvé !")

		return drugFind
