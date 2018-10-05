# -*- coding: utf8 -*-

import random

def random_word():

	list_words=["maison","papier","planifie","assoupir","sel","voix","langage","ville","concert","urgence","pays","personne","cours","horaire","prix","banque","musique","science","trousse","clé","travail","santé","drogue","disque","couteau","écharpe","bol","paperasse"]
	rand_number=random.randint(0,len(list_words) -1)
	word=list_words[rand_number]
	
	return word

def number_tests():

	number_tests=8
	return number_tests

def file_score():
	file_score="score"
	return file_score
