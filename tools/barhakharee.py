vyanjan = """कखगघङचछजञटठडढणतथदधनपफबभमयरलवशषसह"""
diacritics = ["", "ा", "ि", "ी", "ु", "ू", "ृ", "े", "ै", "ो", "ौ", "ँ", "ं", "ः"]

for alphabet in vyanjan:
    for maatraa in diacritics:
        print(alphabet + maatraa, end="\t")
    print()
