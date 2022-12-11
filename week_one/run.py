from betterFreqWords import betterFreqWords
from reverseComplement import reverseComplement
from matchingProblem import patternIndex
from listToString import listToString
DNAseq=open("C:\\Users\\khour\\Downloads\\Vibrio_cholerae.txt").read()
pattern = "CTTGATCAT"
print(listToString(patternIndex(DNAseq, pattern)))