def count_bases(seq):
    return seq.count("A"), seq.count("C"), seq.count("G"), seq.count("T")

def transcribe(seq):
    return seq.replace("T", "U")


def gc_content(seq):
    gc_count = seq.count("G") + seq.count("C")
    return gc_count / len(seq) * 100
print(count_bases("AAAACCCGGT"))
print(transcribe("GATGGAACTTGACTACGTAAATT"))
print(gc_content("AAAACCCGGT"))
