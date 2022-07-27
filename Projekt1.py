# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

#Autor: Miroslav Zelený
#email: m.zeleny@volny.cz
#Discord: Mirek Z.

uzivatelska_jmena = ["bob","ann","mike","liz"]
hesla = ["123","pass123","password123","pass123"]

uzivatelske_jmeno=input("Zadej uzivatelske jmeno:")
while uzivatelske_jmeno not in uzivatelska_jmena:
    print("Uživatel není v databázi")
    uzivatelske_jmeno = input("Zadej uzivatelske jmeno:")
else:
    print( "Ahoj "  +  uzivatelske_jmeno + "!")


if uzivatelske_jmeno in uzivatelska_jmena:
    index=uzivatelska_jmena.index(uzivatelske_jmeno) #najde index uživatelksého jména, aby mohl program porovnat správné heslo

    heslo = input("Zadej heslo:")
while heslo!=hesla[index]:
    print("Heslo neodpovídá zadanému uživateli")
    heslo = input("Zadej heslo:")
else:
    print("Můžeš analyzovat texty")

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
garpike and stingray are also present.'''
]

text=input("Vyber text 1-3:")
while text not in ["1","2","3"]:
    print("Neexistuící číslo textu. Zadej číslo 1-3:")
    text=input("Vyber text 1-3:")
    break
else: print(f"vybírám text {text}:")

#print(TEXTS[int(text)-1])  #vytiskne patřičný text

words=TEXTS[int(text)-1].split()    #udělá z textu list slov

uppercase_latters=0  #deklarace později použitých proměnných
lowercase_latters=0
uppercase_word=False
uppercase_words=0
lowercase_word=False
lowercase_words=0
words_in_capital=0
words_in_lowercase=0
digits=0
sum_digits=0
delka_slov=[]
pocet_slov_v_textu=len(words)
print("Počet slov v textu:", pocet_slov_v_textu)

title_latters=0
for index_slova,word in enumerate(words):
    title_latter = word[0].istitle()  #hledáme slova začínající velkými písmeny
    if title_latter == True:
        title_latters += 1

    if word.isnumeric():       #vrací počet číslic v textu a jejich sumu
        digits+=1
        sum_digits+=int(word)

    lowercase_word=word.islower()    #vrací počet slov psaných malými písmeny
    if lowercase_word==True:
        lowercase_words+=1

    uppercase_word=word.isupper()      #vrací počet slov psaných velkými písmeny
    if uppercase_word==True:
        uppercase_words+=1

    delka_slov.append(len(word))  # vytvoří list s délkami jednotlivých slov v textu
max_delka_slova = max(delka_slov)  # nejdelší slovo v textu

print("Počet slov začínajících velkým písmenem:", title_latters)
print("Počet slov psaných velkými písmeny:", uppercase_words)
print("Počet slov psaných malými písmeny:",lowercase_words)
print("Počet čísel:", digits)
print("Suma všech čísel:",sum_digits)
print("Nejdelší slovo(písmen):", max_delka_slova)


a=0
for i in range(max_delka_slova+1):  #vypíše histogram četnosti délky jednotlivých slov
    for b in range(pocet_slov_v_textu):
        if i==delka_slov[b]:
            a+=1
    print("Četnost délky slov:",i,a*"*",a)
    a=0














