# Caso: SNAI tennis, best odds autunno 2026 (memoria operativa)

Usa questo file quando l'utente parla di SNAI, tennis, Parigi/Torino o "le grafiche di prima": contiene le decisioni già prese, così non si riparte da zero.

## Contesto
- Cliente: SNAI. 5 tornei; 3 grafiche approvate (fotorealistiche: pallina+racchetta su campo blu; arena wide blu; campo navy golden hour), 2 rifiutate (ATP Finals Torino: collage blu "a incastro"; Masters 1000 Parigi: ombra a forma di albero su verde).
- Formato: 5:4 (circa 1374x1120 le approvate), generate a 2304x1856 con `nano_banana_pro` 2k.
- Zona testo: sinistra/alto pulito, soggetto in basso a destra.

## Brief SNAI per palette
- Masters 1000 Parigi (01/11–08/11): verde scuro e nero, "coerente con l'identità storica del torneo indoor". Reale: Bercy 2024 campo verde, bordo grigio scuro; dal 2025 Paris La Défense Arena (16.500 posti, show Moment Factory, "lights fade to green").
- ATP Finals Torino (15/11–22/11): blu navy / blu notte con dettagli turchese. Reale: Inalpi Arena, 12.000 posti, campo blu ATP, bordo navy.

## Feedback ricevuti e regole derivate
- Torino: "meno coerente, elementi non immediatamente visibili, gioco di incastri" → un soggetto solo, fotoreale, niente collage.
- Parigi: "l'albero non tutti lo capiscono; palette piace; più pulito, più easy" → niente simboli, palette invariata, meno elementi.
- Utente: "rispetta identità e colore del campo"; "non un'altra pallina in primo piano"; "usa reference reali"; "più creatività e impatto restando fotorealistico".

## Esito
- Torino: scelta dall'utente la variante con pallina in primo piano su campo navy (serie 3, T7).
- Parigi: 28 varianti in 5 serie. Serie 4 con reference reali da Wikimedia Commons (Bercy 2024 n.1/5/7/19/22, ingresso giocatori 2017, Bercy 2016 n.2). Serie 5 concept creativi: tunnel, sedia arbitro, linee a filo campo, Tour Eiffel, silhouette al servizio, esterno La Défense sotto la pioggia, tribune vuote, nastro rete. Candidate consigliate: tunnel (P21), linee (P23), esterno La Défense (P26), fasci laser da reference 2016 (P20).
- Indice completo consegnato come `SNAI_tennis_best_odds_alternative.md` (link CDN Higgsfield).

## Lezioni tecniche
- Il CDN Higgsfield e Commons sono bloccati dal proxy locale: QA e descrizione reference via slideshow + video analysis (vedi playbook).
- `media_import_url` vuole URL diretti di Commons (thumb.wikimedia.org), non Special:FilePath.
