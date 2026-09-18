# Direzioni di stile per background best odds

Ogni operatore ha un'impronta. Scegli la direzione in fase 1a e usa i blocchi di prompt qui sotto. Tutti i blocchi vanno chiusi con la clausola di composizione (`prompt-templates.md`): zona testo pulita, soggetto in basso a destra, no text/logos.

## A. Fotorealistico editoriale (default per SNAI tennis)

Quando: le grafiche approvate sembrano foto, il cliente parla di "reale", "fotografico", "altissima qualità".

Caratteri: un solo soggetto; luce cinematografica low-key; palette scura a 2 colori + 1 accento (pallina); texture credibili (grana del campo, feltro, corde); profondità (haze, bokeh); nessun elemento grafico.

Blocco prompt:
```
Ultra-realistic cinematic photograph, advertising background plate for typography overlay.
<soggetto e scena reale, colore esatto di campo e bordo>
<luce: single spotlight / emerald wash / rim light; haze>
Palette strictly <colore 1> and <colore 2>, <accento>.
<lente: 24/35/50/85/100mm>, <angolo>, shallow depth of field.
```

Modelli: `nano_banana_pro` (2k) come default; `kling_omni_image` alternativa; reference reali via `image_references`.

Evita: verde/blu neon uniforme, campi "flooded" di luce, più di un soggetto, oggetti fluttuanti.

## B. Stilizzato con effetti (glow, motion, strisce di luce, livelli di colore)

Quando: l'operatore usa visual "energici", social-first, con bagliori e scie; il cliente dice "più dinamico", "più effetti", "più moderno".

Caratteri: soggetto fotografico (pallina, racchetta, giocatore in silhouette) + overlay luminosi: light streaks, motion trails, particelle, gradient duotone, chromatic glow, speed lines, doppia esposizione controllata (mai "a incastro" indecifrabile).

Blocco prompt:
```
High-end sports key visual, photographic subject with graphic light effects.
<soggetto> frozen in motion, <direzione del movimento> leaving long <colore> light trails and fine particles,
duotone grading <colore 1>/<colore 2>, subtle chromatic glow on edges, dark gradient background,
clean vector-like light streaks (3–5, not more), lens flare restrained.
```

Modelli: `nano_banana_pro` regge bene gli overlay; `gpt_image_2` (quality high) per effetti puliti; `recraft_v4_1` (`model_type: standard`, `colors: [#...]`) per controllo esatto della palette.

Regole: gli effetti seguono il movimento del soggetto, non lo attraversano; max 2 colori di luce; la zona testo resta a gradiente piatto.

## C. CGI / 3D render

Quando: l'operatore ha un look "pulito da studio" (oggetti perfetti, materiali lucidi, sfondi astratti), tipico di app e siti betting moderni.

Caratteri: oggetti 3D (pallina, racchetta, trofeo stilizzato senza loghi) su set astratto, studio lighting a 3 punti, materiali PBR, riflessi controllati, sfondo a forme geometriche o gradient mesh.

Blocco prompt:
```
Premium 3D render, octane/redshift look, studio lighting, <oggetto> with realistic PBR materials
(felt, carbon, gloss), floating above a dark <colore> abstract set with soft geometric shapes,
subtle rim light <colore accento>, clean gradient background, high contrast, no text.
```

Modelli: `gpt_image_2` o `recraft_v4_1` (`utility` per look pulito); `generate_3d` solo se serve un asset riutilizzabile.

## D. Collage / cut-out / tipografico

Quando: l'operatore usa layer ritagliati, texture carta/halftone, elementi sovrapposti. Rischioso per i best odds: la leggibilità cala facilmente.

Caratteri: 2–3 elementi ritagliati con bordo netto, un pattern di sfondo (halftone, strisce), palette piatta a 3 colori.

Blocco prompt:
```
Editorial sports collage, cut-out photo of <soggetto> with hard edges over a flat <colore> background
with <halftone/stripe> pattern, two overlapping color blocks, printed poster feel, no text.
```

Modelli: `recraft_v4_1` (`vector`/`standard`) per forme piatte; `nano_banana_pro` per il cut-out fotografico.

Regole: mai più di 3 layer; il pattern non entra nella zona testo.

## E. Ibrido: foto reale + overlay grafico leggero

Quando: il cliente vuole "fotoreale ma con più impatto". È il compromesso più sicuro dopo un feedback "manca il wow" su uno stile fotoreale.

Caratteri: scena fotoreale (direzione A) + un solo overlay: linee di luce che seguono le linee del campo, particelle nella foschia, bordo LED più marcato, leggero glow sull'accento.

Blocco prompt: prendi il blocco A e aggiungi una sola riga:
```
Add a single restrained graphic accent: <thin light lines following the court lines / floating dust in the beam / a soft glow halo around the ball>, still photoreal.
```

## Cosa evitare in tutte le direzioni

- Composizioni "a incastro" con più soggetti sovrapposti e trasparenze (feedback SNAI: "meno coerente, elementi non immediatamente visibili").
- Forme simboliche da interpretare (l'albero-tabellone: "non tutti lo capiscono").
- Testo, loghi, sponsor, volti riconoscibili di giocatori reali.
- Soggetto o effetti dentro la zona testo.
- Palette "neon" quando il brief dice "scuro"; verde/blu uniforme che appiattisce l'immagine.
