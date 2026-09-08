---
name: x-growth
description: Motor de crecimiento de X (@KeziaQl1). Comando X GROWTH / X LOOP / CRECER X. Un ciclo = research de temas de interés (solo crypto) -> capturar alcance de posts propios -> harvest de likes/bookmarks del usuario como señal -> generar/refrescar drafts por pilar -> actualizar cola y métricas. NUNCA publica (solo con "PUBLICA AHORA"). NUNCA automatiza follows/likes. Cero subagentes. Chrome solo en el hilo padre.
---

# x-growth

Ciclo corto y loopeable. Presupuesto: **~15–25 tool calls**, sin subagentes.
Nada se publica sin que el usuario escriba exactamente `PUBLICA AHORA`.

## Insumos (leer primero, rápido)
- `content/x/INTERESES.md` — temas sí / temas no (política y Chile = fuera).
- `content/x/pilares.md` — P1 build / P2 explicador / P3 ecosistema / P4 curación.
- `content/x/metricas.md` — esquema de los 3 archivos de datos y KPIs.
- `ecosystem/x-account.md` — voz y reglas. `data/x-feed.jsonl` — señales previas.

## Cadencia (loop varias veces al día)
Cada corrida decide su modo por el último timestamp de `data/x-metrics.jsonl` / `data/x-engage.jsonl`:
- **Modo LOCAL completo (con Chrome):** solo si la última pasada de Chrome fue hace **> 5 h** y estás en sesión interactiva. Máx **2 pasadas de Chrome al día** (X se navega a ritmo humano — nunca automatizar).
- **Modo RESEARCH (sin Chrome):** todas las demás corridas. Research + refrescar/añadir drafts. Barato y seguro, se puede repetir cada 3–4 h.
- Si en 24 h no hubo ninguna pasada de Chrome → la próxima corrida interactiva fuerza modo LOCAL para no perder el baseline/métricas.
- Rate limit / captcha en X → cerrar tab, marcar en la salida, seguir en modo RESEARCH el resto del día.

## Dos lanes

### Lane LOCAL (sesión interactiva, Chrome en hilo padre) — corrida completa
1. **Baseline / métricas.** `tabs_context_mcp {createIfEmpty:true}` → 1 tab.
   - `x.com/KeziaQl1` → screenshot → anotar seguidores/siguiendo/posts en `data/x-metrics.jsonl`.
   - Si carga: `x.com/i/account_analytics` → impresiones_30d, engagement.
   - Últimos posts propios publicados (los que estén en `data/x-posts.jsonl` sin snapshot de 48h/7d): abrir, leer contadores, **nueva línea** en `data/x-posts.jsonl`.
2. **Harvest de señal del usuario.** Following → bookmarks (`x.com/i/bookmarks`). Por cada like/bookmark relevante y nuevo: 1 línea en `data/x-engage.jsonl`. Ignorar todo lo que sea política/Chile. Límites: 40 posts, 8 perfiles, 3 búsquedas, 8–12 min. Captcha/rate limit → parar y avisar.
3. **Cerrar la tab.**
4. Seguir con los pasos de research + generación (abajo).

### Lane RESEARCH (sirve sola, sin Chrome — también apta para cloud)
5. **Research.** Para 2–4 temas de `INTERESES.md` con movimiento (o pedidos por el usuario): `WebSearch` / `WebFetch`. Buscar catalizador concreto, no vibes. Números de mercado → verificar en DexScreener antes de usarlos; si no se puede, `n/d`.
6. **Generar / refrescar drafts.** 1–3 drafts, cada uno en 1 pilar, formato de `skill:publish`:
   `content/drafts/YYYY-MM-DD-<slug>.md` con Estado `NO PUBLICAR`, versión hilo + post único + corta.
   **Texto publicable SIEMPRE en inglés** (headers/notas internas pueden ser español).
   Reutilizar ideas de `data/ideas.jsonl` (cat `content`) antes de inventar.
   Al mencionar SPARK: contract `0x0FB07c88Bc6d195c196279523957C004eb868248` (Base), no el cashtag.
7. **Registrar.** Cada draft → línea en `content/queue.jsonl` (`estado:"borrador"` o `"listo"`), fila en `content/calendar.md`. Ideas nuevas → `data/ideas.jsonl` (`I0xx`, score rúbrica CLAUDE.md).
8. **Ledger.** Fila en `LEDGER.md` `tipo=time` con lo hecho.
9. **Commit local.** Push solo si no pide credenciales.

## Salida (cerrar la corrida)
`VISTO / DECIDIDO / CONSTRUIDO / DRAFTS / HUNTING / NECESITO DE TI / MAÑANA`
+ 1 línea de métricas: cadencia semana en curso (posts/7) y Δ alcance si hubo captura.

## Prohibido
- Publicar, responder, dar like, seguir, guardar — cualquier acción de escritura en X.
- Drafts publicables en español (van en inglés).
- Subagentes para Chrome/X. Chrome fuera del hilo padre. API de X. Scraping masivo.
- Tocar temas de política o de Chile.
- Citar números de mercado sin fuente viva.
- Shill de $NPC / $CAKE / $SPARK o de token propio. "Consejo de inversión".
- Meter programas/airdrops cerrados como premio vivo (SPK claim está cerrado).

## Loop
- **Varias veces al día:** `/loop 4h x-growth` en una sesión local con Chrome logueado.
  La primera corrida hace el baseline (modo LOCAL); las siguientes alternan según la cadencia de arriba
  (Chrome máx 2×/día, research el resto).
- Alternativa: sumar `x-growth` como paso 4.5 de `daily-loop`.
- Cloud: descartado — la routine cloud está desactivada y el entorno no tiene Chrome logueado.
