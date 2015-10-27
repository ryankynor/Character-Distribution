"""
distribution.py
Author: Ryan Kynor
Credit: 

Assignment:

Write and submit a Python program (distribution.py) that computes and displays 
the distribution of characters in a given sample of text.

Output of your program should look like this:

Please enter a string of text (the bigger the better): The rain in Spain stays mainly in the plain.
The distribution of characters in "The rain in Spain stays mainly in the plain." is:
iiiiii
nnnnnn
aaaaa
sss
ttt
ee
hh
ll
pp
yy
m
r

Notice about this example:

* The text: 'The rain ... plain' is provided by the user as input to your program.
* Uppercase characters are converted to lowercase
* Spaces and punctuation marks are ignored completely.
* Characters that are more common appear first in the list.
* Where the same number of characters occur, the lines are ordered alphabetically. 
  For example, in the printout above, the letters e, h, l, p and y both occur twice 
  in the text and they are listed in the output in alphabetical order.
* Letters that do not occur in the text are not listed in the output at all.
"""


text = input("Please enter a string of text (the bigger the better): ")
ltext = text.lower()

l1 = []
l2 = []

letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
print (('The distribution of characters in "{0}" is:').format(text))

textlen = len(text)
stext = sorted(ltext)


for stext in letters:
    l2.append(ltext.count(stext))

zlist = list(zip(l2,letters))
#print(zlist)
h = textlen
while h > 0:
    for ltext in zlist:
        if ltext[0] == h:
            l1.append(ltext[1]*ltext[0])
    h = h - 1
    
for stext in l1:
    print (stext)


"""
highest = []

biglist = []
for y in results:
    if results[y]:
        #if not in y then append
    else:
        highest.append(results[y])
highest.sort()

#new = highest[::-1]
for g in highest:
    for z in results:
        if results[z] == g:
#           results[z] = 0
            for s in range(g):
                biglist.append(g*z)
print(biglist)
     

#print ('The distrabution of characters in "{0}". is:'.format(text))
""" 