# NEXT ACTIONS

## ▶ AL PRENDER EL PC (arrancar por acá — orden)
_Pausado 2026-09-08 noche. Todo commiteado y pusheado. Working tree limpio. Ver `BRIEFING/2026-09-08.md`._
_El loop `x-growth` (job de sesión `cbd21e5e`) MURIÓ al apagar el PC — no vuelve solo._

1. **Relanzar el motor X**: `/loop 4h x-growth` en sesión con Chrome logueado. (O correr `x-growth` a mano.)
   La 1ª corrida con Chrome debe: (a) recapturar alcance de los posts vivos a 48h → `data/x-posts.jsonl`;
   (b) harvest de likes/bookmarks nuevos → `data/x-engage.jsonl`.
2. **Posts vivos a vigilar** (publicados 2026-09-08, EN):
   - spark-vibe-season0 v3 → `x.com/KeziaQl1/status/2097486155897827347`
   - cake-bstocks → `x.com/KeziaQl1/status/2097465822390218953`
3. **Memes vibe/vibe (Grok, en tu otra sesión)**: generar los briefs pendientes.
   - Listo en draft: **M3** en `content/drafts/2026-09-08-post-vibe-coded-bots-correlation.md` (`## Image brief (Grok)`).
   - Banco M1/M2/M4/M5 en `content/x/imagenes.md` — desarrollar prompt y generar.
   - Al tener la imagen: pegar el prompt final al draft + fila en el log de `imagenes.md`. Se sube al publicar.
4. **IDEATHON — deadline 2026-09-15** (Superteam Ukraine, 1000 USDG): resolver si es **global o Ukraine-only**; si aplica, copiar el bloque de `content/drafts/2026-09-06-ideathon-submission.md` al formulario. NO enviar sin confirmar elegibilidad.
5. **HUNT local**: `curl -sL "https://superteam.fun/api/listings?type=bounty&take=40"` → actualizar `data/bounties.jsonl`. Manic Bug Bounty vencía 2026-09-09 → probablemente cerrado.
6. **Kill-check I001 (2026-09-13)**: ¿demo live (✓) + submission IDEATHON enviada? La submission es el bloqueante.
7. **Drafts EN en cola** (no publicar sin `PUBLICA AHORA <slug>`):
   - `2026-09-08-post-vibe-coded-bots-correlation` (P2, lleva imagen M3)
   - `2026-09-08-post-rhc-claim-scam` (P2, evergreen)
   - `$NPC` — solo idea I013, falta escribir el draft
   - viejos: `2026-09-07-post-unrealized-no-es-plata` (ES, reescribir a EN si se publica)

### Reglas que quedaron fijadas esta sesión (2026-09-08)
- **Posts de X siempre en INGLÉS.** Notas internas pueden ir en español.
- **Cashtag `$SPARK`**: al escribirlo en el composer, esperar el dropdown y **click en la 1ª opción** (contract `…8248`, Base) o enruta a Spark Protocol ($SPK). Paso a paso en `.claude/skills/publish/SKILL.md` §"Al publicar".
- **$SPARK contract** = `0x0FB07c88Bc6d195c196279523957C004eb868248` (Base, ~$0.00157). Incluirlo en el texto.
- X permite **editar posts hasta 1h** después de publicar.
- Motor de contenido: índice en `content/x/README.md`. Workflow de imágenes en `content/x/imagenes.md`.

---

## Hechas (2026-09-06)
- [x] Setup + repo GitHub + Chrome desbloqueado en hilo padre
- [x] Primera lectura de X → x-feed.jsonl, ideas.jsonl
- [x] Apuesta activa I001 + 2 spikes
- [x] I001 SafeCheck v0 funcional (mint/freeze authority + liquidez reales; holders/bundle n/d honesto); probado BONK/USDC
- [x] HUNT: TxODDS descartado; 7 bounties abiertos → data/bounties.jsonl
- [x] INFRA BLITZ: CLAUDE.md (constitución MAIN), MAP.md, ecosystem/{spark-rhc,robinhood-chain,venture-lab,x-account}.md
- [x] .claude/skills/{daily-loop,ingest-x,publish,hunt}
- [x] experiments/002-spark-rhc-watch/ (README + tracker read-only)
- [x] content/{calendar.md,queue.jsonl} + 5 drafts en content/drafts/
- [x] SafeCheck: og:tags + meta description + canonical + favicon + copy ES pulida + index.html redirect en raíz del repo

