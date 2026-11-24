def count_bases(seq):
    return seq.count("A"), seq.count("C"), seq.count("G"), seq.count("T")


def transcribe(seq):
    return seq.replace("T", "U")


def gc_content(seq):
    gc_count = seq.count("G") + seq.count("C")
    return gc_count / len(seq) * 100


def reverse_complement(seq):
    table = str.maketrans("ATCG", "TAGC")
    reversed_seq = seq[::-1]
    return reversed_seq.translate(table)


print(count_bases("AAAACCCGGT"))
print(transcribe("GATGGAACTTGACTACGTAAATT"))
print(gc_content("AAAACCCGGT"))
print(reverse_complement("AAAACCCGGT"))