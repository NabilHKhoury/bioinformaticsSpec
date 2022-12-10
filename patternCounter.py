DNAseq = input("input DNA sequence:")
pattern = input("input DNA pattern to search for:")
count=0
for i in range(len(DNAseq)-len(pattern)+1):
    if (DNAseq[i:i+len(pattern)]==pattern):
        count = count+1
print(count)
