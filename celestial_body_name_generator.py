import random
import string

GREEK_LETTERS = [
    "Alpha",
    "Beta",
    "Gamma",
    "Delta",
    "Epsilon",
    "Zeta",
    "Eta",
    "Theta",
    "Iota",
    "Kappa",
    "Lambda",
    "Mu",
    "Nu",
    "Xi",
    "Omicron",
    "Pi",
    "Rho",
    "Sigma",
    "Tau",
    "Upsilon",
    "Phi",
    "Chi",
    "Psi",
    "Omega"
]
DEITIES = [
    "Aphrodite",
    "Apollo",
    "Ares",
    "Artemis",
    "Athena",
    "Demeter",
    "Dionysus",
    "Hades",
    "Hephaestus",
    "Hera",
    "Hermes",
    "Hestia",
    "Poseidon",
    "Zeus"
]
PRIMORDIAL_DEITIES = [
    "Achlys",
    "Aion",
    "Aether",
    "Ananke",
    "Chaos",
    "Chronos",
    "Erebus",
    "Eros",
    "Hemera",
    "Hypnos",
    "Gaea",
    "Nemesis",
    "Nesoi",
    "Nyx",
    "Uranus",
    "Ourea",
    "Phanes",
    "Pontus",
    "Tartarus",
    "Thalassa",
    "Thanatos"
]
TITANS = [
    "Coeus",
    "Crius",
    "Cronus",
    "Hyperion",
    "Iapetus",
    "Mnemosyne",
    "Oceanus",
    "Phoebe",
    "Rhea",
    "Tethys",
    "Theia",
    "Themis",
    "Asteria",
    "Astraeus",
    "Atlas",
    "Aura",
    "Clymene",
    "Dione",
    "Helios",
    "Selene",
    "Eos",
    "Epimetheus",
    "Eurybia",
    "Eurynome",
    "Lelantos",
    "Leto",
    "Menoetius",
    "Metis",
    "Ophion",
    "Pallas",
    "Perses",
    "Prometheus",
    "Styx"
]
GIGANTES = [
    "Agrius",
    "Alcyoneus",
    "Chthonius",
    "Clytius",
    "Enceladus",
    "Ephialtes",
    "Eurymedon",
    "Eurytus",
    "Gration",
    "Hippolytus",
    "Leon",
    "Mimas",
    "Polybotes",
    "Porphyrion",
    "Thoon",
    "Otus",
    "Anax",
    "Antaeus",
    "Antiphates",
    "Argus Panoptes",
    "Asterius",
    "Cacus",
    "Cyclope",
    "Arges",
    "Brontes",
    "Steropes",
    "Polyphemus",
    "Geryon",
    "Hekatonkheir",
    "Briareus",
    "Cottus",
    "Gyges",
    "Orion",
    "Talos",
    "Tityos",
    "Typhon"
]
PERSONIFICATIONS = [
    "Adephagia",
    "Adikia",
    "Aergia",
    "Agathodaemon",
    "Agon",
    "Aidos",
    "Aisa",
    "Alala",
    "Alastor",
    "Aletheia",
    "Achos",
    "Ania",
    "Lupe",
    "Alke",
    "Amechania",
    "Anaideia",
    "Angelia",
    "Apate",
    "Apheleia",
    "Aporia",
    "Arete",
    "Ate",
    "Bia",
    "Caerus",
    "Corus",
    "Deimos",
    "Dikaiosyne",
    "Dike",
    "Dolos",
    "Dysnomia",
    "Dyssebeia",
    "Eirene",
    "Ekecheiria",
    "Eleos",
    "Elpis",
    "Epiphron",
    "Eris",
    "Anteros",
    "Hedylogos",
    "Hermaphroditus",
    "Himeros",
    "Hymenaeus",
    "Pothos",
    "Eucleia",
    "Eulabeia",
    "Eunomia",
    "Eupheme",
    "Eupraxia",
    "Eusebeia",
    "Euthenia",
    "Gelos",
    "Geras",
    "Harmonia",
    "Hebe",
    "Hedone",
    "Heimarmene",
    "Homados",
    "Homonoia",
    "Horkos",
    "Horme",
    "Hybris",
    "Ioke",
    "Kakia",
    "Kalokagathia",
    "Keres",
    "Koalemos",
    "Kratos",
    "Kydoimos",
    "Limos",
    "Lyssa",
    "Mania",
    "Moira",
    "Clotho",
    "Lachesis",
    "Atropos",
    "Momus",
    "Moros",
    "Nike",
    "Nomos",
    "Oizys",
    "Epiales",
    "Morpheus",
    "Phantasos",
    "Phobetor",
    "Palioxis",
    "Peitharchia",
    "Peitho",
    "Penia",
    "Penthus",
    "Pepromene",
    "Pheme",
    "Philophrosyne",
    "Philotes",
    "Phobos",
    "Phrike",
    "Phthonus",
    "Pistis",
    "Poine",
    "Polemos",
    "Ponos",
    "Poros",
    "Praxidike",
    "Proioxis",
    "Prophasis",
    "Ptocheia",
    "Roma",
    "Soter",
    "Soteria",
    "Sophrosyne",
    "Techne",
    "Thrasos",
    "Tyche",
    "Zelos"
]
CHTHONIC_DEITIES = [
    "Amphiaraus",
    "Angelos",
    "Askalaphos",
    "Cerberus",
    "Charon",
    "Empusa",
    "Erebos",
    "Alecto",
    "Tisiphone",
    "Megaera",
    "Hecate",
    "Aiakos",
    "Minos",
    "Rhadamanthys",
    "Keuthonymos",
    "Lamia",
    "Lampade",
    "Gorgyra",
    "Orphne",
    "Macaria",
    "Melinoe",
    "Menoetes",
    "Mormo",
    "Persephone",
    "Acheron",
    "Kokytos",
    "Lethe",
    "Phlegethon"
]
SEA_DEITIES = [
    "Aegaeon",
    "Achelous",
    "Amphitrite",
    "Benthesikyme",
    "Brizo",
    "Ceto",
    "Charybdis",
    "Cymopoleia",
    "Delphin",
    "Eidothea",
    "Glaucus",
    "Stheno",
    "Euryale",
    "Medusa",
    "Deino",
    "Enyo",
    "Pemphredo",
    "Harpy",
    "Aello",
    "Ocypete",
    "Podarge",
    "Nicothoe",
    "Hippocampi",
    "Bythos",
    "Aphros",
    "Karkinos",
    "Ladon",
    "Leucothea",
    "Nereide",
    "Thetis",
    "Arethusa",
    "Galene",
    "Psamathe",
    "Nereus",
    "Nerites",
    "Nilus",
    "Palaemon",
    "Phorcys",
    "Pontos",
    "Proteus",
    "Sangarius",
    "Scylla",
    "Siren",
    "Aglaope",
    "Himerope",
    "Leucosia",
    "Ligeia",
    "Molpe",
    "Parthenope",
    "Peisithoe",
    "Raidne",
    "Teles",
    "Thelchtereia",
    "Thelxiope",
    "Actaeus",
    "Argyron",
    "Atabyrius",
    "Chalcon",
    "Chryson",
    "Damon",
    "Damnameneus",
    "Dexithea",
    "Lycos",
    "Lysagora",
    "Makelo",
    "Megalesius",
    "Mylas",
    "Nikon",
    "Ormenos",
    "Simon",
    "Skelmis",
    "Thaumas",
    "Thoosa",
    "Triteia",
    "Triton"
]
SKY_DEITIES = [
    "Achelois",
    "Aeolus",
    "Alectrona",
    "Aparctias",
    "Apheliotes",
    "Argestes",
    "Caicias",
    "Circios",
    "Euronotus",
    "Lips",
    "Skeiron",
    "Arke",
    "Astraios",
    "Stilbon",
    "Eosphorus",
    "Hesperus",
    "Pyroeis",
    "Phaethon",
    "Phaenon",
    "Chione",
    "Sabazios",
    "Selene ",
    "Men",
    "Hesperide",
    "Iris",
    "Nephelai",
    "Pandia",
    "Ersa",
    "Boreas",
    "Eurus",
    "Notus",
    "Zephyrus",
    "Alcyone",
    "Sterope",
    "Electra",
    "Maia",
    "Merope",
    "Taygete"
]
RUSTIC_DEITIES = [
    "Aetna",
    "Amphictyonis",
    "Anthousai",
    "Britomartis",
    "Aitnaios",
    "Alkon",
    "Onnes",
    "Tonnes",
    "Centaur",
    "Chariclo",
    "Chiron",
    "Eurytion",
    "Nessus",
    "Pholus",
    "Akmon",
    "Passalos",
    "Chloris",
    "Comus",
    "Corymbus",
    "Cybele",
    "Dindymene",
    "Acmon",
    "Delas",
    "Epimedes",
    "Iasios",
    "Kelmis",
    "Skythes",
    "Titias",
    "Cyllenus",
    "Dryade",
    "Gaia",
    "Hecaterus",
    "Thallo",
    "Auxo",
    "Karpo",
    "Pherousa",
    "Euporie",
    "Orthosie",
    "Auge",
    "Anatole",
    "Musica",
    "Gymnastica",
    "Nymphe",
    "Mesembria",
    "Sponde",
    "Elete",
    "Cypris",
    "Hesperis",
    "Dysis",
    "Arktos",
    "Eiar",
    "Theros",
    "Pthinoporon",
    "Cheimon",
    "Damneus",
    "Idaios",
    "Kyrbas",
    "Okythoos",
    "Prymneus",
    "Pyrrhichos",
    "Ma",
    "Methe",
    "Meliae",
    "Daphne",
    "Metope",
    "Minthe",
    "Hekaerge",
    "Loxo",
    "Oupis",
    "Adrasteia",
    "Echo",
    "Idyia",
    "Pan",
    "Acis",
    "Alpheus",
    "Asopus",
    "Cladeus",
    "Cocytus",
    "Peneus",
    "Scamander",
    "Priapus",
    "Satyr",
    "Krotos",
    "Silenus",
    "Telete",
    "Zagreus"
]
AGRICULTURAL_DEITIES = [
    "Adonis",
    "Aphaea",
    "Carme",
    "Carmanor",
    "Chrysothemis",
    "Cyamites",
    "Despoina",
    "Philomelus",
    "Plutus",
    "Triptolemus"
]
HEALTH_DEITIES = [
    "Aceso",
    "Aegle",
    "Epione",
    "Hygieia",
    "Iaso",
    "Panacea",
    "Telesphorus"
]
OTHER_DEITIES = [
    "Acratopotes",
    "Adrastea",
    "Agdistis",
    "Alexiares",
    "Anicetus",
    "Aphroditus",
    "Astraea",
    "Auxesia",
    "Charites",
    "Aglaea",
    "Euphrosyne",
    "Hegemone",
    "Antheia",
    "Pasithea",
    "Cleta",
    "Phaenna",
    "Eudaimonia",
    "Euthymia",
    "Calleis",
    "Paidia",
    "Pandaisia",
    "Pannychis",
    "Ceraon",
    "Chrysus",
    "Circe",
    "Syntribos",
    "Smaragos",
    "Asbetos",
    "Sabaktes",
    "Omodamos",
    "Deipneus",
    "Eiresione",
    "Eileithyia",
    "Enyalius",
    "Glycon",
    "Harpocrates",
    "Hymenaios",
    "Ichnaea",
    "Iynx",
    "Matton",
    "Aoide",
    "Arche",
    "Melete",
    "Mneme",
    "Thelxinoe",
    "Calliope",
    "Clio",
    "Euterpe",
    "Melpomene",
    "Polyhymnia",
    "Terpsichore",
    "Thalia",
    "Urania",
    "Cephisso",
    "Apollonis",
    "Borysthenis",
    "Hypate",
    "Mese",
    "Nete",
    "Polymatheia",
    "Palaestra",
    "Rhapso",
    "Taraxippus"
]
DEIFIED_MORTALS = [
    "Alabandus",
    "Aristaeus",
    "Asclepius",
    "Attis",
    "Bolina",
    "Pollux",
    "Endymion",
    "Hemithea",
    "Heracles",
    "Lampsace",
    "Ino",
    "Tenes",
    "Hilaera",
    "Phylonoe",
    "Psyche",
    "Semele"
]
HEROES = [
    "Abderus",
    "Achilles",
    "Aeneas",
    "Ajax",
    "Amphitryon",
    "Antilochus",
    "Bellerophon",
    "Castor",
    "Chrysippus",
    "Daedalus",
    "Diomedes",
    "Eleusis",
    "Eunostus",
    "Ganymede",
    "Hector",
    "Icarus",
    "Iolaus",
    "Jason",
    "Meleager",
    "Odysseus",
    "Orpheus",
    "Pandion",
    "Perseus",
    "Theseus"
]
WOMEN = [
    "Alcestis",
    "Andromache",
    "Andromeda",
    "Antigone",
    "Arachne",
    "Ariadne",
    "Atalanta",
    "Briseis",
    "Caeneus",
    "Cassiopeia",
    "Clytemnestra",
    "Danae",
    "Deianeira",
    "Europa",
    "Hecuba",
    "Helen",
    "Hermione",
    "Iphigenia",
    "Ismene",
    "Jocasta",
    "Medea",
    "Niobe",
    "Pandora",
    "Penelope",
    "Phaedra",
    "Polyxena",
    "Thrace"
]
KINGS = [
    "Abas",
    "Acastus",
    "Acrisius",
    "Admetus",
    "Adrastus",
    "Aeacus",
    "Aeetes",
    "Aegeus",
    "Aegimius",
    "Aegisthus",
    "Aegyptus",
    "Aeson",
    "Aethlius",
    "Aetolus",
    "Agamemnon",
    "Agasthenes",
    "Agenor",
    "Alcinous",
    "Alcmaeon",
    "Aleus",
    "Amphictyon",
    "Amphion",
    "Zethus",
    "Amycus",
    "Anaxagoras",
    "Anchises",
    "Arcesius",
    "Argeus",
    "Argus",
    "Assaracus",
    "Asterion",
    "Athamas",
    "Atreus",
    "Augeas",
    "Autesion",
    "Bias",
    "Busiris",
    "Cadmus",
    "Car",
    "Catreus",
    "Cecrops",
    "Ceisus",
    "Celeus",
    "Cephalus",
    "Cepheus",
    "Charnabon",
    "Cinyras",
    "Codrus",
    "Corinthus",
    "Cranaus",
    "Creon",
    "Cres",
    "Cresphontes",
    "Cretheus",
    "Criasus",
    "Cylarabes",
    "Cynortas",
    "Cyzicus",
    "Danaus",
    "Dardanus",
    "Deiphontes",
    "Demophon",
    "Echemus",
    "Echetus",
    "Eetion",
    "Electryon",
    "Elephenor",
    "Epaphus",
    "Epopeus",
    "Erechtheus",
    "Erginus",
    "Erichthonius",
    "Eteocles",
    "Eurotas",
    "Eurystheus",
    "Euxantius",
    "Gelanor",
    "Haemus",
    "Helenus",
    "Hippothoon",
    "Hyrieus",
    "Ilus",
    "Ixion",
    "Laertes",
    "Laomedon",
    "Lycaon",
    "Lycurgus",
    "Makedon",
    "Megareus",
    "Melampus",
    "Melanthus",
    "Memnon",
    "Menelaus",
    "Menestheus",
    "Midas",
    "Myles",
    "Nestor",
    "Nycteus",
    "Oebalus",
    "Oedipus",
    "Oeneus",
    "Oenomaus",
    "Oenopion",
    "Ogygus",
    "Oicles",
    "Oileus",
    "Orestes",
    "Oxyntes",
    "Peleus",
    "Pelias",
    "Pelops",
    "Pentheus",
    "Periphas",
    "Phineus",
    "Phlegyas",
    "Phoenix",
    "Phoroneus",
    "Phyleus",
    "Pirithoos",
    "Pittheus",
    "Polybus",
    "Polynices",
    "Priam",
    "Proetus",
    "Pylades",
    "Rhesus",
    "Sarpedon",
    "Sisyphus",
    "Sithon",
    "Talaus",
    "Tegyrios",
    "Telamon",
    "Telephus",
    "Temenus",
    "Teucer",
    "Teutamides",
    "Teuthras",
    "Thersander",
    "Thyestes",
    "Tisamenus",
    "Tyndareus"
]
ORACLES = [
    "Amphilochus",
    "Anius",
    "Asbolus",
    "Bakis",
    "Branchus",
    "Calchas",
    "Carnus",
    "Carya",
    "Cassandra",
    "Ennomus",
    "Halitherses",
    "Iamus",
    "Idmon",
    "Manto",
    "Mopsus",
    "Polyeidos",
    "Pythia",
    "Telemus",
    "Theoclymenus",
    "Tiresias"
]
AMAZONS = [
    "Aegea",
    "Aella",
    "Alcibie",
    "Antandre",
    "Antiope",
    "Areto",
    "Bremusa",
    "Celaeno",
    "Eurypyle",
    "Hippolyta",
    "Hippothoe",
    "Iphito",
    "Lampedo",
    "Marpesia",
    "Melanippe",
    "Molpadia",
    "Myrina",
    "Orithyia",
    "Otrera",
    "Pantariste",
    "Penthesilea",
    "Thalestris"
]
INMATES_OF_TARTARUS = [
    "Hypermnestra",
    "Gorgophone",
    "Automate",
    "Amymone",
    "Agave",
    "Scaea",
    "Hippodamia",
    "Rhodia",
    "Cleopatra",
    "Glauce",
    "Hippomedusa",
    "Gorge",
    "Iphimedusa",
    "Rhode",
    "Pirene",
    "Dorion",
    "Phartis",
    "Mnestra",
    "Evippe",
    "Anaxibia",
    "Nelo",
    "Clite",
    "Sthenele",
    "Chrysippe",
    "Autonoe",
    "Theano",
    "Eurydice",
    "Glaucippe",
    "Antheleia",
    "Cleodore",
    "Erato",
    "Stygne",
    "Bryce",
    "Actaea",
    "Podarce",
    "Dioxippe",
    "Adite",
    "Pylarge",
    "Hippodice",
    "Adiante",
    "Callidice",
    "Oeme",
    "Hyperippe"
    "Ixion",
    "Tantalus"
]


