---
name: hunt
description: Research de bounties / airdrops / whitelists ABIERTOS con fecha de corte real, para el challenge 0→10k. Comando HUNT. Cero transacciones, cero conexión de wallet, cero firmas. Escribe data/bounties.jsonl. No mete programas cerrados como premio vivo.
---

# hunt

## Objetivo
Mantener `data/bounties.jsonl` con oportunidades **abiertas** donde encaje la apuesta activa
(hoy: I001 SafeCheck — dev tool read-only de Solana + contenido build-in-public).

## Fuentes (sin login, sin API key)
- Superteam Earn (JSON público): `https://superteam.fun/api/listings?type=bounty&take=40` (sigue el redirect 308 desde `earn.superteam.fun`). Campos: `title`, `sponsor.name`, `rewardAmount`, `token`, `deadline`, `status`.
- Colosseum: `blog.colosseum.com` — watch de anuncios de próximo hackathon (el Frontier corrió abr–may 2026).
- Búsqueda web para hackathons Solana/Base con registro abierto.
- X solo si hace falta confirmar una fecha (skill `ingest-x`, límites duros).

## Formato (`data/bounties.jsonl`)
`{"ts":"YYYY-MM-DD","fuente":"...","titulo":"...","sponsor":"...","premio":"N TOKEN","deadline":"YYYY-MM-DD","encaje_I001":"alto|medio|bajo","estado":"abierto|cerrado","nota":"..."}`

## Reglas
- **Nunca** conectar wallet, firmar, depositar, ni "hacer una tx para calificar".
- Programa **cerrado o vencido** → `estado:"cerrado"`, NO va al PIPELINE como premio vivo. Ejemplo: TxODDS x Solana $50k (cerró jul 2026).
- Verificar elegibilidad por chapter/país antes de recomendar aplicar (muchos Superteam son globales, otros no).
- Cada corrida: quitar/relegar lo vencido, marcar los que vencen en <72h.
- Cerrar con una lista corta: top 3 por encaje + deadline.
