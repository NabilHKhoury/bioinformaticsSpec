def freqTable(text,k_mers):
    freq_map = dict()
    for i in range(len(text)-k_mers+1):
        pattern = text[i:i+k_mers]
        if pattern in freq_map:
            freq_map[pattern]= freq_map[pattern]+1
        else:
            freq_map[pattern]=1
    return freq_map

