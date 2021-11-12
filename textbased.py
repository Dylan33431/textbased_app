def start():
    print("\nDit is een textbased applicatie gemaakt voor het bedrijf vluchtelingen werk. Het is gemaakt door Dylan van Ling SD1A.Als u de app wilt starten type start of als u app wilt sluiten type exit")

    answer = input(">")

    if "start" in answer:
        name()
    elif "exit" in answer:
        exit()
    else:
        restart("\nType start om de app te starten. Type exit om de app te verlaten\n")

def name():
    print("\nWelkom, dit word jou eigen verhaal. We willen een naam voor de caracter van dit verhaalt.")
    naam = input("\nNaam >")
    print("\nWelkom " + naam)
    keuzen_1()

def keuzen_1():
    print("\nu woont in een rustig land, je hebt een goede baan aan de rand van de stad in de media industrie en bent ook een belangerijk person met veel invloed op het publiek. Je werdt waker op een dag Maar zag op tv dat er een burger oorlog uit beekt. U heeft in die midag een praat programa waar u in zit en u neemt een beslising. Keuzen 1: Om naar het program te gaan en het gafaar hebben dat de bruger oorlog sneller ontwikeld dan je verwacht heb.  Keuzen 2: niet te gaan en afwachten hoe het gaat met de  burger oorlog.")
    print("\nKies én keuzen, type de nummer van je keuzen om je keuzen te kiezen.")
    answer = input(">")
    if "1" in answer:
        Lkeuzen_1_1()
    elif "2" in answer:
        RKeuzen_1_2()
    else:
        print("\nType 1 of 2 in\n")
        keuzen_1()


def Lkeuzen_1_1():
    print("\nU heeft net ontbeten en bent opweg naar je werk. Je hebt de radio aan en hoort dat de burger oorlog al heel groot geworden. U denkt er over om niet naar je werk te gaan want u denkt dat het te gevaarlijk is om er heen te gaan. keuzen 1: u blijft naar je werk gaan en de dag zoals normaal verder gaan. keuzen 2: u neemt de keuzen om niet naar werk te gaan en u gaat naar huis om daar het nieuws in de gaten houden.")
    answer = input(">")
    if "1" in answer:
        Lkeuzen_2_1()
    else:
        print("\nType 1 of 2 in\n")
        Lkeuzen_1_1()

def Lkeuzen_2_1():
    print("\nU gaat verder naar je werk. na een half uur met de auto bent u eindelijk op je werk. je programa word veranderd en je gaat nu over de burger oorlog praten en je mening er over geven. Je weet nog niet zo veel van de burger oorlog en vraagt aan je colega’s wat hun er van weten en wat ze er van vinden. U weet er nu wat meer van er bedenkt of het wel handig is om er over te praten. Keuzen 1: je gaat er over praten en je mening geven. Keuzen 2: zegen tegen je colega’s dat je er liever niet over wil praten omdat je bang bent om een verkerde mening te geven.")
    answer = input(">")
    if "1" in answer:
        Lkeuzen_3_1()
    else:
        print("\nType 1 of 2 in\n")
        Lkeuzen_2_1()

def Lkeuzen_3_1():
    print("\nJe vertelt tegen je colega’s dat je er liever niet over wil praten. Ze zegen tegen je dat je niet bang moet zijn over je mening te geven maar blijft bij de keuzen dat je er niet over wil praten. Je blijft wel bij de film crew van het programa maar blijft gewoon toekijken hoe andere mensen er over praten. Na het programa ga je nog even lunchen met je colega’s en ga je weer terug naar huis. Je hoort via de radio dat de burger oorlog steeds dichter bij je stad komt. Keuzen 1: je blijft in de stad waar iedereen die je kent is en waar je de beurt kent. Keuzen 2: je wilt de stad verlaten en gaat planen maken om de stad te verlaten om ergen veilig te komen.")
    answer = input(">")
    if "1" in answer:
        Lkeuzen_4_1()
    elif "2" in answer:
        RKeuzen_2_2()
    else:
        print("\nType 1 of 2 in\n")
        Lkeuzen_3_1()

