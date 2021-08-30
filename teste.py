from pymongo import MongoClient
from config import mongoURI

def get_database():
    CONNECTION_STRING = mongoURI
    client = MongoClient(CONNECTION_STRING)
    return client['Loja']

if __name__ == '__main__':
    dbname = get_database()
    collection_func = dbname["Funcionarios"]
    collection_cli = dbname["Clientes"]
    collection_acess = dbname["Acessos"]
    collection_cc = dbname['CartoesCadastrados']

    funcionarios = [
		{	"_id": "p001",
			"namefirst": "Roman",
			"namelast": "Cilano",
			"birthdate": "1997-09-20",
			"email": "dripsAlishasSouthwest@minnowsLeandersexcoriated.org"
		},
		{
			"_id": "p002",
			"namefirst": "Tanner",
			"namelast": "Rugerio",
			"birthdate": "1976-09-04",
			"email": "bandoleersgrime@splotchy.net"
		},
		{
			"_id": "p003",
			"namefirst": "Armand",
			"namelast": "Mansky",
			"birthdate": "1971-09-02",
			"email": "liartrippinggruffed@Capuletsventurerime.edu"
		},
		{
			"_id": "p004",
			"namefirst": "Deangelo",
			"namelast": "Scriver",
			"birthdate": "1987-07-20",
			"email": "Catawbaslewdest@Cyprusjousted.org"
		},
		{	"_id": "p005",
			"namefirst": "Darrell",
			"namelast": "Abdel",
			"birthdate": "1999-07-08",
			"email": "fixationaged@fruitcakesPelesunprivileged.info"
		},
		{
			"_id":"p006",
			"namefirst": "Yong",
			"namelast": "Camm",
			"birthdate": "1982-09-02",
			"email": "tantrumsgayetys@CorneilleErFijis.gov"
		},
		{
			"_id": "p007",
			"namefirst": "Colin",
			"namelast": "Cifarelli",
			"birthdate": "2000-01-11",
			"email": "flourishesAchesons@acousticss.edu"
		},
		{
			"_id":"p008",
			"namefirst": "Wilber",
			"namelast": "Goldthwait",
			"birthdate": "1977-06-03",
			"email": "transittingnitrogens@Macmillanphenomenally.info"
		},
		{
			"_id": "p009",
			"namefirst": "Miguel",
			"namelast": "Worth",
			"birthdate": "1993-12-12",
			"email": "turbulentbrainlessextrasensory@consultantsunplumbed.gov"
		},
		{
			"_id": "p010",
			"namefirst": "Garry",
			"namelast": "Sennet",
			"birthdate": "1995-03-02",
			"email": "syndromeslevered@incisors.org"
		},
		{
			"_id": "p011",
			"namefirst": "Dylan",
			"namelast": "Hardegree",
			"birthdate": "2018-05-31",
			"email": "dandythrowpathologists@Eurasianleaningshouts.gov"
		},
		{	"_id": "p012",
			"namefirst": "Troy",
			"namelast": "Amdahl",
			"birthdate": "1994-04-14",
			"email": "sawarbitratorsépées@midairsdalmatian.info"
		},
		{
			"_id": "p013",
			"namefirst": "Reyes",
			"namelast": "Maclain",
			"birthdate": "1977-09-17",
			"email": "howitzeractivisms@dwarves.com"
		},
		{
			"_id": "p014",
			"namefirst": "Numbers",
			"namelast": "Ogston",
			"birthdate": "2013-12-19",
			"email": "smeltersbadmouthing@Byersoverpopulatedpenultimates.gov"
		},
		{
			"_id": "p015",
			"namefirst": "Danny",
			"namelast": "Weiher",
			"birthdate": "2013-03-10",
			"email": "joggersgallbladders@spankingsflibbertigibbets.edu"
		},
		{
			"_id": "p016",
			"namefirst": "Simon",
			"namelast": "Mccune",
			"birthdate": "2013-11-12",
			"email": "backbonesphilologys@pedantic.net"
		},
		{
			"_id": "p017",
			"namefirst": "Norman",
			"namelast": "Stivers",
			"birthdate": "1973-01-30",
			"email": "washtubsspearing@pitchmanwillpowers.net"
		},
		{
			"_id": "p018",
			"namefirst": "Arnoldo",
			"namelast": "Tush",
			"birthdate": "2016-02-02",
			"email": "controvert@coordinate.info"
		},
		{
			"_id": "p019",
			"namefirst": "Rodrick",
			"namelast": "Mcleon",
			"birthdate": "2002-09-09",
			"email": "armadasconsensuses@techniquecancelled.gov"
		},
		{
			"_id": "p020",
			"namefirst": "Marlon",
			"namelast": "Bucklen",
			"birthdate": "2006-07-01",
			"email": "goddaughterBatesrabbits@warpingpolyethylene.com"
		}]

    acessos = [
		{
			"username": "interrupting",
			"password": "!aj`~KF6\"^*6lQv;",
			"acesso_ativo": "False",
			"ultimo_acesso": "2014-03-11 22:08:44.476259"
		},
		{
			"username": "garbsloavesswalruses",
			"password": "bK.}f!lxZDz*|@?g",
			"acesso_ativo": "True",
			"ultimo_acesso": "2001-11-07 03:00:30.049724"
		},
		{
			"username": "confidinggainsaying",
			"password": "rp='Rrl\\<>!Exn*(",
			"acesso_ativo": "False",
			"ultimo_acesso": "1995-06-29 08:06:31.077515"
		},
		{
			"username": "clientsrocks",
			"password": "zZ~+.U`#xnx'C'X#",
			"acesso_ativo": "False",
			"ultimo_acesso": "2019-10-06 05:03:24.441018"
		},
		{
			"username": "narking",
			"password": "CgWESE#.-Fj,Ry*x",
			"acesso_ativo": "False",
			"ultimo_acesso": "2018-03-01 08:54:39.123476"
		},
		{
			"username": "gracefullest",
			"password": "w}Qd`C^yKatdnQ:}",
			"acesso_ativo": "False",
			"ultimo_acesso": "1985-05-06 02:12:09.315936"
		},
		{
			"username": "warinesssoptometrists",
			"password": "2yg_|8vhq\\v!.28q",
			"acesso_ativo": "True",
			"ultimo_acesso": "1990-11-02 11:33:52.771529"
		},
		{
			"username": "immensity",
			"password": "OG&W+<Oi!4rw-8u)",
			"acesso_ativo": "False",
			"ultimo_acesso": "1975-02-02 03:54:36.555082"
		},
		{
			"username": "corkMichelunsmiling",
			"password": "f.5n'H<D2$V5\"_ey",
			"acesso_ativo": "True",
			"ultimo_acesso": "1999-06-05 02:39:06.071748"
		},
		{
			"username": "Galateacrystallographic",
			"password": "~XBtoPs$===YAE={",
			"acesso_ativo": "False",
			"ultimo_acesso": "2006-09-29 05:01:47.269480"
		},
		{
			"username": "mercerize",
			"password": ")=S(VC,<$Sv.,f#V",
			"acesso_ativo": "False",
			"ultimo_acesso": "2019-03-24 21:57:53.256489"
		},
		{
			"username": "bionic",
			"password": "OkFWE5|'71*@%%k`",
			"acesso_ativo": "False",
			"ultimo_acesso": "1983-10-03 11:23:37.835049"
		},
		{
			"username": "meltdownslitterbugs",
			"password": ";{AlYOAe|5m_pF}:",
			"acesso_ativo": "False",
			"ultimo_acesso": "2012-08-07 00:07:29.916308"
		},
		{
			"username": "heretoendows",
			"password": "P[|,7.;#FN]^+LkF",
			"acesso_ativo": "True",
			"ultimo_acesso": "1985-04-10 10:12:22.506244"
		},
		{
			"username": "weighingjointing",
			"password": "U#~i8G)P8ac<ZTT~",
			"acesso_ativo": "False",
			"ultimo_acesso": "2006-10-08 15:36:56.566893"
		}
	]

    clientes = [
		{
			"namefirst": "Mose",
			"namelast": "Schelble",
			"sex": "Female",
			"email": "batikspringyphysicians@miniaturists.org",
			"age": "85",
			"address": "4258 Civic Center Ln",
			"city": "Tempe",
			"country": "Mexico"
		},
		{
			"namefirst": "Johnathan",
			"namelast": "Pappadakis",
			"sex": "Female",
			"email": "weaknessesstethoscopes@virusskabobsPsyches.me",
			"age": "51",
			"address": "2061 Lyman Ln",
			"city": "Warren",
			"country": "Guinea-Bissau"
		},
		{
			"namefirst": "Dale",
			"namelast": "Helps",
			"sex": "Male",
			"email": "amendmentsimpietys@rebatesjaguar.edu",
			"age": "2",
			"address": "9848 Imperial Ct",
			"city": "Pueblo",
			"country": "India"
		},
		{
			"namefirst": "Brooks",
			"namelast": "Bearry",
			"sex": "Male",
			"email": "reptiledisentangledcommissioning@conflictinglingerers.info",
			"age": "47",
			"address": "1537 Smith Trl",
			"city": "Frisco",
			"country": "Saint Helena"
		},
		{
			"namefirst": "Isiah",
			"namelast": "Tesky",
			"sex": "Male",
			"email": "Tanzanias@cottersrectorys.gov",
			"age": "36",
			"address": "7925 Archer Trl",
			"city": "Vallejo",
			"country": "Croatia"
		},
		{
			"namefirst": "Brendan",
			"namelast": "Bangs",
			"sex": "Male",
			"email": "infieldshideaway@chockedshotguns.edu",
			"age": "63",
			"address": "3358 Madison St",
			"city": "Escondido",
			"country": "Paracel Islands"
		},
		{
			"namefirst": "Ambrose",
			"namelast": "Kleyman",
			"sex": "Male",
			"email": "castratehighways@alluviummoleskin.org",
			"age": "80",
			"address": "624 Oak Pass Blvd",
			"city": "Orlando",
			"country": "Zambia"
		},
		{
			"namefirst": "Teodoro",
			"namelast": "Barsamian",
			"sex": "Female",
			"email": "AsamasrendOshkoshs@prudethatsaddensbullish.me",
			"age": "3",
			"address": "3198 Pamela St",
			"city": "El Paso",
			"country": "Estonia"
		},
		{
			"namefirst": "Domenic",
			"namelast": "Baghdassarian",
			"sex": "Female",
			"email": "YahtzeesPete@enoughOzarkweakly.info",
			"age": "90",
			"address": "5973 Lambsdowne Blvd",
			"city": "Fullerton",
			"country": "Brunei"
		},
		{
			"namefirst": "Wallace",
			"namelast": "Shigaki",
			"sex": "Female",
			"email": "hoodlumsArizonian@mendicants.net",
			"age": "72",
			"address": "5749 600 Ct",
			"city": "Jackson",
			"country": "Malaysia"
		},
		{
			"namefirst": "Billy",
			"namelast": "Morente",
			"sex": "Male",
			"email": "Schillertepees@corrugatesdogmasOdessas.org",
			"age": "20",
			"address": "7325 Dalemere Ave",
			"city": "Ann Arbor",
			"country": "Ghana"
		},
		{
			"namefirst": "Darius",
			"namelast": "Kimmell",
			"sex": "Female",
			"email": "laceSommesember@popularizationsspreading.net",
			"age": "103",
			"address": "2034 Hailstorm Ct",
			"city": "Thornton",
			"country": "Somalia"
		},
		{
			"namefirst": "Donnie",
			"namelast": "Dunlavey",
			"sex": "Female",
			"email": "slenderestelasticdigitizes@Sergiointimidates.com",
			"age": "25",
			"address": "1168 Deep Canyon Trl",
			"city": "Naperville",
			"country": "Malta"
		},
		{
			"namefirst": "Maxwell",
			"namelast": "Paulis",
			"sex": "Male",
			"email": "tuberculousmegalith@swivelingunderstaffed.net",
			"age": "4",
			"address": "5239 Mary Trl",
			"city": "Lansing",
			"country": "Solomon Islands"
		},
		{
			"namefirst": "Santo",
			"namelast": "Kaprelian",
			"sex": "Male",
			"email": "plectraimaginescigarillos@Turinsdittobullfrog.net",
			"age": "21",
			"address": "8417 Peavine Rd",
			"city": "Oxnard",
			"country": "Turkey"
		},
		{
			"namefirst": "Merlin",
			"namelast": "Barcheski",
			"sex": "Male",
			"email": "pitchforkedevangelisms@fuzzesquashes.gov",
			"age": "66",
			"address": "1955 Kimberly Ln",
			"city": "Salem",
			"country": "Madagascar"
		},
		{
			"namefirst": "Julio",
			"namelast": "Laroya",
			"sex": "Female",
			"email": "grabbergeophysical@sprayerpalindromic.gov",
			"age": "28",
			"address": "6692 Cousteau St",
			"city": "Provo",
			"country": "Samoa"
		},
		{
			"namefirst": "Milan",
			"namelast": "Szydlik",
			"sex": "Male",
			"email": "picaskatesbackstabbing@ingestions.me",
			"age": "58",
			"address": "2746 Smokey Hill Ave",
			"city": "Seattle",
			"country": "Mayotte"
		},
		{
			"namefirst": "Rocco",
			"namelast": "Biebl",
			"sex": "Female",
			"email": "ordinarilyrotes@boisterously.org",
			"age": "89",
			"address": "3702 Plattsburg Trl",
			"city": "Dallas",
			"country": "Samoa"
		},
		{
			"namefirst": "Ignacio",
			"namelast": "Schweikart",
			"sex": "Male",
			"email": "Fuzhousmisidentify@furnaces.com",
			"age": "70",
			"address": "4311 Corrinado St",
			"city": "Lexington",
			"country": "Solomon Islands"
		}
	]

    cartoes_credito = [
		{
			"creditcard": "7912-6405-7936-7817",
			"data_cadastro": "1971-08-31",
			"ativo": "True"
		},
		{
			"creditcard": "2885-7900-3197-7268",
			"data_cadastro": "2020-11-19",
			"ativo": "False"
		},
		{
			"creditcard": "5923-8631-3969-0473",
			"data_cadastro": "1993-07-01",
			"ativo": "True"
		},
		{
			"creditcard": "2773-9974-6649-9610",
			"data_cadastro": "1985-11-26",
			"ativo": "False"
		},
		{
			"creditcard": "4383-0460-4319-1450",
			"data_cadastro": "2019-09-10",
			"ativo": "False"
		},
		{
			"creditcard": "8372-6260-8723-1436",
			"data_cadastro": "2012-04-28",
			"ativo": "True"
		},
		{
			"creditcard": "7882-4258-3183-4845",
			"data_cadastro": "2021-05-21",
			"ativo": "False"
		},
		{
			"creditcard": "4619-9309-5418-5526",
			"data_cadastro": "1995-08-30",
			"ativo": "True"
		},
		{
			"creditcard": "5756-7971-4945-9404",
			"data_cadastro": "2007-12-09",
			"ativo": "False"
		},
		{
			"creditcard": "1518-9322-1194-3852",
			"data_cadastro": "1977-01-21",
			"ativo": "False"
		},
		{
			"creditcard": "2406-3869-9333-3558",
			"data_cadastro": "1982-04-01",
			"ativo": "False"
		},
		{
			"creditcard": "7261-2636-3559-4186",
			"data_cadastro": "2000-04-23",
			"ativo": "False"
		},
		{
			"creditcard": "6850-1687-0990-9268",
			"data_cadastro": "2005-08-31",
			"ativo": "True"
		},
		{
			"creditcard": "7200-2897-5881-9549",
			"data_cadastro": "1994-11-05",
			"ativo": "False"
		},
		{
			"creditcard": "5763-6795-4519-2826",
			"data_cadastro": "2001-05-27",
			"ativo": "True"
		},
		{
			"creditcard": "8192-8557-3029-5267",
			"data_cadastro": "1992-03-19",
			"ativo": "False"
		},
		{
			"creditcard": "7960-0819-6053-2274",
			"data_cadastro": "1973-12-08",
			"ativo": "True"
		},
		{
			"creditcard": "4185-9195-1265-2768",
			"data_cadastro": "1993-01-26",
			"ativo": "True"
		},
		{
			"creditcard": "6006-4502-1975-8050",
			"data_cadastro": "2001-04-17",
			"ativo": "False"
		},
		{
			"creditcard": "8121-5009-5645-8750",
			"data_cadastro": "1974-02-12",
			"ativo": "False"
		}
	]

    for idx, cliente in enumerate(clientes):
        cliente['_id'] = f'c{idx + 1:0>3d}'
    
    for idx in range(10):
        cartoes_credito[idx]['_id'] = f'cc{idx + 1:0>3d}'

    # collection_name.insert_one(item_3) # insere um item
    collection_func.insert_many(funcionarios) # insere vários
    collection_cli.insert_many(clientes)
    collection_acess.insert_many(acessos)
    collection_cc.insert_many(cartoes_credito)
    print('Documentos inseridos!')

