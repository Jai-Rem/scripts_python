# -*- coding: utf-8 -*-

class Client:

	listClients=[]

	def __init__(self, nameClient, creditClient):
		self.nameClient = nameClient
		self.creditClient = creditClient

	def _getNameClient(self):
		return (self.nameClient)

	def _getPriceDrug(self):
		return (self.creditClient)
