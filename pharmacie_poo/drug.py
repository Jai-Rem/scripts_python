# -*- coding: utf-8 -*-

from drugstore import *

class Drug:

	def __init__(self, nameDrug, priceDrug):
		self.nameDrug=nameDrug
		self.priceDrug=priceDrug

	def getNameDrug(self):
		return (self.nameDrug)

	def getPriceDrug(self):
		return (self.priceDrug)

