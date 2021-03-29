# Cole
#Takes a file containing separate words and returns all permutations to further generate a wordlist from

from itertools import permutations

#Begin with list of words and append results to original list
infile = "words" 
outfile = "wordlist"

#Create list L that contains each word
with open(infile) as wordlist:
    L = [line.rstrip() for line in wordlist]

#Permutate words at every length from 1 through len(words)
with open(outfile, "w") as wordlist:
    for n in range(len(L)+1):
        for perm in permutations(L, n):
            wordlist.write(''.join(perm))
            wordlist.write('\n')
