# MAP — proyectos locales bajo `Emprendimiento/`

`zero-to-10k/` es la carpeta MAIN (centro de mando del challenge 0→10k).
Las demás son **solo lectura** desde acá: se referencian, no se editan ni se copian.

| Carpeta | Qué es | Chain | Rol respecto a 0→10k | Se itera aquí? |
|---|---|---|---|---|
| **zero-to-10k/** | Centro de mando del challenge. Apuesta activa, spikes, pipeline, ledger, briefings, experiments propios (SafeCheck). | Solana (I001) + agnóstico | — | **SÍ** — todo el trabajo nuevo |
| **spark-testnet/** | Playbook personal de la Season 0 de `vibe/vibe` (launchpad Seedify sobre RHC testnet) + drafts build-in-public. Wallet `0xE427…F9Ae`. Tool de tracking en repo aparte `vibe-season-kit` (público). | Robinhood Chain **testnet (46630)** | Insumo del frente **Spark/RHC**. Único farming "gratis" confirmado (5% nuevo $SFUND a testnet users, ETA sept). | NO — se lee. Ficha: `ecosystem/spark-rhc.md` |
| **robinhood-chain/** | Repo de research + farming-ops del ecosistema RHC/Seedify/Spark. `RESEARCH.md` (doc vivo), `FARMING-TRACKER.md`, `content-ops/` (SOP de contenido X), copias de subagents. | Robinhood Chain **mainnet (4663)**, gas ETH | Insumo del frente **RHC**. Contexto de ecosistema + voz de contenido. Decisión 2026-08-30: solo camino gratis, sin capital de riesgo. | NO — se lee. Ficha: `ecosystem/robinhood-chain.md` |
| **venture-lab/** | Loop de ideación de producto para RHC (backlog rankeado por factibilidad solo-founder). **Loop PAUSADO** desde 2026-09-03 (cron eliminado). Produjo 1 idea en construcción: `float-squeeze-radar`. | Robinhood Chain | Insumo de **ideas de producto**. Fuente de la metodología de scoring. | NO — se lee. Ficha: `ecosystem/venture-lab.md` |
| **vibe-season-kit/** (repo, no carpeta hermana aquí) | Tool pública de tracking checklist / PNL / bonding curve para la Season 0. | RHC testnet | Referencia. No se toca. | NO |
| **float-squeeze-radar/** (aún no creada) | Idea graduada de venture-lab: scanner de squeezes de float sobre stock-tokens de RHC. Gate técnico 2026-09-08 / abort 2026-09-14. | RHC mainnet | **Fuera de 0→10k** salvo que el usuario lo meta como apuesta/spike. | NO |

## Relaciones
- `spark-testnet/` y `robinhood-chain/` son el **mismo frente** (Seedify/Spark/RHC) visto desde dos ángulos: testnet-farming vs research+contenido. El README de `robinhood-chain/` dice que eventualmente se fusionan; **desde 0→10k no lo hacemos**, solo consolidamos la lectura en `ecosystem/spark-rhc.md` + `ecosystem/robinhood-chain.md`.
- `venture-lab/` lee `../robinhood-chain/` como contexto. Nosotros leemos las tres.
- Los subagents (`../.claude/agents/*.md`: scout-proyectos-rh, explorador-airdrops-rh, pulso-x-grok, radar-contenido-x, etc.) pertenecen a esos loops. **En 0→10k no se usan** (regla: cero subagentes para X).

## Qué itera esta carpeta vs qué solo referencia
- **Itera:** I001 SafeCheck (`experiments/001-…`), `experiments/002-spark-rhc-watch/`, `content/`, pipeline/ledger/briefings, HUNT de bounties abiertos.
- **Solo referencia (lectura):** todo lo que hay en `../spark-testnet`, `../robinhood-chain`, `../venture-lab`. Si algo de ahí necesita acción, se resume en la ficha `ecosystem/` correspondiente y se decide acá.
