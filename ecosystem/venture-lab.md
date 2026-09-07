# ecosystem/venture-lab.md — loop de ideación de producto (RHC)

**Estado:** LOOP PAUSADO desde 2026-09-03. 0 candidatas activas.
**Última actualización:** 2026-09-06

## Qué es
Loop de Claude Code (`/loop` cada 3h, ya eliminado) que scouteaba y scoreaba ideas de producto
solo-founder para Robinhood Chain. Salida = `PROYECTOS-BOARD.md` (backlog rankeado, rúbrica en
`SCORING.md`).

## Resultado
- Encontró **1 idea lista para construir**: **`float-squeeze-radar`** — scanner que mide qué % del float de un stock-token de RHC está bloqueado en la LP de un memecoin emparejado contra él, rankea "presión de squeeze" y alerta. Tier A, score 27. **En construcción por el founder desde 2026-09-08, fuera del loop.** Gate técnico 2026-09-08, abort gate 2026-09-14. Plan completo en `../venture-lab/dossiers/float-squeeze-radar.md` §12.
- Probó con evidencia que el resto del espacio "datos RWA en RHC" está tapado por incumbentes first-party (Robinhood API, robinscan Partner API, DefiLlama). **No hay idea #2 viable ahora.**

## Insumo local (solo lectura)
- `../venture-lab/PROYECTOS-BOARD.md` — backlog.
- `../venture-lab/dossiers/float-squeeze-radar.md` — dossier de la idea graduada.
- `../venture-lab/SCORING.md` — rúbrica (reutilizable para puntuar ideas de 0→10k).
- `../venture-lab/OPEN-QUESTIONS.md` — Q27 y triggers para re-activar el loop.

## Tesis (para 0→10k)
- `float-squeeze-radar` NO es parte de 0→10k por defecto. Es RHC-nativo, requiere subgraph/infra y tiene su propio calendario. **Solo entra a 0→10k si el usuario lo declara apuesta/spike** — en ese caso, sería un frente "build cobrable" fuerte (herramienta con premium + alertas Telegram).
- La metodología de `SCORING.md` sí se reutiliza para rankear ideas nuevas.

## Próxima acción
- Ninguna activa. Si el usuario quiere, evaluar `float-squeeze-radar` como spike de 0→10k (score con la rúbrica de CLAUDE.md, no la de venture-lab).
- Re-mirada de oficio del loop ≈ 2026-11-01 (tras el dividendo de SPY on-chain).

## Kill
- El loop ya cumplió su objetivo. No re-lanzar salvo trigger de Q27 explícito.

## No hacer
- No re-correr el `/loop` de venture-lab desde esta carpeta.
- No duplicar el dossier de float-squeeze-radar acá; se referencia.
