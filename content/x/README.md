# content/x/ — motor de contenido de X (@KeziaQl1)

Todo el sistema para postear a diario y subir alcance. Respaldo en GitHub (repo público).
Nada se publica sin que el usuario escriba exactamente `PUBLICA AHORA` + el slug.

## Archivos
| Archivo | Qué es |
|---|---|
| `INTERESES.md` | Temas sí / temas no. Holdings ($NPC, $CAKE, $SPARK). Idioma: **inglés**. Exclusión dura: política / Chile. |
| `pilares.md` | 4 pilares (P1 build-in-public · P2 explicador/anti-scam · P3 señal de ecosistema · P4 curación) → objetivo. Reglas de voz. |
| `metricas.md` | Cómo se mide el alcance. Esquema de `data/x-metrics.jsonl`, `data/x-posts.jsonl`, `data/x-engage.jsonl`. KPIs. |
| `imagenes.md` | Workflow de memes/imágenes: brief + prompt para Grok. Banco de memes vibe/vibe. |
| `../drafts/*.md` | Un draft por post/hilo. Formato en `.claude/skills/publish/SKILL.md`. Texto publicable en inglés. |

## Datos (en `data/`)
- `x-feed.jsonl` — señales de mercado/narrativa vistas en X.
- `x-engage.jsonl` — likes/bookmarks del usuario → tema/idea.
- `x-metrics.jsonl` — foto del perfil (~1/semana).
- `x-posts.jsonl` — posts propios publicados + snapshots de métricas a 48h/7d.
- `ideas.jsonl` — ideas de contenido con id `I0xx`.

## Flujo diario (skill `x-growth`, comando `X GROWTH`)
1. **Revisar lo subido hoy** — posts propios publicados (perfil + analytics) y su alcance.
2. **Revisar lo que sigue el usuario** — Following + likes/bookmarks nuevos → `x-engage.jsonl`.
3. **Research** — 2–4 temas de `INTERESES.md` con movimiento (WebSearch/WebFetch; números en DexScreener).
4. **Sugerir posts** — 1–3 drafts nuevos/refrescados por pilar, en inglés, en `../drafts/`.
5. **Sugerir imágenes** — para los drafts que lo pidan (sobre todo memes vibe/vibe): brief + prompt de Grok en el propio draft (`## Image brief (Grok)`) y/o en `imagenes.md`.
6. **Registrar** — `queue.jsonl`, `calendar.md`, `ideas.jsonl`, fila en `LEDGER.md`, commit + push.

Lane LOCAL (con Chrome, hilo padre) hace pasos 1–2. Lane RESEARCH (sin Chrome) hace 3–6.
Límites de navegación: 8–12 min, 40 posts, 8 perfiles, 3 búsquedas. Captcha/rate limit → parar.

## Publicar
`PUBLICA AHORA <slug>` → skill `publish` §"Al publicar". Cashtag `$SPARK`: seleccionar del dropdown (1ª opción, contract `…8248`).

## Estado
- Publicados 2026-09-08: spark-vibe-season0 (P3), cake-bstocks (P3).
- Loop `x-growth` cada 4h (job de sesión `cbd21e5e`).
