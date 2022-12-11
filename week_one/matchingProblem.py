#Input: Two strings, Pattern and Genome.
#Output: A collection of space-separated integers specifying all starting positions where Pattern appears as a substring of Genome.
def patternIndex(DNAseq,pattern):
    indexArr = []
    for i in range(len(DNAseq)-len(pattern)+1):
        if (DNAseq[i:i+len(pattern)]==pattern):
            indexArr.append(i)
    return indexArr
