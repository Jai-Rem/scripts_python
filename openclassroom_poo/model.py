import json
import math #Pour faire la conversion en radiant

class Agent:
	def __init__(self, position, **agent_attributes):
		self.position = position
		for attr_name, attr_value in agent_attributes.items():
			setattr(self, attr_name, attr_value)

class Position:
	def __init__(self, longitude_degrees, latitude_degrees):
		self.longitude_degrees = longitude_degrees
		self.latitude_degrees = latitude_degrees

		'''property : Ainsi on peut l'appeler de notre instance sans parenthèse. Une propriété est une méthode qui est accessible comme un attribut 
		Vous ne voulez pas que votre instance fasse une action, ce qui correspond plutôt à une méthode, mais qu'elle vous renvoie une valeur qui lui est propre. Nous utilisons donc une propriété.
		La longitude en radians est égale à sa longitude en degrés * pi divisé par 180. 
		'''

	@property
	def longitude(self):
		return self.longitude_degrees * math.pi / 180

	@property
	def latitude(self):
		return self.latitude_degrees * math.pi / 180

class Zone:

	'''ATTRIBUT DE CLASSE CI DESSOUS
	Pour créer la première ligne de notre grille, nous devons donc définir certaines variables qui, a priori, ne changeront pas. 
	Nous voulons qu'elles soient associées à la classe et non pas aux instances. 
	En effet, si nous changeons l'abscisse minimale de nos zones, nous voulons le faire pour toutes les instances en une fois. 
	Nous pouvons raisonnablement nous dire que le champ d'action de ces variables sera plus large que celui des attributs d'instance.
	Nous appelons ces variables des attributs de classe car elles appartiennent à la classe dans son ensemble, et non à l'instance. 
	C'est notre zone de manière générale qui a une latitude minimale et une latitude maximale, et non l'instance !
	Un attribut de classe est une variable dont le champ d'action s'étend à l'ensemble d'une classe. 
	Ils sont très utilisés pour compter le nombre d'instances d'une classe par exemple. 
	Par convention, ils sont définis en majuscules et au début de la classe. 
	
	LA LOGIQUE DES VALEURS
	Nous allons utiliser la même logique dans notre grille mais pas les mêmes valeurs, 
	puisque la longitude est comprise entre -180 et 180 degrés et que la latitude, elle, est comprise entre -90 et 90 degrés.
	'''

	MIN_LONGITUDE_DEGREES = -180
	MAX_LONGITUDE_DEGREES = 180
	MIN_LATITUDE_DEGREES = -90
	MAX_LATITUDE_DEGREES = 90
	WIDTH_DEGREES = 1 # degrees of longitude
	HEIGHT_DEGREES = 1 # degrees of latitude

	''' 
	Pourquoi avons-nous créé cette grille ? Pour positionner nos habitants à l'intérieur. 
	Il nous faut donc un moyen de parcourir toutes les zones, d'une manière ou d'une autre, afin de trouver la zone d'habitation de chaque agent. 
	Nous allons donc créer un nouvel attribut de classe pour stocker chaque nouvelle zone qui est créée.
	'''

	ZONES = []


	def __init__(self, corner1, corner2):
		self.corner1 = corner1
		self.corner2 = corner2
		#  Il faut que les habitants par défaut ne soient pas 0 mais une liste vide :
		self.inhabitants=[]

	'''
	J'aimerais pouvoir lancer ma méthode maintenant ! Mais si j'essaie de la lancer, je suis prise moi-même dans une boucle infinie. 
	Le seul moyen que nous connaissions pour lancer une méthode, jusqu'à maintenant, est de créer une instance et de l'utiliser pour exécuter la méthode. 
	Comment lancer une méthode sur une instance alors que cette même méthode est celle qui, justement, est censée les créer ? 
	Il faudrait une méthode qui soit globale, au niveau de la classe, et non de l'instance. En fait nous l'avons déjà fait pour les attributs d'instance et de classe ! 
	Alors, comment le faire pour les méthodes ? Vous ajoutez  @classmethod  juste avant.
	'''

	@classmethod
	# Étant donné que nous ne sommes plus au niveau de l'instance mais au niveau de la classe, nous allons remplacer self par cls (afin de ne pas confondre).
	# En soi, vous pourriez mettre n'importe quel mot : caillou, boubou, chouchou... 
	def initialize_zones(cls):

		
		for latitude in range(cls.MIN_LATITUDE_DEGREES, cls.MAX_LATITUDE_DEGREES, cls.HEIGHT_DEGREES):

			'''
			Nous créons une première boucle qui crée une zone pour chaque nombre compris entre MIN_LONGITUDE_DEGREES et MAX_LONGITUDE_DEGREE.
			La méthode range() permet justement de créer une liste à partir d'une valeur minimale, d'une valeur maximale et d'un intervalle. range(minimal_value, maximal_value, added_value).
			'''

			for longitude in range(cls.MIN_LONGITUDE_DEGREES, cls.MAX_LONGITUDE_DEGREES, cls.WIDTH_DEGREES):
				''' zone = Zone(bottom_left_corner, top_right_corner)
				Chaque instance de type Zone prend en paramètre la position de son coin inférieur gauche et la position de son coin supérieur droit. 
				Dans notre cas, il s'agit de la toute première ligne. La latitude est donc toujours égale à 1 !
				Quant à la longitude de départ, nous y avons déjà accès dans notre boucle :
				'''
				bottom_left_corner = Position(longitude, 1)
				''' 
				Comment calculer la position du coin supérieur droit ? 
				En ajoutant un intervalle ! Nous l'avons d'ailleurs déjà stocké dans l'attribut de classe WIDTH_DEGREE : longitude + cls.WIDTH_DEGREES
				Nous pouvons aussi calculer la latitude du coin supérieur droit et créer la zone correspondante : 1 + cls.HEIGHT_DEGREES
				'''
				top_right_corner = Position(longitude + cls.WIDTH_DEGREES, 1 + cls.HEIGHT_DEGREES)
				zone = Zone(bottom_left_corner,top_right_corner)

				# A l'intérieur de notre méthode qui initialise les zones, nous allons ajouter une à une chaque zone à notre liste ZONES.
				cls.ZONES.append(zone)

		# Afin de connaître combien de zones ont été créées, j'ajoute un print() à la fin :
		print(len(cls.ZONES))

	''' Premièrement, trouvons les zones dans lesquelles habitent chacun de nos agents.
	La solution est de trouver l'index de la zone à partir de l'index de la position. 
	'''

	def contains(self,position):
		return position.longitude >= min(self.corner1.longitude, self.corner2.longitude) and \
			position.longitude < max(self.corner1.longitude, self.corner2.longitude) and \
			position.latitude >= min(self.corner1.latitude, self.corner2.latitude) and \
			position.latitude < max(self.corner1.latitude, self.corner2.latitude)

	@classmethod
	def find_zone_that_contains(cls, position):
		# Compute the index in the ZONES array that contains the given position
		# Verification qu'une zone existe, sinon l'initialiser
		if not cls.ZONES:
			cls.initialize_zones()
		longitude_index = int((position.longitude_degrees - cls.MIN_LONGITUDE_DEGREES)/ cls.WIDTH_DEGREES)
		latitude_index = int((position.latitude_degrees - cls.MIN_LATITUDE_DEGREES)/ cls.HEIGHT_DEGREES)
		longitude_bins = int((cls.MAX_LONGITUDE_DEGREES - cls.MIN_LONGITUDE_DEGREES) / cls.WIDTH_DEGREES) # 180-(-180) / 1
		zone_index = latitude_index * longitude_bins + longitude_index
		# Just checking that the index is correct
		zone = cls.ZONES[zone_index]
		assert zone.contains(position)
		return zone

	'''Nous souhaitons connaître la population d'une zone, c'est-à-dire le nombre total d'habitants, 
	que nous diviserons par le nombre de kilomètres carrés afin d'obtenir la densité de population. 
	Nous allons donc créer une nouvelle méthode qui renvoie le nombre total d'éléments dans la liste de population.
	On la transforme en propriété pour qu'elle effectue une action :
	'''
	@property
	def population(self):
		return len(self.inhabitants)

	#Methode pour ajouter les habitants dans une zone
	def add_inhabitant(self, inhabitant):
		self.inhabitants.append(inhabitant)


def main():
	Zone.initialize_zones()

	for agent_attributes in json.load(open("agents-100k.json")):
		latitude = agent_attributes.pop('latitude')
		longitude = agent_attributes.pop('longitude')
		position = Position(longitude, latitude)
		agent = Agent(position, **agent_attributes)
		#print(position.longitude)
        #print(agent.agreeableness)
		zone = Zone.find_zone_that_contains(position)
		# Ajout d'un habitant
		zone.add_inhabitant(agent)
		print("Zone population : ", zone.population)


main()
