# Brief template, feedback → regola, indice di consegna

## 1. Modulo intake (compila prima di generare)

```
Operatore: ______  (es. SNAI)
Stile operatore (fase 1a): fotoreale / stilizzato-effetti / CGI / collage / ibrido
Grafiche approvate disponibili: sì/no → cosa hanno in comune (soggetto, luce, palette, zona testo)
Grafiche rifiutate disponibili: sì/no → perché (parole esatte del cliente)
Eventi:
  - Nome, date, sede, superficie/colore campo, palette richiesta dal cliente
  - ...
Formato: rapporto d'aspetto (es. 5:4), risoluzione (2k), n. alternative per evento (default 4–5)
Zona testo: es. terzo alto-sinistro pulito, soggetto in basso a destra
Elementi ammessi: persone/silhouette ☐  pallina in primo piano ☐  landmark città ☐  loghi ☐ (mai)
Vincoli extra: ______
```

## 2. Feedback del cliente → regola operativa

Traduci sempre il feedback in una regola che entra nel prompt. Esempi reali (SNAI, tennis 2026):

| Feedback (parole del cliente) | Regola operativa |
|---|---|
| "Meno coerente rispetto alle altre, gli elementi non sono immediatamente visibili, è un gioco di incastri" | Un solo soggetto leggibile, niente collage/doppie esposizioni/layer trasparenti; stessa grammatica visiva delle approvate (soggetto in basso a dx, fondo scuro) |
| "Quell'albero che sarebbe la forma del torneo non tutti lo capiscono" | Niente forme simboliche da decifrare; identità del torneo tramite colore campo, arena, città, non tramite metafore |
| "La palette piace, però più pulito, più easy" | Mantieni palette; riduci elementi a 1–2; più spazio negativo; luce che modella, non decora |
| "Palette verde scuro e nero coerente con l'identità storica del torneo indoor" | Campo verde scuro o nero, luce smeraldo che "accende" la scena, niente verde neon |
| "Blu navy / blu notte con dettagli turchese" | Campo blu ATP, run-off navy, accenti turchese solo nelle luci (rim light, LED, bokeh) |
| "Non vedo ancora quella che mi fa dire wow" | Cambia leva: inquadratura inedita (tunnel, sedia arbitro, linee a filo campo, esterno arena), momento iconico reale usato come reference, o overlay ibrido. Non un'altra pallina in primo piano |
| "Rispetta l'identità dei tornei, colore del campo ecc." | Ricerca reale (fase 1b) prima di ogni prompt; scrivi nel prompt il colore esatto del campo e del bordo |

## 3. Template dell'indice di consegna (file .md inviato con SendUserFile)

```
# <Operatore> Best Odds <sport> – <evento/i> (Higgsfield, <modello>, <res>, <aspect>)

## Scheda di analisi
- Stile operatore: ...
- Identità evento: campo ..., bordo ..., arena ..., rituali ..., città/periodo ...
- Palette: ...
- Zona testo: ...
- Regole da feedback: ...

## Serie 1 – <evento> – <direzione>
| # | Concept | Leva percettiva | Zona testo | Reference (URL) | PNG |
|---|---------|-----------------|------------|-----------------|-----|

## QA (analisi automatica)
- Cosa è stato verificato, cosa non è verificabile
## Candidate consigliate
- P.., P.. : perché
```

Aggiungi una sezione "Serie N" per ogni giro di feedback, non sovrascrivere: l'utente vuole mostrare al cliente l'evoluzione.
