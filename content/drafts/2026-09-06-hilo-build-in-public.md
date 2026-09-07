# DRAFT — hilo build-in-public (arranque)
Estado: NO PUBLICAR. Solo se publica si el usuario escribe exactamente "PUBLICA AHORA".
Formato: X thread. Tono directo, sin hype, sin promesas de retorno.

---

## Versión hilo (6 posts)

1/
Voy a construir en público una herramienta para traders de Solana.
Regla: read-only. Nunca conecta wallet, nunca firma nada.
Objetivo personal: 0 → 10k en 90 días, solo build + contenido. Día 1.

2/
El problema: cada launch nuevo es un campo minado. Mint authority viva, LP sin quemar, holders concentrados, bundles.
Ya hay checkers, pero o son pesados o esconden lo que importa detrás de un login.

3/
Lo que voy a shippear esta semana:
- página estática, sin backend propio
- pegás un contract address
- te devuelve las 5 señales de riesgo que de verdad importan, sin ruido
- open source desde el commit 1

4/
Lo que NO va a hacer:
- no ejecuta trades
- no te dice "comprá"
- no toca tu wallet
Si algo te pide firmar una tx para "revisar" un token, cerrá la pestaña.

5/
Stack: APIs y RPC públicos, hosting gratis. Costo del proyecto: 0.
Todo el trabajo y las decisiones quedan en un repo público. Los errores también.

6/
Si armás bots o tools sobre Solana y querés que revise algo, respondé acá.
Update con el primer release en unos días.

---

## Versión post único

Construyo en público: tool read-only para chequear el riesgo de un launch en Solana antes de tocarlo.
Sin conectar wallet, sin firmar nada, open source, costo 0.
Primer release esta semana. 0→10k, día 1.

---

## Versión corta (para reply/quote)

Read-only safety-check para launches de Solana. Pegás el CA, ves las 5 señales que importan. Sin wallet, sin txs, open source. Shippeo esta semana.
