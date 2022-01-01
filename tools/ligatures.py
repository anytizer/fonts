vyanjan = """कखगघङचछजञटठडढणतथदधनपफबभमयरलवशषसह"""

halant = "्"
for half in vyanjan:
    ligatures = []
    for full in vyanjan:
        ligature = half + halant + full
        ligatures.append(ligature)
    print(ligatures)
