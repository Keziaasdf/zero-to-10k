# content/x/metricas.md — medición de alcance @KeziaQl1

Objetivo medible: **1 post/día** y alcance creciente semana a semana.
La captura de métricas necesita Chrome logueado como el usuario → **solo en sesión local interactiva**
(la lane cloud no puede leer X). Límites de navegación de siempre: 8-12 min, 40 posts, 8 perfiles, 3 búsquedas.

## Archivos

### `data/x-metrics.jsonl` — foto del perfil (1 línea por captura, ~1/semana)
```json
{"ts":"YYYY-MM-DD","seguidores":0,"siguiendo":0,"posts_30d":0,"impresiones_30d":null,"tasa_engagement":null,"post_top_30d":"","nota":""}
```
`impresiones_30d` y `tasa_engagement`: de x.com/i/account_analytics si está disponible; si no, `null` y se estima con la suma de `x-posts.jsonl`.

### `data/x-posts.jsonl` — 1 línea por post propio publicado, + snapshots de métricas
```json
{"ts":"YYYY-MM-DD","url":"https://x.com/KeziaQl1/status/...","slug":"content/drafts/...","pilar":"P1|P2|P3|P4","tipo":"hilo|post|quote|reply","capturado":"YYYY-MM-DD","impresiones":0,"likes":0,"rt":0,"replies":0,"guardados":0,"clicks_perfil":0,"follows_atribuidos":null,"nota":""}
```
Re-capturar a las ~48h y a los ~7d del post. Nueva línea por snapshot (no editar la vieja).

### `data/x-engage.jsonl` — likes/bookmarks del usuario → señal
```json
{"ts":"YYYY-MM-DD","accion":"like|bookmark","url":"...","handle":"...","tema":"...","por_que":"inferencia corta","destino":"x-feed|idea Ixxx|draft|descartar"}
```

## KPIs (revisar en REVIEW semanal)
- **Cadencia:** posts publicados / 7. Meta ≥ 5/sem, ideal 7/7.
- **Alcance:** Δ impresiones_30d vs semana previa. Meta: no bajar; +10% sem si hay tracción.
- **Seguidores:** Δ absoluto/sem. Registrar, sin obsesión.
- **Engagement:** (likes+rt+replies+guardados)/impresiones por post. Comparar por pilar → doblar el pilar que rinde.
- **Dealflow (cualitativo):** replies/DMs de proyectos, devs, bounties. Anotar en briefing.

## Baseline
Primera corrida de `x-growth`: capturar la foto inicial en `x-metrics.jsonl` ANTES de publicar nada.
Sin baseline no hay "creció".
