from frequencyWordProblem import freqTable

def findClumps(dnaSeq,k_mer, l,t):
    patterns= []
    for i in range(len(dnaSeq)-l+1):
        currSeq = dnaSeq[i:i+l]
        freqMap = freqTable(currSeq,k_mer)
        for key in sorted(freqMap.keys()):
            if freqMap[key] >=t and key not in patterns:
                patterns.append(key)
    return patterns

