# DRAFT — post: SafeCheck v0
Estado: NO PUBLICAR. Publicar solo con "PUBLICA AHORA". Requiere URL de Pages viva + verificar que BONK/USDC sigan dando PASS/KILL.
Tema: ship del primer artefacto de I001.

---

## Versión post único

Ya funciona la v0 de la tool que estoy construyendo en público:

pegás el contract address de un token de Solana → te devuelve 5 señales de riesgo y un veredicto PASS / CAUTION / KILL, en español.

- no conecta wallet
- no firma nada
- no te dice "comprá"
- open source

Link abajo. Pegale un CA y probá.

## Versión corta (reply/quote)

v0 lista: CA → 5 señales → PASS/CAUTION/KILL, en español, sin wallet, open source. <URL>

## Versión hilo (4)

1/ Hace unos días dije que iba a construir en público una tool para traders de Solana. v0 ya funciona.

2/ Qué hace: pegás un contract address y te devuelve 5 señales —mint authority, freeze authority, liquidez, concentración de holders, bundles— con un veredicto de una frase: PASS, CAUTION o KILL.

3/ Qué NO hace: no conecta tu wallet, no firma nada, no ejecuta trades, no te dice qué comprar. Si un dato no sale de una fuente pública, dice "n/d" — no lo inventa.

4/ Es estático y open source. Link con `?ca=` para pegar en un grupo: el que lo abre ve el análisis solo. Probala y decime qué le falta. <URL>
