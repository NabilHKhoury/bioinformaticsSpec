import webbrowser
from betterFreqWords import betterFreqWords
from reverseComplement import reverseComplement
from matchingProblem import patternIndex
from listToString import listToString
from findClumps import findClumps
from patternCounter import patternCounter
DNAseq= webbrowser.open(input("Enter URL"))
k_mer= 9
length = 500
t = 3
print(findClumps(DNAseq,k_mer,length,t))