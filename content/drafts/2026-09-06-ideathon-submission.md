# DRAFT — Submission: Superteam Ukraine IDEATHON
Estado: NO ENVIAR. Listo para copiar-pegar al formulario de Superteam Earn.
Premio: 1000 USDG · Deadline: 2026-09-15 · NO es un post de X.

═══════════ COPIAR DESDE ACÁ ═══════════

**Título:** Solana SafeCheck — chequeo de riesgo de un token, en español

**Qué es.** Una página estática que, dado el contract address de un token de Solana, devuelve 5 señales de riesgo y un veredicto de una frase —PASS / CAUTION / KILL— en español. Pensada para traders nuevos y comunidades hispanohablantes que hoy no usan los checkers en inglés (RugCheck, GMGN) porque están cargados de ruido o detrás de un login. Cada resultado tiene un link compartible (`?ca=...`): quien lo abre ve el análisis al instante.

**Demo:** https://keziaasdf.github.io/zero-to-10k/experiments/001-solana-safecheck/
**Repo (open source desde el commit 1):** https://github.com/Keziaasdf/zero-to-10k — carpeta `experiments/001-solana-safecheck`

**Read-only, sin riesgo para el usuario.** No conecta wallet, no pide firmar transacciones, no ejecuta trades, no dice "comprá", no tiene login. Solo lee datos públicos. Lo que no se puede obtener de una fuente pública gratuita se muestra como `n/d` — nunca se inventa.

**Stack.** HTML/JS estático, sin backend, sin build step. Mint y freeze authority vía RPC público de Solana (`solana-rpc.publicnode.com`); liquidez y edad del par vía la API pública de DexScreener. Hosteado gratis en GitHub Pages. Costo de operación: 0.

**Impacto:**
- Baja la barrera de la seguridad on-chain al español, un idioma que casi ningún checker cubre.
- Embebible con una sola URL y compartible en un grupo con `?ca=` — se distribuye solo.
- Open source y sin dependencias de pago: cualquier proyecto que lance en Solana lo puede forkear o extender.

═══════════ HASTA ACÁ ═══════════

**REVISAR SI ES GLOBAL O UKRAINE-ONLY antes de enviar.** Si el bounty está restringido al chapter de Ucrania, no aplica — buscar el equivalente global en Superteam Earn.
