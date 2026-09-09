# ecosystem/x-account.md — cuenta X `@KeziaQl1`

**Estado:** ACTIVA para lectura + motor de crecimiento montado. Publicación BLOQUEADA salvo `PUBLICA AHORA`.
**Última actualización:** 2026-09-08

## Datos
- Handle: **@KeziaQl1** (display: `keziacl.eth`). Logueada en el Chrome de esta máquina.
- Suscripción X: mínima (Premium básico).
- Lista pinneada vista: "Vibe Coding Meta".
- Feed Following: mezcla cripto (Solana memecoins, RHC, zcash, BTC) + noticias Chile + política.
- Bookmarks (tema dominante): AI trading agents, "repos que imprimen dinero", tracking de wallets memecoin, cómo conseguir web3 jobs.

## Rol en 0→10k
- **Canal de dealflow y audiencia**, no de ingreso directo.
- Build-in-public del challenge y de I001 SafeCheck.
- Explicadores de ecosistema (Spark/RHC, "qué es scam") = contenido con demanda y defensivo.
- Meta operativa: **1 post/día**, alcance creciente → posición para airdrops / WL (vibe/vibe $SPARK y otros) / dealflow.

## Motor de crecimiento (montado 2026-09-08)
- Skill **`x-growth`** (comando `X GROWTH` / `X LOOP`): research de interés → captura de alcance → harvest de likes/bookmarks → drafts por pilar → cola + métricas. No publica.
- **`content/x/INTERESES.md`** — temas sí/no. Holdings del usuario: **$NPC, $CAKE, $SPARK** (seguir de cerca, jamás shill). Exclusión dura: política y Chile.
- **`content/x/pilares.md`** — P1 build-in-public · P2 explicador/anti-scam · P3 señal de ecosistema · P4 curación.
- **`content/x/metricas.md`** + `data/x-metrics.jsonl` (foto perfil) · `data/x-posts.jsonl` (posts propios) · `data/x-engage.jsonl` (likes/bookmarks → señal).

## Reglas
- **Cero automatización.** No follows, no likes masivos, no API, no scraping.
- **Cero subagentes** para leer X. Chrome solo en hilo padre.
- Límites por sesión: 8–12 min, 40 posts, 8 perfiles, 3 búsquedas.
- Verificar números de mercado en fuente viva (DexScreener) antes de escribir un draft que los use.
- Todo texto va a `content/drafts/`. Se publica **solo** cuando el usuario escribe exactamente `PUBLICA AHORA`, y solo lo que él señale.

## Voz
- Referencia: `../robinhood-chain/content-ops/VOICE-GUIDE.md`.
- **Posts en INGLÉS siempre** (decisión del usuario 2026-09-08). Notas internas en español.
- Directo, sin hype, sin promesas de retorno. Listas > párrafos.
- Nunca "consejo de inversión". Nunca shill de token propio.
- $SPARK (holding) = contract `0x0FB07c88Bc6d195c196279523957C004eb868248` en Base (~$0.00157, MCAP ~$1.5M).
  - **Al escribir `$SPARK` en el composer: esperar el dropdown y hacer click en la PRIMERA opción** (SPARK, contract `…8248`). Eso liga el cashtag al token correcto y la card de preview sale bien (chart verde, $0.00157). Verificado 2026-09-08 (post `2097486155897827347`).
  - Sin seleccionar, `$SPARK` enruta a Spark Protocol ($SPK), token distinto.
  - Igual incluir el contract en el texto como respaldo.

## Próxima acción
- Cola de contenido en `content/queue.jsonl`, calendario en `content/calendar.md`.
- Correr `x-growth` en sesión local para capturar **baseline de métricas** (seguidores / impresiones_30d) antes de publicar nada.
- Confirmar con el usuario a qué token exacto se refiere con **$SPARK** (no es `$SPK` de Spark Protocol, cuyo airdrop está cerrado).

## No hacer
- No publicar sin la frase exacta.
- No responder DMs ajenos ni citar contenido privado.
- No pelear en replies de política/noticias con la cuenta.
