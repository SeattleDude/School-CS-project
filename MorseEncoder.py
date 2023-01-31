DIVIDINGCHAR = "/" # set the character to divide letters by

inp = input("input english here e.g. \'hi for \'..../..\'\'")


lst = [] # this list is used to concatenate all the letters' results and turn them into a single pretty output

ab = {

    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",

}
# the above dictionary is just the translations of english to morse code

for ch in inp:
    lst.append(ab.get(ch))
    lst.append(DIVIDINGCHAR)

for thing in lst:
    print(thing, end = "")

print("\n")