# content/x/imagenes.md — memes e imágenes para X

El usuario genera las imágenes con **Grok** en otra sesión. Acá se dejan: (1) el **brief** (qué mostrar)
y (2) un **prompt listo para pegar en Grok**. No se generan imágenes desde este repo.

## Cuándo una imagen ayuda
- Meme vibe/vibe (P3) — la comunidad postea memes; entrar en el formato = alcance + relevancia para WL.
- Explicador visual (P2) — un diagrama simple pega más que 4 líneas de texto.
- Ship shots (P1) — screenshot real de SafeCheck, no ilustración.
- NO forzar imagen en posts de dato puro/anti-scam serio.

## Formato del brief (va en el draft, sección `## Image brief (Grok)`)
```
Concepto: <la idea en 1 frase>
Formato: meme | diagrama | ilustración | screenshot
Composición: <qué se ve, quién, dónde>
Texto en imagen: "<overlay exacto, corto>"  (o: sin texto)
Estilo: <ver paletas abajo>
Prompt Grok: <texto listo para pegar>
Alt text: <descripción para accesibilidad>
```

## Identidad visual vibe/vibe (observada)
- Logo/marca: **"v/v"** (aparece en gorros, carteles).
- Estética recurrente: **bloques tipo Minecraft / voxel**, personajes cúbicos, talleres, robots, chispas.
- Colores del ecosistema Robinhood: **verde (#00C805-ish) + negro + blanco**, a veces **amarillo/pluma**.
- Tono: irónico, "build in public", anti-sniper, pro-creador. Nada de charts serios.

## Paletas de estilo para el prompt
- **vibe/vibe meme**: "blocky voxel / Minecraft-style 3D render, chunky characters, workshop or trading-floor setting, green and black palette, playful, meme caption top and bottom, clean lighting"
- **explicador**: "flat vector diagram, 2 colors on off-white, thick strokes, labeled boxes and arrows, no gradients, legible at thumbnail size"
- **retro/edu**: "1950s educational poster, limited palette, halftone texture"

## Reglas
- Texto en imagen: máx ~7 palabras, alto contraste, legible en miniatura.
- Nunca logos de terceros que impliquen endorsement (Robinhood/PancakeSwap oficiales) salvo que sea claramente meme/comentario.
- Cero caras de personas reales. Cero contenido que parezca comunicación oficial de un proyecto.
- Verificar que el meme no afirme algo falso (ej: "airdrop confirmado").
- Siempre dejar `Alt text`.

## Banco de conceptos vibe/vibe (para desarrollar)
| # | Concepto | Caption tentativo | Pilar |
|---|---|---|---|
| M1 | Creador vibe-codeando un token mientras 100 snipers cúbicos esperan en la puerta | "shipping the token / the snipers, waiting" | P3 |
| M2 | Dos cofres: uno "unrealized $38M" brillando, otro "realized" vacío | "the green number / your bank account" | P2 |
| M3 | Robot de trading idéntico ×1000 saliendo todos por la misma puerta angosta | "everyone's bot, same exit" | P2 |
| M4 | Personaje mirando 5 tokens llamados "SPARK", solo 1 con el contrato correcto brillando | "which $SPARK" | P3 |
| M5 | "Season 0" como obra en construcción voxel, cartel "5% SFUND — testnet only" | "farming season 0, the free way" | P3 |

## Log de imágenes usadas
(vacío — llenar cuando el usuario genere y publique)
`{"ts":"YYYY-MM-DD","concepto":"M?","draft":"...","grok_prompt_final":"...","publicada_en":"<url del post>"}`
