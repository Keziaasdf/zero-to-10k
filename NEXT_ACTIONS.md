# NEXT ACTIONS

## ▶ AL PRENDER EL PC (arrancar por acá — orden)
_Pausado 2026-09-08 noche. Todo commiteado y pusheado (HEAD `a1e7cc1`). Working tree limpio._

1. **Relanzar el motor X** si se quiere seguir: `/loop 4h x-growth` en sesión con Chrome. El loop es de-sesión → murió al apagar. (Si no, correr `x-growth` a mano 1×/día.)
2. **IDEATHON — urgente, deadline 2026-09-15** (Superteam Ukraine, 1000 USDG): resolver si el bounty es **global o Ukraine-only**; si aplica, copiar el bloque entre marcadores de `content/drafts/2026-09-06-ideathon-submission.md` al formulario de Superteam Earn. NO enviar sin confirmar elegibilidad.
3. **HUNT local**: `curl -sL "https://superteam.fun/api/listings?type=bounty&take=40"` → actualizar `data/bounties.jsonl` (quitar vencidos, marcar <72h). Manic Bug Bounty vencía 2026-09-09 → probablemente ya cerrado.
4. **Triage de ideas**: scorear I007 / I012 / I013 con la rúbrica de CLAUDE.md; decidir si alguna sube a spike de build.
5. **Kill-check I001 (2026-09-13)**: ¿demo live (✓) + submission IDEATHON enviada? Si no está la submission, es el bloqueante.
6. **Drafts en cola** (no publicar sin `PUBLICA AHORA`): `2026-09-07-post-unrealized-no-es-plata`, `2026-09-08-post-cake-bstocks` (refrescar precio $CAKE), `2026-09-08-post-rhc-claim-scam`, `2026-09-08-post-spark-vibe-season0`.

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

## Motor X `x-growth` (montado 2026-09-08 · loop DETENIDO al apagar el PC — relanzar con `/loop 4h x-growth`)
- [x] Baseline capturado (2026-09-08): 406 seguidores / 1118 siguiendo / impresiones 4W 854 (cayendo desde pico Aug 30). En `data/x-metrics.jsonl`.
- [x] $SPARK confirmado = token del ecosistema **vibe/vibe** (Seedify, narrativa de @meta_alchemist). NO es $SPK. `content/x/INTERESES.md` actualizado.
- [x] Loop: `/loop 4h x-growth` en esta sesión local. Chrome máx 2×/día (baseline + 1 refresco); las demás corridas = research only.
- [ ] Recapturar métricas de perfil cada ~5–7 días → nueva línea en `x-metrics.jsonl` (comparar Δ alcance).
- [ ] Drafts en cola (`content/calendar.md` #7–9): `cake-bstocks` (refrescar precio $CAKE antes de publicar), `rhc-claim-scam`, `spark-vibe-season0`.
- Publicar cualquiera: el usuario escribe `PUBLICA AHORA` + cuál.

## Revisar
- [ ] Kill-check 2026-09-13: ¿demo pública live + submission IDEATHON enviada?
- [ ] Watch blog.colosseum.com: próximo hackathon Colosseum
- [ ] experiments/002: revisión de oficio 2026-11-01
