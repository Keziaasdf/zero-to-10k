---
name: ingest-x
description: Pasada corta de X (como el usuario, Chrome logueado en el hilo padre) para extraer señales al archivo data/x-feed.jsonl. Invocar con INGEST X, o cuando la corrida diaria necesite contexto de mercado/narrativa. NUNCA publica, NUNCA automatiza follows/likes, NUNCA usa subagentes.
---

# ingest-x

## Límites duros (por sesión)
- 8–12 min de navegación continua. 40 posts máx. 8 perfiles máx. 3 búsquedas máx.
- **Chrome solo en el hilo padre.** Cero subagentes. 1 tab, se cierra al terminar.
- Captcha / rate limit → parar y avisar. No reintentar 3 veces.

## Pasos
1. `tabs_context_mcp {createIfEmpty:true}` → `navigate x.com/home`.
2. Following primero (si existe la pestaña). Luego bookmarks (`x.com/i/bookmarks`, puede redirigir a `x.com/i/history`). Máx 1–3 búsquedas dirigidas a una pregunta concreta.
3. Screenshot + scroll. No abrir hilos largos salvo que la señal lo valga.
4. Escribir cada señal como una línea JSON en `data/x-feed.jsonl`:
   `{"ts":"YYYY-MM-DD","fuente":"following|bookmarks|search:<q>","handle":"...","tema":"...","nota":"...","senal":"alta|media|baja|contexto"}`
5. Ideas nuevas → `data/ideas.jsonl` con id `I0xx`, score tentativo (rúbrica de CLAUDE.md), estado.
6. Cerrar la tab.

## Prohibido
- Publicar, responder, dar like, seguir.
- Abrir DMs, extraer datos privados.
- Verificar números de mercado sin fuente viva (DexScreener) antes de usarlos en un draft.
- Meter hackathons/programas ya cerrados al PIPELINE como premio vivo.
