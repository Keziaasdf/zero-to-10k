# NEXT ACTIONS

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

## Rutina diaria — /schedule (CREADA 2026-09-06)
- Routine cloud: **"zero-to-10k daily-auto (HUNT + briefing)"** · id `trig_01EFCGHwx3wAj8wtPMJv1xih`
- Cron `0 12 * * *` UTC = **09:00 America/Santiago**. Próxima corrida: 2026-09-07 ~09:02.
- Panel: https://claude.ai/code/routines/trig_01EFCGHwx3wAj8wtPMJv1xih
- **Qué hace (nube, sin Chrome/X):** HUNT vía API pública de Superteam Earn → actualiza `data/bounties.jsonl` (cierra vencidos, agrega abiertos), escribe `BRIEFING/<hoy>.md` con top-3 bounties + pendientes para la sesión local, ajusta NEXT_ACTIONS si algo venció, commit + push a master.
- **Qué NO hace (queda para la sesión local interactiva):** leer X, build de SafeCheck, publicar drafts, enviar la submission del IDEATHON, cualquier cosa con Chrome/wallet.
- Para pausar/editar/borrar: el panel de arriba o pedirlo en sesión.

## Motor X `x-growth` (montado 2026-09-08)
- [ ] **Sesión local:** correr `X GROWTH` una vez para capturar **baseline** en `data/x-metrics.jsonl` (seguidores, siguiendo, impresiones_30d si carga analytics). Sin baseline no se mide crecimiento.
- [ ] Confirmar con el usuario a qué token se refiere **$SPARK** (¿Spark Protocol `$SPK` — airdrop cerrado —, un token nuevo, o "ecosistema vibe/vibe"?). Ajustar `content/x/INTERESES.md`.
- [ ] Elegir cómo loopea (una de dos, o ambas):
  - Local diario: `/loop x-growth` en sesión con Chrome, o sumar `x-growth` como paso 4.5 de `daily-loop`.
  - Cloud: sumar la **Lane RESEARCH** (research + drafts, sin métricas) a la routine `trig_01EFCGHwx3wAj8wtPMJv1xih`. La captura de alcance NO puede ir a cloud (necesita Chrome logueado).
- [ ] Revisar drafts nuevos: `2026-09-08-post-cake-bstocks` (verificar números en DexScreener), `2026-09-08-post-rhc-claim-scam`.
- Publicar cualquiera de ellos: el usuario escribe `PUBLICA AHORA` + cuál.

## Revisar
- [ ] Kill-check 2026-09-13: ¿demo pública live + submission IDEATHON enviada?
- [ ] Watch blog.colosseum.com: próximo hackathon Colosseum
- [ ] experiments/002: revisión de oficio 2026-11-01
