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

## Feedback del 22/09 (serie 6)
- SNAI: le due nuove creatività (Parigi P28 palo rete + racchetta; Torino T7 pallina sulla baseline) "vanno molto meglio", ma le strisce LED illuminate "sono in contrasto con le grafiche precedenti approvate". Chiesto di lavorare su "sfumature, bagliori e cose simili, come nelle grafiche che ci piacciono molto" (Shanghai, Six Kings Slam).
- Regola: mai fasce/strisce LED o bokeh a punti; lo sfondo è un gradiente morbido con bloom diffuso nel colore del brief (Parigi verde scuro su nero, Torino turchese tenue su navy/blu notte); la scena scelta dal cliente non si tocca.
- Tecnica: edit con `nano_banana_pro` passando il `job_id` dell'immagine scelta come `image_references` e prompt "Edit the reference image while keeping its exact composition ... remove ... replace the background with a smooth gradient and diffuse glow". Tre gradi: fedele, atmosferica, reinterpretata.
- Nota operativa: due job del batch sono rimasti "in_progress" oltre 5 minuti; rilanciati come nuovi job con stesso prompt (funziona, non attendere all'infinito).

## Feedback utente del 22/09 (serie 7): il bagliore deve essere motivato
- Le varianti a "sfumatura/bagliore" della serie 6 sono state bocciate dall'utente: "nubi buttate lì", senza significato tecnico di design.
- Regola di design: il colore del brief entra come luce di scena reale (proiettore d'arena con gel colorato, fuori campo o visibile come punto luce), con caduta naturale sul campo, rim light sugli oggetti, bloom dell'ottica solo dove entra la sorgente, foschia solo dentro il fascio, spalti spenti. Mai gradienti dipinti, fog o smoke generici.
- Prompt pattern: "Relight the scene like a professional sports photographer: one floodlight fitted with a <colour> gel mounted high behind ..., pointing back toward the camera ... natural falloff ... restrained realistic lens bloom ... no fog clouds, no smoke, no painted glow".

## Serie 8 (22/09): coerenza con le approvate Shanghai e Six Kings Slam
- Le due approvate: (1) Shanghai = arena wide dalla tribuna alta, campo centrato in basso, tilt-shift sugli spalti, grading blu monocromo, piccoli spot sul tetto, vignettatura; (2) Six Kings Slam = top-down su campo navy texturizzato (grana asfalto), linea bianca a sinistra, racchetta che entra dall'alto a destra con luce radente calda e ombra lunga delle corde, pallina in basso a destra, testo a sinistra.
- Metodo che funziona: caricare le approvate con `media_upload` + `media_confirm` (il PUT su S3 dalla macchina locale passa) e usarle come `image_references` con prompt "Match the style, framing, lens, grading and mood of the reference exactly; change only the identity to <torneo>: <colore campo/bordo/tinta luce>". Due famiglie per torneo, con una variante di angolo o di tinta luce ciascuna.
- Nota: i job con reference webp sono rimasti bloccati "in_progress"; rilanciati identici, completati in 1 minuto.

## Serie 9 (22/09): il "bagliore" richiesto è un color grade, non una luce
- Chiarimento dell'utente: SNAI, con "sfumature e bagliori come nelle grafiche approvate", intende il filtro cromatico naturale di Shanghai (tono blu unificato su tutta la foto) e del Six Kings (tinta portata dalla luce), che cambia l'atmosfera senza stravolgere la foto e senza nebbie.
- Metodo corretto: edit con DUE reference (job dell'immagine da correggere + approvata come riferimento di grading) e prompt "The first image is the photograph to edit; the second image is only a colour-grading reference ... remove the LED strip and replace it with the natural dark perimeter wall and unlit seats ... apply one unified natural tonal filter like the second image ... it must read like a colour grade on a real photo, not added light: no fog, no glow, no smoke, no new light sources". Tre gradi: grade unificato, tinta nella luce esistente, grade bilanciato con pochi spot lontani.

## Serie 10 (22/09): Torino "troppo scolastica"
- Lezione: quando la scena base è piatta (pallina sulla baseline con luce frontale), nessun grading la salva. Serve rifare l'art direction: camera a filo campo, luce direzionale scolpita (key fredda + controluce colorato che disegna il rim e l'ombra lunga), micro-texture leggibile, un "momento" (rimbalzo congelato con polvere) invece di una posa. Prompt con vocabolario da produzione: "premium advertising photograph, medium format, 100mm f/2, editorial retouching quality, tack sharp, micro-contrast".
- Reference doppia utile: immagine promossa dal cliente (soggetto/palette) + approvata di craft più alto (Six Kings) per il livello di luce e texture.

## Serie 11 (22/09): regola ferrea sulle correzioni
- Errore da non ripetere: quando il cliente chiede di "modificare" una grafica, l'inquadratura e la scena restano quelle. Non proporre concept nuovi al posto della correzione; i concept nuovi si offrono a parte, se richiesti.
- Chiedere sempre all'utente il file esatto da correggere (può essere diverso dall'ultima generazione: qui la base Torino era un'immagine 4:3 con arena piena e spot sul tetto, non il job T7). Caricarla con media_upload dal disco locale (funziona) e usarla come prima reference; approvata come seconda reference solo per il grading.
- Aspect ratio della generazione = aspect ratio della base (qui 4:3), altrimenti il modello reinquadra.
