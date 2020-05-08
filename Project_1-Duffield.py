#Projekt 1 - Karolína Duffield


#variables:
ODDELOVAC = '-'*50
USERS = {'user':'password','bob':'123','ann':'pass123','mike':'password123','liz':'pass123'}
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley.''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

#1. Na začátku přivítá uživatele.

print(ODDELOVAC)
print('Welcome to the app. Please log in:')

#2. Vyžádá si od uživatele přihlašovací jméno a heslo.

username=input('USERNAME:')
pswd=input('PASSWORD:')

#print('USERNAME: ',username)
#print('PASSWORD: ',pswd)

#3. Zjistí, jestli zadané údaje odpovídají někomu z registrovaných uživatelů.

if username not in USERS:
    print("We're sorry, you're not registered.")
    exit()

while username in USERS:
    if USERS[username] == pswd:
        print(ODDELOVAC)
    else:
        print("We're sorry, password is not correct.")
        exit()
    break

#4. Program nechá uživatele vybrat mezi třemi texty, uloženými v proměnné TEXTS.

print('We have 3 texts to be analyzed.')
select = int(input('Enter a number btw. 1 and 3 to select:'))-1 #aby sa zvolene cislo textu rovnalo indexu
print(ODDELOVAC)

#5. Pro vybraný text spočítá následující statistiky:
    #- počet slov,
    #- počet slov začínajících velkým písmenem,
    #- počet slov psaných velkými písmeny,
    #- počet slov psaných malými písmeny,
    #- počet čísel (ne cifer!).

seleced_text = TEXTS[select].split()

count_word = len(seleced_text)
print(f'There are {count_word} words in the selected text.')

i=0
container,container2,container3,container4=[[],[],[],[]]
count_title,count_upper,count_lower,count_digit = [0,0,0,0]

while i<len(seleced_text):
    word = seleced_text[i]
    
    if word.istitle():
        container.append(word)
        count_title=len(container)
    elif word.isupper():
        container2.append(word)
        count_upper=len(container2)
    elif word.islower():
        container3.append(word)
        count_lower=len(container3)
    elif word.isdigit():
        container4.append(float(word))
        count_digit=len(container4)
    i=i+1

print(f'There are {count_title} titlecase words')
print(f'There are {count_upper} uppercase words')
print(f'There are {count_lower} lowercase words')
print(f'There are {count_digit} numeric strings')
print(ODDELOVAC)

#6. Program zobrazí jednoduchý sloupcový graf, který bude reprezentovat četnost různých délek slov v textu. 

i=0
slo = dict()
lenghts=[]

while i<len(seleced_text):
    lenght = len(seleced_text[i])
    lenghts.append(lenght)
    counts = lenghts.count(lenghts[i])
    slo.update({lenght: counts})
    i += 1

l = list(slo.keys())
l.sort()

for a in l:
    graph = '*' * slo.get(a)
    index = l.index(a)
    print(l[index], graph, slo[a])
    
print(ODDELOVAC)

#7. Program spočítá součet všech čísel (ne cifer!) v textu. 
# Výsledkem tohoto součtu v následujícím textu by teby bylo číslo 8500:

print("If we summed all the numbers in this text we would get: ", sum(container4))
print(ODDELOVAC)
    