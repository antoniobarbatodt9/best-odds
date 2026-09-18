---
name: best-odds-backgrounds
description: Workflow completo per creare background grafici di banner "best odds" (quote scommesse) per operatori di betting (SNAI e altri) con Higgsfield MCP. Usa questa skill ogni volta che l'utente chiede grafiche, banner, background, visual o immagini per best odds, quote, tornei, partite o campagne sportive di un cliente betting, anche se non dice esplicitamente "best odds" o "background" (es. "mi servono le grafiche per gli ATP Finals", "rifammi il banner di Parigi", "SNAI ha dato feedback sulle immagini"). Copre analisi preliminare dello stile dell'operatore, ricerca dell'identità reale del torneo, scelta fra fotorealismo e stili stilizzati (glow, motion, CGI, collage), intervista guidata, generazione batch su Higgsfield, QA e ciclo di feedback.
---

# Best Odds Backgrounds

Produci background per banner "best odds": immagini su cui il cliente sovrappone quote, loghi e testo. La grafica non è mai il messaggio, è il palco del messaggio. Tutto il workflow serve a ottenere immagini impattanti, coerenti con l'identità del torneo e dell'operatore, e con una zona pulita e leggibile per il testo.

Il processo ha 6 fasi. Non saltare la fase 1 e la fase 2: sono quelle che evitano di generare venti immagini nella direzione sbagliata.

## Fase 0. Intake: cosa ti serve prima di iniziare

Raccogli o deduci dal messaggio dell'utente:

- **Operatore/cliente** (es. SNAI) e se esistono grafiche già approvate o rifiutate. Le approvate sono il riferimento di stile più affidabile che avrai: analizzale prima di qualsiasi altra cosa.
- **Eventi/tornei** e date. Le date contano: il pubblico deve collegare l'immagine al momento in cui la campagna gira.
- **Brief del cliente** (palette, mood, indicazioni verbali riportate da account/responsabile). Trascrivi le parole esatte: "verde scuro che sembra illuminare la scena" è più utile di "verde".
- **Feedback precedenti** e la loro traduzione operativa (vedi tabella in `references/brief-template.md`).
- **Formato**: rapporto d'aspetto delle grafiche approvate (spesso 5:4 o 4:5), dove va il testo, quante alternative servono.

Se mancano informazioni decisive (operatore, torneo, stile) fai le domande della **Fase 2**. Se invece il messaggio è già completo, riassumi in 5 righe ciò che hai capito e procedi.

## Fase 1. Analisi preliminare (obbligatoria)

Prima di generare, costruisci una scheda in tre parti. Scrivila nel file indice di consegna (vedi Fase 5), così resta tracciata.

### 1a. Stile dell'operatore
Ogni operatore ha un'impronta. Classificala usando `references/style-directions.md`:

- **Fotorealistico editoriale** (es. SNAI tennis 2026): foto vere o indistinguibili da foto, luce cinematografica, palette scura, un solo soggetto leggibile.
- **Stilizzato / effetti**: glow, strisce di luce, motion blur, livelli di colore, mix pallina+racchetta con elementi grafici, grading neon.
- **CGI / 3D render**: oggetti renderizzati, materiali lucidi, studio light, sfondi astratti.
- **Collage / cut-out**: elementi ritagliati e composti, tipografico, layer sovrapposti.
- **Ibrido**: foto reale + overlay grafici (linee, particelle, gradienti).

Deducilo da: grafiche approvate, sito e social dell'operatore, campagne precedenti. Se non hai materiale, proponi 2 direzioni opposte (una fotoreale, una stilizzata) come primo test da 2–3 immagini ciascuna, prima di investire su un batch grande.

### 1b. Identità reale del torneo/evento
Le persone devono riconoscere il torneo a colpo d'occhio. Ricerca sempre:

- colore reale del campo e del bordo campo (es. Bercy 2024: campo verde, bordo grigio scuro; Inalpi Arena Torino: campo blu ATP, bordo navy);
- sede, dimensioni, architettura (tetto, tribune, LED perimetrali, maxischermi);
- rituali visivi del torneo (ingresso giocatori con proiezioni sul campo, light show, night session);
- città e periodo (novembre a Parigi, neve sulle Alpi a Torino, ecc.);
- palette del brand del torneo.

Fonti in ordine di affidabilità: brief del cliente, siti ufficiali, ATP/WTA/lega, Wikimedia Commons (foto con licenza CC riutilizzabili come reference), stampa sportiva, social. Nel sandbox remoto molti siti sono bloccati dal proxy: usa `WebSearch` per i testi e le API di Commons dal sandbox di Higgsfield per le foto (procedura in `references/higgsfield-playbook.md`).

