nato = {
    'a' : "Alpha",
    'b' : "Bravo",
    'c' : "Charlie",
    'd' : "Delta",
    'e' : "Echo",
    'f' : "Foxtrot",
    'g' : "Golf",
    'h' : "Hotel",
    'i' : "India",
    'j' : "Juliet",
    'k' : "Kilo",
    'l' : "Lima",
    'm' : "Mike",
    'n' : "November",
    'o' : "Oscar",
    'p' : "Papa",
    'q' : "Quebec",
    'r' : "Romeo",
    's' : "Sierra",
    't' : "Tango",
    'u' : "Uniform",
    'v' : "Victor",
    'w' : "Whisky",
    'x' : "XRay",
    'y' : "Yankee",
    'z' : "Zulu",
    '0' : "Zero",
    '1' : "One",
    '2' : "Two",
    '3' : "Three",
    '4' : "Four",
    '5' : "Five",
    '6' : "Six",
    '7': "Seven",
    '8' : "Eight",
    '9' : "nine"
}
word = str(input('Write your word: ')) 
for n in word:
    if n == ' ':
        print('/ ', end='')
    print(nato.get(n), ' ', end='')

#b = word.split(' ')
#for n in b:
#    print(n)
#    if n in nato.values():
#        print(nato.items(n))

