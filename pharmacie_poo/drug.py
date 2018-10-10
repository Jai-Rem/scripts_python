# -*- coding: utf-8 -*-

from drugstore import *

class Drug:

	def __init__(self, nameDrug, priceDrug):
		self.nameDrug=nameDrug
		self.priceDrug=priceDrug

	def _getNameDrug(self):
		return (self.nameDrug)

	def _getPriceDrug(self):
		return (self.priceDrug)