def Lkeuzen_4_1():
    print("\nJe neemt de keuzen om in je stad te blijven en blijft verder rijden naar je huis. Je bent thuis en wilt gaat eten maar ziet in de koelkast dat je geen eten meer heb. Je loopt naar de winkel toe en je hoort je buren praten dat ze uit de stad gaan om een veilige plek te zoeken. Je vraagt aan hun of ze denken dat de burger oorlog naar de stad gaan komen. Ze zegen dat hun familie in de stad naast de stad waar jij woont. Dat ze al een beetje me de oorlog te maken hebben. Hun familie heeft tegen hun gezegt dat het verstandig je om uit de stad te gaan en naar een veilig stad/lang moeten vluchten. Keuzen 1: gewoon in de stad blijven en hopen dat de burger oorlog niet naar hun stad gaat. Keuzen 2: vragen aan hun of je met hun mee mogen met vluchten.")
    answer = input(">")
    if "1" in answer:
        Lkeuzen_5_1()
    else:
        print("\nType 1 of 2 in\n")
        Lkeuzen_4_1()
    
def Lkeuzen_5_1():
    print("\nJe zegt tegen hun dat je weer verder gaat met winkelen en je geeft hun geluk op een veilige reis. Je bent in de winkel en gaat kijken wat je wil kopen voor avond eten. Je bent klaar met winkelen en gaat naar huis. Je ziet de buren nog een keer en ze vragen aan jou of je mischien me wil reizen. Keuzen 1: je zegt tegen hun dat je niet mee hoeft te reizen want je blijft in de stad. Keuzen 2: je zegt dat je wel mee wil gaan en vraagt waneer ze vertreken.")
    answer = input(">")
    if "1" in answer:
        Lkeuzen_6_1()
    elif "2" in answer:
        RKeuzen_2_2()
    else:
        print("\nType 1 of 2 in\n")
        Lkeuzen_5_1()

def Lkeuzen_6_1():
    print("\nJe vertelt ze dat je liever hier in de stad wil blijven en zegt hun gedag. Je loopt verder naar huis en gaat eten. Je bent tv aan het kijken aan het luisteren naar het nieuws. Je krijgt een bericht van een colega en hij zegt dat de hooft producer overladen is en zegt dat de burger oorlog al aan de rand van de stad is. Hij verteld dat hij van plan is om uit de stad te gaan. Hij vraagt aan jou of je mischien mee wilt gaan. Keuzen Keuzen 1: je zegt tegen hem dat je liever hier in de stad blijft dan uit de stad wil gaan. Keuzen 2: je vertelt hem dat je wel mee wil gaan en vraagt aan hem waneer hij weg wil gaan.")
    answer = input(">")
    if "1" in answer:
        Lkeuzen_7_1()
    elif "2" in answer:
        RKeuzen_2_2()
    else:
        print("\nType 1 of 2 in\n")
        Lkeuzen_6_1()

def Lkeuzen_7_1():
    print("\nJe stuur je colega een appje dat je liever in de stad wil blijven en je zegt hem gedag. Het begint laat te worden en je gaan naar bed. De volgende ochtend wordt je waker door de schooten buiten je huis. Je loopt naar het raam to en ziet in de verten gebouwen in de brand en je hoort veel schooten. Je brobeert zo snel mogelijk we te komen. Je neemt je belangerkijken spullen me. Je rent zo snel mogelijk weg maar je wordt gevolgd door mensen met geweren. Je brobeert in een steeg te verbergen maar ze vinden je en ze schieten je dood.")
    game_over("\nF\n")

def RKeuzen_1_2():
    print("\nJe vertelt je collega’s dat je niet naar werk gaat omdat je wilt weten hoe de burgeroorlog gaat ontwikkelen. Je gaat verder met tv kijken en zoekt op het internet op hoe het gaat met de burgeroorlog. Je ziet op internet dat de oorlog snel groot wordt. Keuzen 1: je blijft in de stad en wacht nog even af hoe het gaat aflopen. Keuzen 2: je neemt de keuzen om uit de stad te gaan.")
    answer = input(">")
    if "2" in answer:
        RKeuzen_2_2()
    else:
        print("\nType 1 of 2 in\n")
        RKeuzen_1_2

def Rkeuzen_2_1():
    print("\nJe neemt de keuzen om in je stad te blijven. Je wilt wat eten maar ziet in de koelkast dat je geen eten meer hebt. Je loopt naar de winkel toe en je hoort je buren praten dat ze uit de stad gaan om een veilige plek te zoeken. Je vraagt aan hun of ze denken dat de burger oorlog naar de stad gaan komen. Ze zegen dat hun familie in de stad naast de stad waar jij woont. Dat ze al een beetje me de oorlog te maken hebben. Hun familie heeft tegen hun gezegd dat het verstandig je om uit de stad te gaan en naar een veilig stad/lang moeten vluchten. Keuzen 1: gewoon in de stad blijven en hopen dat de burgeroorlog niet naar hun stad gaat. Keuzen 2: vragen aan hun of je met hun mee mogen met vluchten.")
    answer = input(">")
    if "1" in answer:
        Lkeuzen_5_1()
    else:
        print("\nType 1 of 2 in\n")
        Rkeuzen_2_1