def star_names():
    return DEITIES + PRIMORDIAL_DEITIES + GIGANTES + KINGS + AMAZONS


def planet_names():
    return TITANS + GIGANTES + CHTHONIC_DEITIES + SEA_DEITIES + AGRICULTURAL_DEITIES + HEROES


def satellite_names():
    return PERSONIFICATIONS + SKY_DEITIES + OTHER_DEITIES + ORACLES


def asteroid_names():
    return PERSONIFICATIONS + RUSTIC_DEITIES + OTHER_DEITIES + DEIFIED_MORTALS


def comet_names():
    return RUSTIC_DEITIES + HEALTH_DEITIES + WOMEN + INMATES_OF_TARTARUS


def generate_star_name():
    name = random.choice(star_names())
    letter = random.choice(GREEK_LETTERS)
    return "{0} {1}".format(name, letter)


def generate_planet_name():
    name = random.choice(planet_names())
    return "{0}".format(name)


def generate_planet_name_by_star(star_name):
    number = random.choice(range(1, 20))
    return "{0} ({1} — {2})".format(generate_planet_name(), star_name, number)


def generate_satellite_name():
    name = random.choice(satellite_names())
    letter = random.choice(string.ascii_uppercase)
    number = random.choice(range(1, 50))
    return "{0} {1}{2}".format(name, number, letter)


def generate_asteroid_name():
    name = random.choice(asteroid_names())
    letter = random.choice(string.ascii_uppercase)
    number = random.choice(range(1000, 9999))
    return "{0} {1}-{2}".format(name, letter, number)


def generate_comet_name():
    name = random.choice(comet_names())
    number = random.choice(range(1, 100))
    letter = random.choice(string.ascii_uppercase)
    return "{0}{1}/{2}".format(number, letter, name)


print("Star: {0}".format(generate_star_name()))
print("Planet: {0}".format(generate_planet_name_by_star(generate_star_name())))
print("Satellite: {0}".format(generate_satellite_name()))
print("Asteroid: {0}".format(generate_asteroid_name()))
print("Comet: {0}".format(generate_comet_name()))
