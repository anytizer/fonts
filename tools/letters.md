SQL:

```
select
	letter_name name,
	letter_variable variable,
	letter_strokes strokes,
	letter_type type
from tw_letters
order by
	type, name
;
```

name	|	variable	|	strokes	|	type
------|-----------|---------|------------------------
rree	|	rree	|		|	
अ	|	a	|	u, terso, danda, dikaa	|	
आ	|	aa	|	u, terso, danda, kaannaanee, dikaa	|	
इ	|	i	|	i, dikaa	|	
ई	|	ee	|	i, reph, dikaa	|	
उ	|	u	|	u, dikaa	|	
ऊ	|	oo	|	u, puchchhar, dikaa	|	
ऋ	|	rri	|		|	
ऌ	|	lri	|		|	
ऍ	|	eh	|		|	
ऎ	|	eaih	|		|	
ए	|	e	|	letter_ra, vertical	|	
ऐ	|	ai	|	letter_ra, vertical, eklakke	|	
ओ	|	o	|	u, terso, danda, kaannaanee, eklakke, dikaa	|	
औ	|	au	|	u, terso, danda, kaannaanee, dolakke, dikaa	|	
क	|	ka	|	letter_wa, danda, puchchhar, dikaa	|	
क्ष	|	क्ष	|		|	
ख	|	kha	|	letter_ra, letter_wa, danda, dikaa	|	
ग	|	ga	|	letter_ga, danda, dikaa	|	
घ	|	gha	|	letter_gha, danda, dikaa	|	
ङ	|	nga	|	letter_da, thoplo, dikaa	|	
च	|	cha	|	letter_cha, danda, dikaa	|	
छ	|	chha	|	letter_chha, dikaa	|	
ज	|	ja	|	letter_ja, terso, danda, dikaa	|	
ज्ञ	|	ज्ञ	|		|	
झ	|	jha	|	i, terso, danda, dikaa	|	
ञ	|	nya	|	letter_nya, terso, danda, dikaa	|	
ट	|	ta	|	letter_ta, alpa, dikaa	|	
ठ	|	tha	|	letter_tha, alpa, dikaa	|	
ड	|	da	|	letter_da, dikaa	|	
ढ	|	dha	|	letter_dha, alpa, dikaa	|	
ण	|	nna	|	letter_nna, danda, dikaa	|	
त	|	tta	|	letter_tta, danda, dikaa	|	
त्र	|	त्र	|		|	
थ	|	ttha	|	letter_ttha, danda, dikaa	|	
द	|	dda	|	letter_dda, dikaa	|	
ध	|	ddha	|	letter_ddha, danda, dikaa	|	
न	|	na	|	letter_na, danda, dikaa	|	
प	|	pa	|	letter_pa, danda, dikaa	|	
फ	|	pha	|	letter_pa, danda, puchchhar, dikaa	|	
ब	|	ba	|	letter_wa, petchiryo, danda, dikaa	|	
भ	|	bha	|	letter_bha, danda, dikaa	|	
म	|	ma	|	letter_ma, danda, dikaa	|	
य	|	ya	|	letter_ya, danda, dikaa	|	
र	|	ra	|	letter_ra, dikaa	|	
ल	|	la	|	letter_la, dikaa, danda	|	
व	|	wa	|	letter_wa, danda, dikaa	|	
श	|	moto_saw	|	letter_sha, danda, dikaa	|	
ष	|	petchiryo_saw	|	letter_pa, petchiryo, danda, dikaa	|	
स	|	patalo_saw	|	letter_ra, terso, danda, dikaa	|	
ह	|	ha	|	letter_ha, dikaa	|	
़	|	nukta	|	nukta	|	
ऽ	|	avagraha	|	avagraha	|	
ॐ	|	symbol_om	|	symbol_om	|	
ॡ	|	ॡ	|		|	
०	|	numeral_shunya	|	numeral_shunya	|	
१	|	numeral_ek	|	numeral_ek	|	
२	|	numeral_dui	|	numeral_dui	|	
३	|	numeral_teen	|	numeral_teen	|	
४	|	numeral_chaar	|	numeral_chaar	|	
५	|	numeral_paanch	|	numeral_paanch	|	
६	|	numeral_chha	|	numeral_chha	|	
७	|	numeral_saat	|	numeral_saat	|	
८	|	numeral_aath	|	numeral_aath	|	
९	|	numeral_nau	|	numeral_nau	|	
॰	|	symbol_abbr	|	symbol_abbr	|	
क्क	|	kka	|	ligature_kka, letter_wa, danda, puchchhar, dikaa	|	ligature
त्त	|	ttta	|	ligature_tta, danda, dikaa	|	ligature