## HAZLO TÚ EN GITHUB (a mano, ~5 clicks)
**A. Repo público** — ✅ YA ESTÁ (verificado con `gh`: visibility = PUBLIC). Nada que hacer.

**B. GitHub Pages** (esto sí falta)
1. github.com/Keziaasdf/zero-to-10k → **Settings**
2. Menú izq → **Pages**
3. **Source**: "Deploy from a branch"
4. **Branch**: `main` · carpeta `/ (root)` · **Save**
5. Esperá ~1 min y abrí: `https://keziaasdf.github.io/zero-to-10k/experiments/001-solana-safecheck/`
   (y `https://keziaasdf.github.io/zero-to-10k/` que redirige ahí).

> El repo NO contiene llaves, seeds ni direcciones de wallet: docs + una página estática read-only. Ya es público y open-source por diseño.

## Próxima corrida (BUILD)
- [x] Pages live + URL canónica pegada en README, drafts y submission (2026-09-06).
- [ ] Enviar submission al **Superteam Ukraine IDEATHON** — copiar el bloque entre marcadores de `content/drafts/2026-09-06-ideathon-submission.md` al formulario de Superteam Earn. Antes del **2026-09-15**. PRIMERO revisar si el bounty es global o Ukraine-only.
- [ ] Revisar `data/bounties.jsonl`: quitar lo vencido, marcar lo que vence <72h.
- [ ] (Opcional) Buscar fuente gratuita browser-CORS para "top holders". Si no hay → queda n/d. NO pedir ni hardcodear API keys.

## Rutina diaria — cron MATADO 2026-09-08
- Routine cloud `trig_01EFCGHwx3wAj8wtPMJv1xih` **DESACTIVADA** (`enabled:false`). No vuelve a correr.
  - Motivo: el entorno cloud bloquea `superteam.fun` (egress) → no puede hacer HUNT; y `git push` daba 403 (sin acceso GitHub write) → los commits se perdían.
  - Para borrarla del todo (opcional): https://claude.ai/code/routines → eliminar. Desactivada ya no gasta corridas.
- **HUNT ahora vive 100% local**, como paso 5 de la skill `daily-loop` (curl a la API de Superteam desde esta máquina, que sí tiene salida). El briefing también se escribe en la sesión local.

## Motor X `x-growth` (montado 2026-09-08 · loop `cbd21e5e` MUERTO al apagar el PC — relanzar con `/loop 4h x-growth`)
- [x] Baseline (2026-09-08): 406 seguidores / 1118 siguiendo / impresiones 4W 854 (cayendo desde pico 30-ago). `data/x-metrics.jsonl`.
- [x] $SPARK = token vibe/vibe, contract `0x0FB07c88Bc6d195c196279523957C004eb868248` (Base). Técnica de dropdown para el cashtag guardada en `publish/SKILL.md`.
- [x] Posts de X en **inglés** (regla fija).
- [x] Motor indexado: `content/x/README.md`. Workflow de imágenes/memes (Grok): `content/x/imagenes.md` + `## Image brief (Grok)` en el formato de draft.
- [x] Publicados 2026-09-08 (EN): spark-vibe-season0 v3 (P3), cake-bstocks (P3). Registro en `data/x-posts.jsonl`.
- [ ] Recapturar métricas de perfil + de los 2 posts vivos a 48h → nuevas líneas en `x-metrics.jsonl` / `x-posts.jsonl`.
- [ ] Generar imágenes en Grok (M3 listo en el draft de vibe-coded-bots; M1/M2/M4/M5 en `imagenes.md`).
- [ ] Drafts EN en cola: `vibe-coded-bots-correlation` (P2 + img), `rhc-claim-scam` (P2), `$NPC` (falta escribir).
- Publicar cualquiera: `PUBLICA AHORA <slug>`.

## Revisar
- [ ] Kill-check 2026-09-13: ¿demo pública live + submission IDEATHON enviada?
- [ ] Watch blog.colosseum.com: próximo hackathon Colosseum
- [ ] experiments/002: revisión de oficio 2026-11-01
