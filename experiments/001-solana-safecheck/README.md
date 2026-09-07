# 001 — Solana SafeCheck

Página estática que, dado un contract address (CA) de un token SPL de Solana,
devuelve 5 señales de riesgo y un veredicto **PASS / CAUTION / KILL** con una
frase en español y un resultado copiable / link compartible.

## Hipótesis
La gente entra a launches de Solana sin revisar lo básico. Los checkers que existen
(RugCheck, GMGN) están en inglés, cargados de ruido y a veces detrás de login.
Un chequeo de 5 señales, en español, con link compartible y hecho en público,
puede ganar atención → dealflow (bounties, gigs, followers que convierten).

Esto NO compite en features con RugCheck/GMGN. Diferencial:
1. Copy en español, veredicto de una frase.
2. Link compartible (`?ca=...`) para pegar en un grupo.
3. Build-in-public: repo abierto desde el commit 1.

## Alcance del entregable 7d (kill 2026-09-13)
- 1 archivo `index.html`, estático, sin backend, sin build step.
- UX: input CA → botón Analizar → 5 filas + veredicto PASS/CAUTION/KILL + frase ES + botón "Copiar resultado".
- `?ca=<address>` en la URL autoejecuta el análisis (link compartible).
- Sin wallet, sin firmar, sin login, sin backend de pago.
- APIs/RPC públicos sin API key. Si un dato no sale → se muestra `n/d`, no se inventa.

## Señales
| # | Señal | Fuente | Regla |
|---|---|---|---|
| 1 | Mint authority | Solana RPC `getAccountInfo` (jsonParsed) sobre el mint | activa = KILL (pueden imprimir supply) |
| 2 | Freeze authority | mismo `getAccountInfo` | activa = KILL (pueden congelar tu balance) |
| 3 | Liquidez | DexScreener `GET /latest/dex/tokens/{ca}` | sin par o `< $1k` = KILL; `$1k–$10k` = CAUTION; par `< 24h` = CAUTION |
| 4 | Concentración top holders | Solana RPC `getTokenLargestAccounts` vs `supply` | top-10 (excl. pools conocidos si se puede) `> 25%` = CAUTION |
| 5 | Bundle / snipers | — | **omitida**: sin fuente pública gratuita fiable → fila fija `n/d`, no puntúa |

## Veredicto
- **KILL**: cualquier regla KILL se cumple (mint/freeze authority activa, sin par, liquidez < $1k).
- **CAUTION**: ninguna KILL, pero ≥1 regla CAUTION, o falta un **dato clave = señales 1–3** (`n/d` en mint, freeze o liquidez).
- **PASS**: señales 1–3 con dato y ninguna regla KILL/CAUTION.
- Señales 4 (holders) y 5 (bundle) son *best-effort*: si están en `n/d` NO fuerzan CAUTION, solo se muestran.

## APIs concretas (keyless, CORS abierto para browser) — verificadas 2026-09-06
- **`api.mainnet-beta.solana.com` NO sirve**: devuelve `403 Access forbidden` a requests con origin de browser.
- Señales 1–2 (mint/freeze authority): `https://solana-rpc.publicnode.com` (POST `getAccountInfo` jsonParsed). Responde 200, keyless. Bloquea `getTokenLargestAccounts`.
- Señal 4 (holders): `https://solana.api.onfinality.io/public` (POST `getTokenLargestAccounts`). Permite el método pero con rate-limit duro → **en la práctica casi siempre `n/d`**. No hay endpoint gratuito browser-CORS fiable para holders; se documenta la limitación en vez de fingir el dato.
- Señal 3 (liquidez): `https://api.dexscreener.com/latest/dex/tokens/{ca}` (GET). Campos: `pairs[].liquidity.usd`, `pairs[].pairCreatedAt`, `pairs[].dexId`. Funciona bien.
- Señal 5 (bundle/snipers): sin fuente → fila fija `n/d`.

## No hace
- No ejecuta ni sugiere trades ("comprá/vendé").
- No conecta ni lee wallets del usuario.
- No pide firmar transacciones.
- No guarda datos; todo corre en el browser.

## Kill / pivote
Al 2026-09-13, si NO hay (a) `index.html` funcional con ≥1 llamada real resolviendo,
o (b) ≥1 bounty abierto concreto donde este entregable encaje → se mata I001 y se re-elige apuesta.

## Deploy (GitHub Pages)
- URL prevista: **https://keziaasdf.github.io/zero-to-10k/experiments/001-solana-safecheck/**
- También `https://keziaasdf.github.io/zero-to-10k/` → el `index.html` de la raíz del repo redirige acá.
- Requiere: repo **público** + Pages activado (Settings → Pages → Source: Deploy from a branch → Branch: `main` → `/ (root)` → Save). GitHub Pages solo sirve desde `/root` o `/docs`; por eso el redirect en la raíz en vez de mover el site.

## Estado
- 2026-09-06: README + `index.html` funcional. Señales 1-2 (mint/freeze authority) vía `solana-rpc.publicnode.com` + señal 3 (liquidez/edad par) vía DexScreener resuelven con datos reales. Señales 4-5 → `n/d` honesto. Probado en Chrome: BONK → PASS, USDC → KILL.
- 2026-09-06 (infra blitz): og:tags + `<meta description>` + canonical + favicon; copy ES pulida (leyenda PASS/CAUTION/KILL, frases de veredicto en lenguaje llano); `index.html` redirect en la raíz del repo para Pages.
