""" Lists of words for the parser"""

# PLACE_WORDS = [
# 			  "cinema","aquarium","restaurant", "musee", "theatre", 
# 			  "ville", "eglise", "place", "port", "aeroport", "gare"
# 			  ]

QUESTION_WORDS = [
				"hello", "salut", "bonjour", "hey", "yo", "ola", "hi",
				"grandpy", "py", "bot", "pybot", "papy",
				"dis", "moi", "sais", "ou", "trouve", "adresse", 
				"connais", "connaissez", "est-ce-que", "aller", "emmener"
				]

STOP_WORDS = [
			"a","abord","absolument","afin","ah","ai","aie","ailleurs",
			"ainsi","ait","allaient","allo","allons","allô","alors","anterieur",
			"anterieure","anterieures","apres","après","as","assez","attendu","au", 
			"aucun","aucune","aujourd","aujourd'hui","aupres","auquel","aura",
			"auraient","aurait","auront","aussi","autre","autrefois","autrement",
			"autres","autrui","aux","auxquelles","auxquels","avaient","avais",
			"avait","avant","avec","avoir","avons","ayant","b","bah","bas","basee",
			"bat","beau","beaucoup","bien","bigre","boum","bravo","brrr","c","car",
			"ce","ceci","cela","celle","celle-ci","celle-là","celles","celles-ci",
			"celles-là","celui","celui-ci","celui-là","cent","cependant","certain",
			"certaine","certaines","certains","certes","ces","cet","cette","ceux",
			"ceux-ci","ceux-là","chacun","chacune","chaque","cher","chers","chez",
			"chiche","chut","chère","chères","ci","cinq","cinquantaine",
			"cinquante","cinquantième","cinquième","clac","clic","combien","comme",
			"comment","comparable","comparables","compris","concernant","contre",
			"couic","crac","d","da","dans","de","debout","dedans","dehors","deja",
			"delà","depuis","dernier","derniere","derriere","derrière","des",
			"desormais","desquelles","desquels","dessous","dessus","deux",
			"deuxième","deuxièmement","devant","devers","devra","different",
			"differentes","differents","différent","différente","différentes",
			"différents","dire","directe","directement","dit","dite","dits",
			"divers","diverse","diverses","dix","dix-huit","dix-neuf","dix-sept",
			"dixième","doit","doivent","donc","dont","douze","douzième","dring",
			"du","duquel","durant","dès","désormais","e","effet","egale",
			"egalement","egales","eh","elle","elle-même","elles","elles-mêmes",
			"en","encore","enfin","entre","envers","environ","es","est","et",
			"etant","etc","etre","eu","euh","eux","eux-mêmes","exactement",
			"excepté","extenso","exterieur","f","fais","faisaient","faisant",
			"fait","façon","feront","fi","flac","floc","font","g","gens","h","ha",
			"hein","hem","hep","hi","ho","holà","hop","hormis","hors","hou","houp",
			"hue","hui","huit","huitième","hum","hurrah","hé","hélas","i","il",
			"ils","importe","j","je","jusqu","jusque","juste","k","l","la",
			"laisser","laquelle","las","le","lequel","les","lesquelles","lesquels",
			"leur","leurs","longtemps","lors","lorsque","lui","lui-meme","lui-même",
			"là","lès","m","ma","maint","maintenant","mais","malgre","malgré",
			"maximale","me","meme","memes","merci","mes","mien","mienne","miennes",
			"miens","mille","mince","minimale","moi","moi-meme","moi-même",
			"moindres","moins","mon","moyennant","multiple","multiples","même",
			"mêmes","n","na","naturel","naturelle","naturelles","ne","neanmoins",
			"necessaire","necessairement","neuf","neuvième","ni","nombreuses",
			"nombreux","non","nos","notamment","notre","nous","nous-mêmes",
			"nouveau","nul","néanmoins","nôtre","nôtres","o","oh","ohé","ollé",
			"olé","on","ont","onze","onzième","ore","ou","ouf","ouias","oust",
			"ouste","outre","ouvert","ouverte","ouverts","o|","où","p","paf",
			"pan","par","parce","parfois","parle","parlent","parler","parmi",
			"parseme","partant","particulier","particulière","particulièrement",
			"pas","passé","pendant","pense","permet","personne","peu","peut",
			"peuvent","peux","pff","pfft","pfut","pif","pire","plein","plouf",
			"plus","plusieurs","plutôt","possessif","possessifs","possible",
			"possibles","pouah","pour","pourquoi","pourrais","pourrait",
			"pouvait","prealable","precisement","premier","première",
			"premièrement","pres","probable","probante","procedant","proche",
			"près","psitt","pu","puis","puisque","pur","pure","q","qu","quand",
			"quant","quant-à-soi","quanta","quarante","quatorze","quatre",
			"quatre-vingt","quatrième","quatrièmement","que","quel","quelconque",
			"quelle","quelles","quelqu'un","quelque","quelques","quels","qui",
			"quiconque","quinze","quoi","quoique","r","rare","rarement","rares",
			"relative","relativement","remarquable","rend","rendre","restant",
			"reste","restent","restrictif","retour","revoici","revoilà","rien",
			"s","sa","sacrebleu","sait","sans","sapristi","sauf","se","sein",
			"seize","selon","semblable","semblaient","semble","semblent",
			"sent","sept","septième","sera","seraient","serait","seront","ses",
			"seul","seule","seulement","si","sien","sienne","siennes","siens",
			"sinon","six","sixième","soi","soi-même","soit","soixante","son",
			"sont","sous","souvent","specifique","specifiques","speculatif","stop"
			,"strictement","subtiles","suffisant","suffisante","suffit","suis",
			"suit","suivant","suivante","suivantes","suivants","suivre",
			"superpose","sur","surtout","t","ta","tac","tant","tardive","te",
			"tel","telle","tellement","telles","tels","tenant","tend","tenir",
			"tente","tes","tic","tien","tienne","tiennes","tiens","toc","toi",
			"toi-même","ton","touchant","toujours","tous","tout","toute",
			"toutefois","toutes","treize","trente","tres","trois","troisième",
			"troisièmement","trop","très","tsoin","tsouin","tu","té","u","un",
			"une","unes","uniformement","unique","uniques","uns","v","va","vais",
			"vas","vers","via","vif","vifs","vingt","vivat","vive","vives","vlan",
			"voici","voilà","vont","vos","votre","vous","vous-mêmes","vu","vé",
			"vôtre","vôtres","w","x","y","z","zut","à","â","ça","ès","étaient",
			"étais","était","étant","été","être","ô"
			]

