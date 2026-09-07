# DRAFT — Submission: Superteam Ukraine IDEATHON
Estado: NO ENVIAR todavía. Revisar elegibilidad (¿es global o chapter-only?) y deadline (2026-09-15) antes.
Destino: formulario de Superteam Earn (NO es un post de X).
Premio: 1000 USDG. Bounty id: 9ceadd2f-style (ver data/bounties.jsonl).

---

## Idea: Solana SafeCheck

**One-liner.** Una página estática que, dado un contract address, devuelve 5 señales de riesgo y un veredicto PASS / CAUTION / KILL en español, con un link compartible — sin conectar wallet, sin firmar nada, open source.

**Problema.** Cada launch nuevo en Solana es un campo minado: mint authority viva, freeze authority viva, liquidez de humo, holders concentrados. Los checkers que existen (RugCheck, GMGN) están en inglés, cargados de ruido, y a veces detrás de login. La gente que más los necesita —traders nuevos, comunidades en español— no los usa.

**Qué hace SafeCheck.**
- Pegás el CA → 5 filas + un veredicto de una frase.
- Señales: mint authority, freeze authority, liquidez y edad del par, concentración top-10 holders, bundle/snipers.
- Lo que no se puede sacar de una fuente pública gratuita se muestra como `n/d` — no se inventa.
- Link `?ca=...` para pegar en un grupo: el que lo abre ve el análisis al instante.

**Qué NO hace.** No ejecuta trades. No dice "comprá". No toca tu wallet. No pide firmar transacciones.

**Estado (al momento de enviar).** v0 funcional: mint/freeze authority vía RPC público + liquidez vía DexScreener resuelven con datos reales. Probado con BONK (PASS) y USDC (KILL). Repo abierto desde el primer commit. Demo: <URL de GitHub Pages>.

**Por qué encaja en el hackathon.** Es infra de seguridad de bajo nivel, útil para cualquier proyecto que lance en Solana, en un idioma que casi nadie cubre. Fácil de embeber (una URL) y de extender (open source).

**Roadmap corto.** Deploy público → pulir copy → embeddable widget → si aparece una fuente de holders, activar esa señal.

**Autor.** @KeziaQl1 · repo: github.com/Keziaasdf/zero-to-10k (carpeta `experiments/001-solana-safecheck`).
