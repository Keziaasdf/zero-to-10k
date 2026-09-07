---
name: daily-loop
description: Rutina diaria del challenge 0→10k (comando DAILY / CORRIDA). Leer estado, construir el incremento de la apuesta activa, dejar drafts, hunt de bounties abiertos, actualizar ledger y briefing, commit local. Invocar cuando el usuario escriba DAILY, CORRIDA, o pida "la corrida de hoy".
---

# daily-loop

Ciclo corto. Presupuesto: **~15–25 tool calls**, sin subagentes. Chrome solo si un dato lo exige.

## Pasos
1. **Leer** (rápido): `STATE.md`, `NEXT_ACTIONS.md`, `PIPELINE.md`, `BRIEFING/` del día anterior. No re-leer las otras carpetas salvo que NEXT_ACTIONS lo pida.
2. **X (opcional)**: solo si hay una pregunta concreta que responder. Si sí → skill `ingest-x` (máx 8–12 min, 40 posts). Si no aporta a la apuesta, saltar.
3. **BUILD**: un incremento real de la apuesta activa (código/archivo). Si la apuesta es I001, trabajar en `experiments/001-solana-safecheck/`.
4. **DRAFTS**: si hay algo que decir, actualizar `content/drafts/` + `content/queue.jsonl`. No publicar.
5. **HUNT**: skill `hunt` — refrescar `data/bounties.jsonl` con lo que sigue abierto y sus deadlines. Quitar lo vencido.
6. **LEDGER**: fila nueva en `LEDGER.md` con `tipo=time`, horas aprox, qué se hizo, experimento, resultado.
7. **BRIEFING**: crear/actualizar `BRIEFING/YYYY-MM-DD.md` con las 8 secciones (X, ideas, decisión, build, drafts, hunting, capital, hacer/no-hacer/métrica).
8. **STATE / PIPELINE / NEXT_ACTIONS**: reflejar cambios. Apuesta activa y kill date intactos salvo decisión del usuario.
9. **COMMIT local**. Push solo si el repo es público. Si pide credenciales → parar y dar el comando.

## Reglas
- Cero subagentes. Cero Chrome fuera del hilo padre.
- No re-hacer SETUP. No reescribir experiments enteros; solo el incremento.
- Cerrar con: VISTO / DECIDIDO / CONSTRUIDO / DRAFTS / HUNTING / NECESITO DE TI / MAÑANA.

## Si la cuota de tokens está baja
Prioridad: BUILD incremento → LEDGER → BRIEFING → commit. HUNT y drafts pueden esperar a mañana; dejar NEXT_ACTIONS preciso.
