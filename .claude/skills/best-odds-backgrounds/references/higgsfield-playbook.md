# Higgsfield MCP playbook per background best odds

Sequenza collaudata (sessione SNAI tennis, settembre 2026). Carica gli strumenti con `ToolSearch` (`select:mcp__HIGGSFIELD_MCP__...`) prima di usarli.

## 1. Setup (una volta per sessione)

- `balance` → crediti disponibili (ogni immagine 2k costa crediti; avvisa l'utente se il batch è grande).
- `models_explore` (`action: recommend`, `type: image`) → conferma il modello. Default:
  - fotoreale: `nano_banana_pro`, `resolution: "2k"`, aspect `5:4` (o quello delle approvate); accetta `image_references`.
  - stilizzato/CGI: `gpt_image_2` (`quality: high`) o `recraft_v4_1` (`colors: ["#0B3D2E","#000000"]`, `model_type: standard|utility`).
- `use_unlim: false` nei batch, salvo richiesta esplicita dell'utente di usare le generazioni unlimited.

## 2. Reference reali (foto del torneo)

1. Trova le foto: `WebSearch` con `site:commons.wikimedia.org <torneo> <arena>` e cerca le categorie per anno (es. `Category:2024 Rolex Paris Masters`).
2. Elenca file e URL diretti dal sandbox Higgsfield (`sandbox_exec`), perché il proxy locale blocca Commons: usa `scripts/commons_refs.sh` (API `action=query&list=categorymembers` + `prop=imageinfo&iiurlwidth=2048`).
3. `media_import_url` accetta solo URL **diretti** (`upload.wikimedia.org` o `thumb.wikimedia.org/.../NNNNpx-...jpg`): `Special:FilePath` fallisce con "Exceeded 2 redirects". Togli i parametri `?utm_...`.
4. Passa il `media_id` in `medias: [{value, role: "image_references"}]`.
5. Cita l'URL della pagina Commons nell'indice di consegna (licenza CC, attribuzione).

Se non riesci a vedere le foto (CDN bloccato), descrivile con il trucco della slideshow (sezione 5) prima di sceglierle: nella sessione SNAI questo ha rivelato che il campo di Bercy 2024 era verde con bordo grigio e quali frame mostravano il light show.

## 3. Generazione

- `generate_image_batch` con `requests[]` (max 12), `index` stabile per evento (1–9 evento A, 11–19 evento B, 21+ serie successive).
- `jobs_wait` (max 12 job, timeout 15s) ripetuto finché `all_terminal`; nel frattempo fai altro (ricerche, indice).
- Una sola `show_generation_by_ids` per l'intero set completato (mai `job_display` per ogni job).
- Salva subito i `result_url` nel file indice: se la sessione si interrompe, i link restano.

## 4. Errori noti

- `media_import_url` + redirect → usa URL diretti.
- `sandbox_exec` timeout 60s di default (max 120): dividi i lavori lunghi o usa `background: true`.
- Il sandbox si resetta ~10s dopo ogni chiamata: fai download → elaborazione → upload nello stesso comando, oppure riscarica.
- `magick` non esiste nel sandbox: usa `convert` (ImageMagick 6) o Pillow.
- `ffmpeg -pattern_type glob` può fallire: usa `-f concat` con lista file.
- `curl` locale verso `*.cloudfront.net`, `wikimedia.org`, siti ATP: 403 dal proxy. Non riprovare, usa il sandbox Higgsfield o `WebSearch`.

## 5. QA senza vedere le immagini (slideshow + video analysis)

Quando non puoi aprire i PNG:

1. `media_upload` (filename `qa.mp4`, `content_type: video/mp4`) → ottieni `upload_url` e `media_id`.
2. `sandbox_exec`: esegui `scripts/slideshow_qa.py` con la lista di URL (immagini generate o reference), che scarica, crea frame 1280x720 numerati "OUT 61 / REF 07", monta un mp4 (3s a frame) e fa il `PUT` sull'`upload_url` nello stesso comando.
3. `media_confirm` (`type: video`), poi `video_analysis_create` (`video_input_id`) e `video_analysis_status` dopo ~60s (usa `sandbox_exec` con `sleep 50` per attendere).
4. Le scene sono in ordine temporale: con 3s a frame, scena k = frame k. Con molti frame simili l'analisi può accorparne alcuni: per i frame ambigui rifai una slideshow corta (5–6 frame).
5. Nel report scrivi cosa dice l'analisi (testo/loghi presenti? persone? palette?) e dichiara che la verifica visiva finale spetta all'utente.

## 6. Consegna

- Indice `.md` nella scratchpad (template in `brief-template.md`), aggiornato ad ogni serie, inviato con `SendUserFile` (`display: attach`).
- Messaggio finale breve: metodo, elenco concept con una riga ciascuno, esito QA, limiti, candidate consigliate, passo successivo.
