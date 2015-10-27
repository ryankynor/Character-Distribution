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
import collections

text = input("Please enter a string of text (the bigger the better): ")
ltext = text.lower()

print (('The distribution of characters in "{0}" is: '.format(text))
"""
results = collections.Counter(ltext)
"""
textlen = len(results)
stext = sorted(ltext)

textlength = int(textlen)
for stext in ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    dis.append(ltext.count(stext))

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