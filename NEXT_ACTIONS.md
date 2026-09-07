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

## Próxima corrida (BUILD / cuando Pages esté live)
- [ ] Verificar la URL de Pages y pegarla en: SafeCheck README, drafts de content (reemplazar `<URL>`), submission IDEATHON.
- [ ] Enviar submission al **Superteam Ukraine IDEATHON** (formulario en Superteam Earn) — antes del **2026-09-15**. Revisar si el bounty es global o chapter-only.
- [ ] Revisar `data/bounties.jsonl`: quitar lo vencido, marcar lo que vence <72h.
- [ ] (Opcional) Buscar fuente gratuita browser-CORS para "top holders". Si no hay → queda n/d. NO pedir ni hardcodear API keys.

## Rutina diaria — /schedule (NO disparado; el usuario decide)
Cron disponible en este plan (verificado con CronList). Para automatizar la corrida diaria, el usuario puede correr:

```
/schedule cada día a las 09:00 America/Santiago: abre la carpeta zero-to-10k y ejecuta la skill daily-loop (comando DAILY). Sin subagentes. Chrome solo en el hilo padre y solo si un dato lo exige. No publicar en X. Commit local al final; push solo si el repo es público.
```

O el equivalente con la skill `schedule`. **No lo lancé** — dejarlo a criterio del usuario.

## Revisar
- [ ] Kill-check 2026-09-13: ¿demo pública live + submission IDEATHON enviada?
- [ ] Watch blog.colosseum.com: próximo hackathon Colosseum
- [ ] experiments/002: revisión de oficio 2026-11-01
