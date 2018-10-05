# -*- coding: utf8 -*-

import os
from donnees import *
import re
import pickle


debug=True

#Function to set each letter of word in a dictionnary and another dictionnary with "*"
def setWordInDictio(p_word):
	i=0
	for letter in p_word:
		dictionnary_letters[i]=letter
		dictionnary_lettersFind[i]="*"
		i+=1

	return dictionnary_letters,dictionnary_lettersFind

def writeScoring(p_file,p_surname,p_score):
	p_surname=str(p_surname)
	p_score=str(p_score)
	allLines=""
	
	try:
		file_scoring=open(p_file,'r')
	
		for line in file_scoring:
			if surname in line:
				print("Le prénom a été trouvé ! Inscription nouveau score")
				allLines=allLines+"\n"+p_surname+":"+p_score+"\n"
			else:
				print("Stockage de la ligne")
				currentLine=file_scoring.readline()
				allLines=allLines+"\n"+str(currentLine)
				print(allLines)


		file_scoring.close()

		file_scoring=open(p_file,'w')
		file_scoring.writelines(allLines)
		file_scoring.close()

	except FileNotFoundError:
		file_scoring=open(p_file,'w')
		print("Création du fichier qui n'a pas été trouvé")
		file_scoring.write(p_surname+":"+p_score+"\n")

	found = False

	

	'''with open(p_file,'wb') as file:
		my_pickler = pickle.Pickler(file)
		my_pickler.dump(p_score)
	'''







#choose a random word with "donnees.py" file
random_word=random_word()
#set each letter of word in dictionnary
dictionnary_letters=dict()
dictionnary_lettersFind=dict()
dictionnary_letters,dictionnary_lettersFind=setWordInDictio(random_word)

#Define number of tests possible in file "donnees.py"
number_tests=number_tests()

#Define variable for surname
surname=""

#Define variable for score of user
score=0

#File score
file_scoring=file_score()

if debug:
	print("Parcours du dictionnaire")
	for key,value in dictionnary_letters.items():
		print("La clé {} contient la valeur {}.".format(key,value))

	for key,value in dictionnary_lettersFind.items():
		print("La clé {} contient la valeur {}.".format(key,value))

	print("Mot choisi : "+random_word)



print("On va jouer au pendu, trouvez le mot. Vous avez "+str(number_tests)+" tentatives possibles.")

while(True):

	try:
		surname=input("Veuillez indiquer votre prénom s'il vous plait : ")

		if not(surname):
			raise ValueError("Vous n'avez rien saisi, veuillez recommencer s'il vous plait.")

	except (ValueError,SyntaxError) as error:
		print(error)
		continue
	
	break


setScore=writeScoring(file_scoring,surname,score)

# User can try 8 tests
for i in range(1,number_tests+1):


	# As long as there is an error, we ask the question
	while(True):

			letterChoose=input("Veuillez saisir une lettre s'il vous plait : ")

			#check if input is a letter
			if letterChoose.isalpha() == False :
				print("Ce n'est pas une lettre ! Veuillez recommencer.")
			#check if there aren't more one letter
			elif len(letterChoose) > 1 :
				print("Vous devez saisir une seule lettre")
			else :
			#if all is ok, exit the loop
				break

	if letterChoose in dictionnary_letters.values():
		print("La lettre "+letterChoose+" a été trouvée dans le mot !")
		#Find the key of the value
		#index is a function of list, not of a dict_values object returned by dico.values(). So, change your code so that dico.values() is converted to a list
		# Remarque : La commande suivante ne fonctionne pas lorsque l'on a plus valeurs identiques
		#print (list(dictionnary_letters.keys())[list(dictionnary_letters.values()).index(letterChoose

		#Set the letter find in the dictionnary result
		for key,value in dictionnary_letters.items():
			if value==letterChoose:
				dictionnary_lettersFind[key]=value

		#Display result
		for value in dictionnary_lettersFind.values():
			print(value, end ='')

		print("\n")
		# This line could display the all values, but there is "dict_values"...
		#print(dictionnary_lettersFind.values())

	else:
		print("La lettre "+letterChoose+" n'a pas été trouvée dans le mot !")

	#if there are not "*" in dictonnary, that means user find the word !
	if ("*" in dictionnary_lettersFind.values()) == False :
			print("Vous avez trouvez toutes les lettres ! Félicitation !")
			break

	print("Il vous reste "+str(number_tests-i)+" tentative(s).")

	if (number_tests-i==0) :
		print("Perduuuu ! Le mot était : "+random_word)

			