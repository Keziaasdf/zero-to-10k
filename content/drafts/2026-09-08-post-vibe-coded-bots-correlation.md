# DRAFT — post/thread: "vibe-coded trading bots converge"
Estado: NO PUBLICAR. Publicar solo con "PUBLICA AHORA".
Pilar: P2 explicador (+ P1 tie-in a SafeCheck al cierre).
IDIOMA: inglés.
Tema / objetivo: el riesgo real de la ola de "vibe-code tu bot de trading" no es código malo, es CONVERGENCIA — miles de bots con lógica casi idéntica = una posición correlada gigante que sale por la misma puerta. Refuerza el worldview de SafeCheck sin repetir posts previos.

Datos (research 2026-09-08):
- Narrativa vibe-trading fuerte en 2026: describir estrategia en lenguaje natural → código ejecutable. Repo "Vibe-Trading" (HKUDS) ~22k–32k stars, 460+ alpha factors.
- Marzo 2026: 3 exchanges grandes lanzaron infra de AI agent trading en días (Binance Skills Hub, etc.).
- Riesgo citado por la prensa: alta densidad de templating → concentración de vulnerabilidades; millones de bots con lógica idéntica → comportamiento correlado a escala; retail sin el marco de compliance/riesgo que tiene un banco.
- Señal del día (bookmarks del usuario): tutorial "bot de trading con Claude Fable 5.1" (@MikuBTC), prompts de research "GPT-6 Astra" (@milesdeutscher).

---

## Single post

Everyone's vibe-coding a trading bot now — describe a strategy in plain English, ship it in an afternoon. The tooling is genuinely good.

The part nobody prices in: if thousands of people generate bots from the same prompts and the same open-source templates, they converge on the same logic. Same entries, same exits, same stops.

That's not a set of independent bots. It's one big correlated position, all trying to leave through the same door at once.

A green backtest doesn't tell you who else is running your exact strategy.

## Thread (4)

1/ Vibe-coding a trading bot is real now: plain-English strategy in, working code out, live in an afternoon. Not knocking the tooling — it works.

2/ The risk isn't "the AI writes bad code" (though it can). It's convergence. Thousands of people prompting similar ideas against the same few open-source templates end up with near-identical logic.

3/ Identical logic = correlated behavior. The same triggers fire for everyone at the same time. On the way in it looks like alpha. On the way out it's a crowd through one exit, and the slippage is real.

4/ Same reason I'm building SafeCheck around liquidity and contract permissions, not signals that look clever: a backtest doesn't show you how many people run your exact strategy, or whether there's a bid left when you all sell. https://keziaasdf.github.io/zero-to-10k/experiments/001-solana-safecheck/

## Short (reply/quote)

Vibe-coded trading bots converge: same prompts + same templates = same logic = one correlated position trying to exit through one door. A green backtest doesn't show you who else is running it.
