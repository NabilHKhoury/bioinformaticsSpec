from frequencyWordProblem import freqTable

def maxMap(freqTable):
    max=0
    for key in sorted(freqTable.keys()):
        if freqTable[key]>max:
            max= freqTable[key]
    return max