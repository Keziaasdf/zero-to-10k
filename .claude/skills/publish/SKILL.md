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
2. Escribir/editar el draft. **Texto publicable en INGLÉS** (decisión 2026-09-08; headers/notas internas pueden ir en español). Directo, sin hype, sin "consejo de inversión", sin shill de token propio. Incluir el contract de SPARK `0x0FB07c88Bc6d195c196279523957C004eb868248` (Base) en el texto.
3. Verificar cualquier número de mercado en DexScreener (fuente viva) antes de dejarlo en el draft.
4. Registrar en `content/queue.jsonl`:
   `{"ts":"YYYY-MM-DD","slug":"...","tipo":"hilo|post|reply","tema":"...","estado":"borrador|listo|publicado","archivo":"content/drafts/..."}`
5. Actualizar `content/calendar.md` (qué va cuándo, en orden, sin fechas rígidas).
6. Commit local.

## Al publicar (solo con PUBLICA AHORA)
- Abrir `x.com/compose/post` en el hilo padre. Pegar. **Mostrar screenshot al usuario antes del click final.**
- **CASHTAGS — seleccionar el token del dropdown (obligatorio para `$SPARK`).**
  X enruta `$SPARK` por defecto al token equivocado (Spark Protocol). Procedimiento:
  1. Escribir el texto sólo hasta `$SPARK` (ej: `type "The $SPARK"`).
  2. Esperar 2s → aparece el dropdown de autocomplete de cashtag.
  3. Screenshot. **Click en la PRIMERA opción** — es `SPARK · SPARK · Crypto · ~1.5M · 0x0fb0…8248` (~$0.00157). Verificar que el contract del item termina en `…8248` (Base).
  4. Recién ahí escribir el resto del post. Usar `SFUND`/`SPARK` sin `$` en el cuerpo para no re-disparar el dropdown.
  5. Confirmar que la card de preview muestra el token correcto (chart verde, `$0.00157`, MCAP ~$1.5M) antes de publicar.
- Si aparece una card de auto-embed que no corresponde → quitarla con la X de la card.
- Tras publicar: marcar `estado:"publicado"` + URL en `queue.jsonl`, fila en `LEDGER.md`.
