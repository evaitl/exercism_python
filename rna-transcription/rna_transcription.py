def to_rna(dna_strand):
    compls = {"G": "C", "C": "G", "T": "A", "A": "U"}
    return "".join(compls[x] for x in dna_strand)
