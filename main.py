"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Ivo Srot
email: srot.ivo@gmail.com
discord: theivos_63282
"""
# TEXTS

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
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
garpike and stingray are also present.''',
]

# STARTING VARIABLES

user = True

users = {"bob":"123", "ann":"pass123","mike":"password123","liz":"pass123"}
oddelovac = "-" * 40

user = input("username: ")
if user == "":
    user = "anonymouse"

    # PROGRAM

while user:
    # USER AND PASS CORRECT
    if (password := input("password: ")) == users.get(user):
        print(oddelovac)
        print("Welcome to the app,",user)
        print("We have " + str(len(TEXTS)) + " texts to be analyzed.")
        print(oddelovac)
        
        # TEXT CHOICE
        choice = int(input("Enter a number btw. 1 and " + str(len(TEXTS)) + " to select: ")) -1
        print(oddelovac)

        # TEXT CHOICE DOESNT EXIST
        if choice not in range(len(TEXTS)):
            print("Option",choice +1,"doesnt exist, terminating program...")
            break
        else:
         
            # CHOSEN TEXT
            texttoex = TEXTS[choice]
            
            # TEXT TO LIST
            splittedtext = texttoex.split()

            # TEXT IN MASH STYLE = Cases like: "M.A.S.H", "37.episode", "I did.But you" and such
            pre_mashstyle = []
            for i in splittedtext:
                for j in i:
                    if j == j.upper() and "." in j:
                        pre_mashstyle.append(i)
            
            toset = set(pre_mashstyle)
            pre_mashstyle = list(toset)
            
            forsplitted = []
            addinstnt_list = []
            for i in pre_mashstyle:
                dotssum = []
                uppersum = []
                for j in i:
                    if j == ".":
                        dotssum.append(j)
                    elif j == j.upper():
                        uppersum.append(j)
                if len(dotssum) >= 2 or i.endswith("."):
                    addinstnt_list.append(i)
                else:
                    forsplitted = i.split(".")
                    splittedtext.remove(i)
                    for i in forsplitted:
                        splittedtext.append(i)
                                 
            # TEXT IN MASH STYLE WITH NO PUNCT
            nopunct_splitted = splittedtext.copy()
            for i in nopunct_splitted:
                dotssum = []
                for j in i:
                    if j == ".":
                        dotssum.append(j)                
                if i.endswith(".") and len(dotssum) < 2:
                    splittedtext.remove(i)
                    splittedtext.append(i.replace(".",""))
                if i.endswith(","):
                    splittedtext.remove(i)
                    splittedtext.append(i.replace(",",""))
                if i.endswith("!"):
                    splittedtext.remove(i)
                    splittedtext.append(i.replace("!",""))
                if i.endswith("?"):
                    splittedtext.remove(i)
                    splittedtext.append(i.replace("?",""))    
            
            # LIST TEXT WITHOUT ANY NUMBERS
            total_numberlesstext = splittedtext.copy()
            remove_list = []
            to_remove = set()
            for i in splittedtext:
                for j in i:
                    if j.isnumeric():
                        to_remove.add(i)
                        remove_list = list(to_remove)
            for i in range(len(remove_list)):
                total_numberlesstext.remove(remove_list[i])

            # WORDCOUNT
            wordcount = len(splittedtext)
            print("There are", wordcount ,"words in the selected text.")
            
            # TITLES
            titles = []
            for i in splittedtext:
                if i[0].isupper():
                    titles.append(i)
            print("There are",(len(titles)),"titlecase words.")

            # UPPERCASE WORDS
            uppercases = []
                        
            for i in total_numberlesstext:
                if i == i.upper():
                    uppercases.append(i)
            
            print("There are",len(uppercases),"uppercase words.")

            # LOWERCASE WORDS
            lowercases = []
                                    
            for i in total_numberlesstext:
                if i == i.lower():
                    lowercases.append(i)
            
            print("There are",len(lowercases),"lowercase words.")      

            # NUMERIC STRINGS
            numericstrings = []

            for i in splittedtext:
                if i.isnumeric():     
                    numericstrings.append(i)

            print("There are",len(numericstrings),"numeric strings.")

            # NUM SUM
            numstosum = []
            for i in numericstrings:
                numstosum.append(int(i))
            summednums = sum(numstosum)
            print("The sum of all the numbers:",summednums)

            # STARS
            stars_dict = {}
            stars_dict_big = {}

            for i in splittedtext:
                if len(str(i)) < 10:
                    stars_dict[len(str(i))] = 0
                else:
                    stars_dict_big[len(str(i))] = 0

            dict_to_comp = list(stars_dict)
            dict_to_comp_big = list(stars_dict_big)

            for i in splittedtext:
                for j in dict_to_comp:
                    if len(str(i)) == j:
                        stars_dict[len(str(i))] += 1
                    
            for i in splittedtext:
                for j in dict_to_comp_big:
                    if len(str(i)) == j:
                        stars_dict_big[len(str(i))] += 1

            pre_stars = list(stars_dict.items())
            pre_stars_big = list(stars_dict_big.items())

            # MAX LINE-LENGTH
            pre_maxlength = pre_stars + pre_stars_big
            notyet_maxlength = []
            for i,b in pre_maxlength:
                notyet_maxlength.append(b)
            maxlength = max(notyet_maxlength)
            
            abeceda = []
            for i,b in pre_stars:
                adda = str((3 - len(str(i))) * " ") + str(i) + "|" + str(b * "*") + str(((maxlength - b) + 2)*" ") + "|" + str(b)
                abeceda.append(adda)

            abeceda_big = []
            for i,b in pre_stars_big:
                adda = str((3 - len(str(i))) * " ") + str(i) + "|" + str(b * "*") + str(((maxlength - b) + 2)*" ") + "|" + str(b)
                abeceda_big.append(adda)

            sorted_abc = sorted(abeceda)
            sorted_abc_big = sorted(abeceda_big)

            # STAR TABLE
            print(oddelovac)
            print("LEN|  OCCURENCES  |NR.")
            print(oddelovac)

            for i in sorted_abc:
                print(str(i).replace("'","").replace(",","").strip("()"))

            for i in sorted_abc_big:
                print(str(i).replace("'","").replace(",","").strip("()"))
            
            # END OF PROGRAM
            break    

    # WRONG PASSWORD
    elif user in users and password != users[user]:
        print("Wrong password, terminating the program...")  
        user = False  
    
    # UNREGISTERED USER
    else:
        print("Unregistered user, terminating the program...")
        user = False

