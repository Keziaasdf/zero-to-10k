---
name: publish
description: Redactar y organizar contenido para X (@KeziaQl1) en content/ y content/drafts/. Comando CONTENT. Produce drafts (hilo, post único, versión corta), actualiza content/queue.jsonl y content/calendar.md. NO publica en X salvo que el usuario escriba exactamente "PUBLICA AHORA".
---

# publish

## Regla #1
**Nunca se publica en X** salvo que el mensaje del usuario contenga exactamente `PUBLICA AHORA`.
Sin esa frase: todo queda en `content/drafts/`. Aun con la frase, se publica **solo lo que el usuario señale**, y Chrome solo en el hilo padre.

## Formato de un draft (`content/drafts/YYYY-MM-DD-<slug>.md`)
```
# DRAFT — <título>
Estado: NO PUBLICAR (o: LISTO, espera PUBLICA AHORA)
Tema / objetivo:

## Versión hilo (N posts)
1/ ...
## Versión post único
## Versión corta
```

## Pasos
1. Leer `ecosystem/x-account.md` (voz, reglas) y `../robinhood-chain/content-ops/VOICE-GUIDE.md` (solo lectura).
2. Escribir/editar el draft. **Texto publicable en INGLÉS** (decisión 2026-09-08; headers/notas internas pueden ir en español). Directo, sin hype, sin "consejo de inversión", sin shill de token propio. Al mencionar SPARK usar el contract `0x0FB07c88Bc6d195c196279523957C004eb868248` (Base), no el cashtag (enruta mal en X).
3. Verificar cualquier número de mercado en DexScreener (fuente viva) antes de dejarlo en el draft.
4. Registrar en `content/queue.jsonl`:
   `{"ts":"YYYY-MM-DD","slug":"...","tipo":"hilo|post|reply","tema":"...","estado":"borrador|listo|publicado","archivo":"content/drafts/..."}`
5. Actualizar `content/calendar.md` (qué va cuándo, en orden, sin fechas rígidas).
6. Commit local.

## Al publicar (solo con PUBLICA AHORA)
- Abrir `x.com/compose/post` en el hilo padre. Pegar. **Mostrar screenshot al usuario antes del click final.**
- Tras publicar: marcar `estado:"publicado"` + URL en `queue.jsonl`, fila en `LEDGER.md`.
