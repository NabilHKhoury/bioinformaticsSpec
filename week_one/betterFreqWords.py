from frequencyWordProblem import freqTable
from maxMap import maxMap

def betterFreqWords(DNAseq, k):
    freqPatterns = []
    freq_map = freqTable(DNAseq, k)
    max = maxMap(freq_map)
    for pattern in freq_map:
        if freq_map[pattern] == max:
            freqPatterns.append(pattern)
    return freqPatterns




