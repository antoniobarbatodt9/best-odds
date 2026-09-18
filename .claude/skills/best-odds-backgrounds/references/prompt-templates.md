# Prompt templates (in inglese) e regole di composizione

## Scheletro universale

```
[STYLE]  Ultra-realistic cinematic photograph | High-end sports key visual | Premium 3D render ...
[SUBJECT + IDENTITY]  scena/oggetto + colore esatto del campo e del bordo + arena/città/rituale
[LIGHT]  single spotlight / emerald wash / rim light / LED ribbon bokeh / haze
[PALETTE]  Palette strictly <c1> and <c2>, <accento>; niente altri colori
[LENS/ANGLE]  24mm low angle | 50mm court level | 85mm f/2 | 100mm macro | high-angle wide
[TEXT ZONE]  The upper left third (or: left half) of the frame is dark and clean for text overlay; subject in the lower right
[EXCLUSIONS]  No people, no text, no logos, no sponsor boards, no readable signage, no graphic shapes (+ no ball in foreground se richiesto)
[QUALITY]  Photoreal, sharp, cinematic, premium
```

Scrivi la zona testo e le esclusioni in ogni prompt: il modello tende a riempire il frame e a inventare scritte sugli LED.

## Prompt con reference reale (image_references)

```
Use the reference photo only as a guide for the real venue and moment: <cosa prendere: architettura, punto di vista, momento del light show>.
Recreate it as an ultra-realistic advertising background: <palette>, <cosa cambia: luci spente, campo vuoto, colore diverso della luce>.
Shift the framing slightly: court in the lower right, upper left third dark and clean for text.
Remove all people, sponsor boards, logos, text, screen content and signage.
```

Il "shift the framing slightly" e il cambio di palette servono a non produrre una copia della foto.

## Esempi collaudati (SNAI tennis 2026)

**Parigi, Masters 1000, palette verde scuro/nero, tunnel dei giocatori**
```
Ultra-realistic cinematic photograph, advertising background. Concept: the players' tunnel. We stand inside the dark concrete entrance tunnel of a large indoor tennis arena, looking out toward the opening in the lower right of the frame: through the opening, the deep dark green hard court with its white lines glows under emerald green spotlights, with a thin haze and the black silhouette of the stands beyond. The tunnel walls and ceiling are near-black, with a faint green rim of light on their edges creating strong leading lines toward the court. No people, no players, no signage, no logos, no text. Palette strictly black and deep dark green, white court lines. 35mm lens, low angle, shallow depth on the tunnel walls, sharp on the court. The upper left two thirds of the frame are black and clean for text overlay. Photoreal, moody, anticipation before the match, premium.
```

**Parigi, linee a filo campo**
```
Ultra-realistic cinematic photograph, advertising background. Concept: the lines. Extreme low angle at surface level on a deep dark green indoor hard court: the white baseline and a sideline meet in the lower right corner of the frame and run away into the distance, converging toward a vanishing point in the dark. Deep emerald green arena light rakes across the acrylic texture, revealing fine grain and tiny scuffs, and the far end dissolves into black haze with soft green bokeh from the arena lights. No ball, no racket, no people, no logos, no text. Palette strictly black and deep dark green, white lines. 24mm lens, f/2, very shallow depth of field, cinematic. The upper left of the frame is black and clean for text. Photoreal, graphic, powerful, premium.
```

**Torino, ATP Finals, palette navy/blu notte + turchese, pallina sulla baseline**
```
Ultra-realistic editorial sports photograph at court level during the ATP Finals night session in Turin. A fluorescent yellow tennis ball rests on the white baseline of a medium ATP-blue hard court in the lower right foreground, sharp, fine acrylic texture visible. Beyond it the court recedes out of focus into a deep navy run-off area, and a perimeter LED ribbon glowing turquoise-cyan forms a soft horizontal bokeh band in the background, the dark arena stands above dissolving into midnight blue. Cool white spotlight from above rims the ball. Palette: ATP blue, navy, midnight blue, turquoise accent, white, yellow. Medium format, 85mm, very shallow depth of field, cinematic. Large clean dark negative space on the left and upper part of the frame for text. No people, no text, no logos, no readable signage, no graphic shapes. Photoreal, clean, premium.
```

**Silhouette senza volto (quando le persone sono ammesse)**
```
... a single tennis player, seen only as a small backlit silhouette at the far baseline in the lower right of the frame, tossing the ball for a serve, face not visible, no recognizable features ...
```

## Regole di composizione per la zona testo

- Soggetto in basso a destra (o in basso al centro per le wide dall'alto); mai nel terzo alto-sinistro.
- Linee guida (linee del campo, tunnel, rete) che partono dal soggetto e puntano verso la zona testo: l'occhio arriva alle quote.
- Gradiente verso il nero nella zona testo: contrasto garantito per testo bianco/colorato.
- Un accento cromatico (pallina gialla, luce turchese) al massimo, lontano dalla zona testo.
- Rapporto d'aspetto uguale alle approvate (di solito 5:4); risoluzione 2k.

## Catalogo inquadrature da alternare

wide dall'alto (arena) · panoramica dagli spalti · livello campo lungo la baseline · linee a filo superficie · tunnel d'ingresso · sedia dell'arbitro · palo e nastro della rete (macro) · racchetta top-down · esterno arena di notte (pioggia, riflessi) · città/landmark sfocato · silhouette controluce · tribune vuote dall'alto.
