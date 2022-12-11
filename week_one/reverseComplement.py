def reverseComplement(DNAseq):
    DNAseq.upper()
    reverseStrand = ""
    for i in range(len(DNAseq)):
        if DNAseq[i] == "A":
            reverseStrand = "T" +reverseStrand
        elif DNAseq[i] == "T":
            reverseStrand = "A"+ reverseStrand
        elif DNAseq[i] == "G":
            reverseStrand = "C"+ reverseStrand
        else:
            reverseStrand = "G"+ reverseStrand
    return reverseStrand


