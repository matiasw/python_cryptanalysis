import re
import sys
from ngram_score import ngram_score
fitness = ngram_score('quadgrams.txt') # load our quadgram statistics
from pycipher import Caesar
      
def break_caesar(ctext):
    # make sure ciphertext has all spacing/punc removed and is uppercase
    ctext = re.sub('[^A-Z]','',ctext.upper())
    # try all possible keys, return the one with the highest fitness
    scores = []
    for i in range(26):
        scores.append((fitness.score(Caesar(i).decipher(ctext)),i))
    return max(scores)
    
# ciphertext
ctext = ""
if (len(sys.argv) >= 2):
	with open(sys.argv[1], "r") as f:
		ctext = str(f.read())
	print("Cipher text: " + ctext)
else:
	print("Usage: " + sys.argv[0] + " filename")
max_key = break_caesar(ctext)

print('best candidate with key (a,b) = '+str(max_key[1])+':')
plaintext = Caesar(max_key[1]).decipher(ctext)
print(plaintext)

print("Cipher spacing and such reconstructed into plaintext:")
restoredplain = ""
pi = 0
for c in ctext:
	if c.isalpha():	#alphabetic, ie. this character is in the filtered plaintext
		if c.isupper():
			restoredplain = restoredplain + plaintext[pi]
		else:
			restoredplain = restoredplain + plaintext[pi].lower()
		pi = pi + 1
	else:	#some other character
		restoredplain = restoredplain + c

print(restoredplain)