# er zijn 3 keuzes \/
def RKeuzen_2_2():
    print("\nJe zoekt al je belangrijks spullen en pakt alles in wat je nodig hebt. Je zoekt uit wat de veiligste weg is uit het land. Je verteld tegen de huurder van je appartement dat je uit het land gaat en de laatste betaling geeft. Je zegt hem gedag en vertrekt. Je stapt in je auto en begint naar het noorden te gaan. je bent op de snelweg en je ziet dat er verderop een groot ongeluk is gebeurt. Je weet dat dit de enige route is naar de plek waar je heen wilt. Je stopt in een file en denkt na wat je nu gaat doen. Keuzen 1: je rijd terug naar achter en probeert toch een andere route te zoeken. Keuzen 2: je beslist om verder te gaan lopen want je weet dat je later toch met een boot moet. Keuzen 3: in de auto wachten tot dat je weer verder kan rijden.")
    answer = input(">")
    if "2" in answer:
        RKeuzen_3_2()
    else:
        print("\nType 1 of 2 in\n")
        RKeuzen_2_2()

def Rkeuzen_3_1():
    print("\nJe kijkt in je spiegels en ziet dat er veel auto’s aan komen. Je kan niet echt naar achter rijden. Keuzen 1: je beslist om verder te gaan lopen want je weet dat je later toch met een boot moet. Keuzen 2: in de auto wachten tot dat je weer verder kan rijden.")
    answer = input(">")
    if "1" in answer:
        RKeuzen_3_2()
    elif "2" in answer:
        Rkeuzen_3_3()
    else:
        print("\nType 1 of 2 in\n")
        Rkeuzen_3_1()

def Rkeuzen_3_3():
    print("\nJe bent aan het wachten en wachten er gebeurt niets. je neemt toch de beslissing om te gaan lopen.")
    RKeuzen_4_2()

def RKeuzen_3_2():
    print("\nJe loopt verder naar je locatie en loop langs het ongeluk. Je ziet dat er een paar mensen gewond zijn. Keuzen 1: de mensen die gewond zijn helpen. Keuzen 2: gewoon verder lopen en ze laten ligen")
    answer = input(">")
    if "2" in answer:
        RKeuzen_4_2()
    else:
        print("\nType 1 of 2 in\n")
        RKeuzen_3_2()

def RKeuzen_4_2():
    print("\nJe beslist dat je gewoon verder gaat lopen. Je ziet in een tankstation je gaat daar even ontbijten. Je loopt weer verder en komt bij de boot aan die je moet pakken. Je ziet dat er nog niet veel mensen zijn en je neemt de volgende boot die zo meteen vertrekt. Je zit met wat andere mensen te praten en ze vertellen je over een land dat heel veilig is en veel vrijheid. Het land is wel een stuk verder dan je land dat je gekozen hebt. Je denkt over dat je misschien met hun mee wilt gaan. Keuzen 1: je neemt de keuzen om niet met hun mee te gaan. Keuzen 2: je vraagt aan hun of je misschien met hun mee kan gaan.")
    answer = input(">")
    if "2" in answer:
        RKeuzen_5_2()
    else:
        print("\nType 1 of 2 in\n")
        RKeuzen_4_2()

def RKeuzen_5_2():
    print("\nJe vraagt aan hun of je misschien mee mag gaan met hun. Hun zeggen tegen je dat je wel mee mag gaan met hun. Jullie hebben een rustige reis ver door de landen heen en jullie zijn al binnen een paar weken op jullie locatie. Je komt binnen in het land maar je mag er niet in van de gemeente. Ze zegen dan je er nog niet in mag omdat er heel veel mensen naar het land toe gaan. Keuzen 1: Je gaat naar het land hiernaast. Keuzen 2: Hier blijven en wachten tot je weer naar binnen kan gaan.")
    answer = input(">")
    if "2" in answer:
        RKeuzen_6_2
    elif "1" in answer:
        RKeuzen_6_1()
    else:
        print("\nType 1 of 2 in\n")
        RKeuzen_5_2