### 1c. Vincoli di leggibilità
Definisci esplicitamente la **zona testo**: quale parte del frame resta scura/pulita (di norma il terzo alto-sinistro o l'intera metà sinistra) e dove sta il soggetto (in basso a destra, o in basso al centro per le wide). Questo vincolo entra in ogni prompt.

## Fase 2. Intervista guidata

Fai al massimo 5 domande, solo quelle che cambiano davvero il lavoro. Proponi sempre un'opzione consigliata così l'utente può rispondere "ok".

1. Stile: fotorealistico, stilizzato/effetti, CGI, collage, ibrido? (mostra la classificazione della fase 1a e la tua raccomandazione)
2. Palette per evento: la fornisce il cliente o la deduci dall'identità del torneo?
3. Elementi ammessi: persone/silhouette sì o no? pallina in primo piano sì o no? città/landmark sì o no?
4. Formato e zona testo: rapporto d'aspetto, dove vanno le quote.
5. Quantità: quante alternative per evento (default 4–5) e se servono varianti di un concept scelto.

Se l'utente ha già dato feedback del cliente, traducilo in regole operative prima di procedere (vedi tabella "Feedback → regola" in `references/brief-template.md`).

## Fase 3. Progettazione dei concept

Lavora come un art director, non come un generatore di prompt. Per ogni evento progetta 4–8 concept diversi per inquadratura e idea emotiva. Per ciascuno annota:

- **Idea** (una frase): "il tunnel dei giocatori prima dell'ingresso".
- **Leva percettiva**: linee convergenti, singolo punto luce, profondità con foschia, simbolo riconoscibile, scala, dettaglio tattile.
- **Aggancio all'identità**: colore campo, arena, città, rituale del torneo.
- **Composizione**: soggetto in basso a destra, zona testo in alto a sinistra, nessun elemento nella zona testo.

Varia sistematicamente: wide dall'alto, livello campo, macro, esterno arena, città, dettaglio oggetto, silhouette. Non consegnare cinque varianti della stessa inquadratura. Evita composizioni "a incastro", doppie esposizioni e forme simboliche da decifrare: nei banner best odds il cliente vuole leggibilità immediata.

Scrivi i prompt in inglese con la struttura in `references/prompt-templates.md`. Ogni prompt dichiara: stile, soggetto, luce, palette rigorosa, obiettivo/lente, zona testo, esclusioni (no text, no logos, no people/faces, no sponsor boards).

## Fase 4. Generazione con Higgsfield MCP

Segui `references/higgsfield-playbook.md`. In sintesi:

1. `models_explore` una volta per sessione per confermare il modello (default fotoreale: `nano_banana_pro`, resolution `2k`; per stili stilizzati/CGI valuta `gpt_image_2` o `recraft_v4_1` con `colors` di palette).
2. Foto reali come reference: `media_import_url` con URL diretti (no redirect) e ruolo `image_references`; prompt che dice esplicitamente "use the reference only as a guide for the venue, change palette/framing, remove people/logos".
3. `generate_image_batch` con indici stabili per evento (es. 1–9 Parigi, 11–19 Torino), max 12 per batch, `use_unlim: false` salvo indicazione dell'utente.
4. `jobs_wait` a gruppi, poi **una sola** `show_generation_by_ids` per l'intero set.
5. Salva ogni URL in un file indice markdown (vedi Fase 5) man mano che arrivano.

## Fase 5. QA e consegna

Nel sandbox remoto il CDN di Higgsfield è spesso bloccato per il tuo ambiente: non puoi aprire i PNG. Non fingere di averli visti. Usa il **QA via analisi video**: monta le immagini in una slideshow nel sandbox Higgsfield, caricala con `media_upload` + `media_confirm`, lancia `video_analysis_create` e leggi le descrizioni scena per scena (script pronto in `scripts/slideshow_qa.py`). Cerca: testo o loghi comparsi, persone riconoscibili, palette fuori brief, soggetto nella zona testo, colori "neon" dove era chiesto "scuro".

Consegna sempre:

- la galleria Higgsfield (la vede l'utente);
- un file indice `.md` con: scheda di analisi (Fase 1), tabella per evento con numero, concept, leva percettiva, zona testo, reference usata (URL) e PNG; note di QA; le tue 2–3 candidate consigliate con il perché.
- Invia il file con `SendUserFile` e chiudi con un messaggio breve: cosa hai fatto, cosa segnala il QA, cosa non hai potuto verificare, passo successivo proposto.

## Fase 6. Ciclo di feedback

Quando arriva un feedback (dall'utente o riportato dal cliente):

1. Traducilo in regole operative esplicite e ripetile all'utente in 2–3 righe.
2. Non rigenerare tutto: individua i concept promossi e produci 2–3 varianti ciascuno (angolo, intensità luce, quantità di foschia), più 1–2 concept nuovi se il feedback apre una direzione.
3. Aggiorna il file indice con una nuova sezione "Serie N" invece di sovrascrivere: il cliente vuole vedere l'evoluzione.
4. Se il feedback è "manca il wow", cambia leva: inquadratura inedita, reference reale di un momento iconico del torneo, o un cambio di stile (da fotoreale a ibrido con overlay), non un altro giro della stessa scena.

## File di riferimento

- `references/brief-template.md`: modulo intake, tabella feedback→regola, template dell'indice di consegna.
- `references/style-directions.md`: le direzioni di stile con blocchi di prompt per ciascuna (fotoreale, glow/motion, CGI, collage, ibrido) e cosa evitare.
- `references/prompt-templates.md`: scheletri di prompt in inglese, esempi collaudati (Parigi verde/nero, Torino navy/turchese), regole di composizione per la zona testo.
- `references/case-snai-tennis-2026.md`: memoria del caso SNAI tennis 2026 (palette, feedback, cosa è stato scelto): leggilo quando l'utente cita SNAI, Parigi, Torino o lavori precedenti.
- `references/higgsfield-playbook.md`: sequenza esatta degli strumenti Higgsfield, modelli, parametri, import reference, ricerca foto su Wikimedia Commons, QA via video analysis, errori noti.
- `scripts/slideshow_qa.py`: script da eseguire nel sandbox Higgsfield per costruire la slideshow di QA (o di analisi delle reference).
- `scripts/commons_refs.sh`: elenca file e URL diretti di una categoria Wikimedia Commons dal sandbox.