PYBOT_ANSWER_GOOD = [
	"Mais oui mon biquet ! Là voilà :",
	"Bien sûr mon mimi, ça devrait être ça:",
	"Avec plaisir mon p'tiot. Tadaaaaaam:",
	"""Mazette, ça fait un bail que j'en avais pas entendu parlé !\n
	Tiens :""",
	"Bonjour p'tit! C'est ça que tu cherches?",
	"Ola Moussaillon! Voici ta destination:",
	"""Salut gamin, t'as bien poussé depuis le temps!\n
	Tiens, c'est juste là:"""
]

PYBOT_ANSWER_LOST = [
	"""Ca aurait été avec plaisir mon poussin, mais là je ne me souviens plus...\n
	demande moi autre chose!""",
	"""Oulala, je voudrais bien t'aider mais ça ne me revient pas !  
	Tu as une autre demande?""",
	"""Dediou j'ai la mémoire qui flanche! Une autre requête? """,
	"""Mouais, la boussole de jadis peine à trouver son chemin...\n
	T'as pas quelque chose de plus facile pour ton Pybot? """,
	"""Tu le fais exprès? Tu voulais me piéger? 
	Bah voilà, t'as gagné, j'en sais RIEN! """,
	"Entre nous...si je connais pas c'est que ça en vaut pas la peine!",
	"""Mais oui, ça me parle....PAS! 
	Désolé chou, va falloir me demander autre chose."""
]

PYBOT_ANSWER_GET_STORY = [
	"Hahahaaaa! Ca me rappelle bien des choses. Ecoute bien.",
	"Dis poussin, je t'ai déjà raconté cette histoire?",
	"Mais enfait, ça me fait penser.",
	"Nom d'un castor, j'ai des souvenirs qui remontent!",
	"Hop, hop, hop... t'en vas pas mon choupisson, j'ai des choses à te dire!",
	"Par la barbe de Merlin, j'ai eu un flash!",
	"Une encyclopédie je suis...écoute le vieux!"
]

PYBOT_ANSWER_NO_STORY = [
	"Fichtre! Je me souviens plus ce que je voulais te raconter...",
	"T'y crois toi? J'ai perdu le fil.",
	"""Sapristi, ça m'agace quand je perds la boule. 
	Je l'avais sur le bout de la langue mon histoire.""",
	"Psssst, tu veux dormir moins bête? Et bah non, reste bête ça te vas bien.",
	"Alors là, j'ai beau chercher, j'ai rien à ajouter...",
	"Voilà, voilà...parfois il faut savoir rester concis.",
	"""Ooooh la vie d'un pirate à bord d'une frégateeee, 
	c'est la plus belleeee des vies!\n Quand je ne sais plus quoi dire,
	je chante. Bécot.
	"""
]