def RKeuzen_6_1():
    print("\nHet land waar je nu naar toe gaat is een stuk verder maar je weet wel dat het veilig is en dat je naar binnen mag. Je begint er heen te lopen en ziet verder op een paar mensen lopen. Je vraagt aan hun of ze ook naar dat land gaan en ze zegen ja. Je vraagt aan hun of je misschien met hun mee mag gaan omdat jij ook de zelfde kant op gaat. Je komt aan bij het land het zegt ze gedag. Je komt het land binnen maar ze zegen dat je er niet in mag omdat er te veel vluchtelingen naar binnen gaan. Je moet toch naar een ander land gaan. Je weet nog dat er een land is waar familie woont maar je weet ook dat het daar gevaarlijk is vindt er is veel misdaad. Keuzen 1: toch hier blijven wachten tot je naar binnen kan gaan.) Keuzen 2: naar het land gaan waar een familie lid woont.")
    answer = input(">")
    if "1" in answer:
        RKeuzen_6_2()
    elif "2" in answer:
        RKeuzen_7_2()
    else:
        RKeuzen_6_1()

def RKeuzen_7_2():
    print("\nJe gaat op rijs naar het land waar je familie woont. Maar onderweg word je aangehouden door de politie want je mag niet door dat land heen vluchten. Het is een best brute gevangenis en je maakt niet bepaalt vrienden. Na een tijd heb je niet genoeg eten gekregen en ga je dood van de honger.")
    game_over("you died")
    
def RKeuzen_6_2():
    print("\nJij verblijft in het land tot je binnen wordt gelaten. Je wordt geïnterviewd omdat ze willen weten uit welk land je komt en of je wel moet vluchten uit je land. Je hebt verteld dat het niet veilig is in je land en dat je gevlucht ben omdat de oorlog dicht bij zijn stad was. Na het interview word er gezegd dat ze later bij je terug komen. En paar dagen later kijk je een email dat je in het land mag blijven.")
    good_ending("\nGOOD Ending\n")

def LKeuzen_2_2():
    print("\nJe gaat terug naar huis. Je vertelt je collega’s dat je niet naar werk gaat omdat je wilt weten hoe de burgeroorlog gaat ontwikkelen. Je gaat verder met tv kijken en zoekt op het internet op hoe het gaat met de burgeroorlog. Je ziet op internet dat de oorlog snel groot wordt. Keuzen 1: je blijft in de stad en wacht nog even af hoe het gaat aflopen. Keuzen 2: je neemt de keuzen om uit de stad te gaan.")
    answer = input(">")
    if "1" in answer:
        Rkeuzen_2_1()
    elif "2" in answer:
        RKeuzen_2_2()
    else:
        LKeuzen_2_2()

def LKeuzen():
    print("\nJe vertelt wat je over de situatie te zegen heb en geeft je mening tegen je. Na het programma ga je nog even lunchen met je collega’s. Een collega zegt tegen je of je misschien met hem naar huis kan om daar wat meer over de situatie te praten. Je bent met hem over je mening aan het praten. Maar dan hoorde ze in de beurt een bom afgaan. Je rent naar buiten en ziet dat ze voor je de oorlog gebeuren. Je hoort geweer schoten tot dat er een bom op de locatie valt waar je bent.")
    game_over()

def LKeuzen_5_2():
    RKeuzen_2_2()

def RKeuzen_3_1_1():
    print("\nJe neemt de keuzen om in je stad te blijven. Je bent thuis en wilt gaat eten maar ziet in de koelkast dat je geen eten meer hebt. Je loopt naar de winkel toe en je hoort je buren praten dat ze uit de stad gaan om een veilige plek te zoeken. Je vraagt aan hun of ze denken dat de burger oorlog naar de stad gaan komen. Ze zegen dat hun familie in de stad naast de stad waar jij woont. Dat ze al een beetje me de oorlog te maken hebben. Hun familie heeft tegen hun gezegt dat het verstandig je om uit de stad te gaan en naar een veilig stad/lang moeten vluchten. Keuzen 1: gewoon in de stad blijven en hopen dat de burgeroorlog niet naar hun stad gaat. Keuzen 2: toch gaan vluchten na wat je gehoord hebt.")
    answer = input(">")
    if "1" in answer:
        Lkeuzen_5_1()
    elif "2" in answer:
        RKeuzen_2_2()
    else:
        RKeuzen_3_1_1()

def restart(reason):
    print("" + reason)
    start()

def game_over(reason):
  print("" + reason)
  print("Game Over!")
  play_again()

def good_ending(reason):
    print("" + reason)
    print("goed gedaan!!!")
    play_again()

def play_again():
    print("\nwil je opnieuw spelen? (ja of nee)")
    answer = input(">")
    if "ja" in answer:
        start()
    else:
        exit()

start()
