# Eichler Gold

Base de estilo de Kaiser: Mid-Century Modern con nogal, teca y dorado. Inspirado en las casas Eichler, los muebles Eames, la madera de teca y los afiches de la era atómica.

Es el punto de partida para páginas, productos y diseños. Nació en [mintdistroconfiguration](https://github.com/FidelCaicedo/mintdistroconfiguration), donde vive aplicado a Linux Mint.

## Contenido

```
tokens/eichler-gold.tokens.json   fuente de verdad: colores, temas, fuentes, radios, sombras, espacios (formato W3C DTCG)
css/eichler-gold.css              variables CSS --eg-* y piezas base (panel, botones, tecla, filete, etiqueta, grano)
motifs/*.svg                      starburst, mini-burst, destello, boomerang (currentColor)
motifs/generate.py                regenera los SVG
assets/                           wallpaper 1920x1080, referencia visual principal
docs/principios.md                notas del estilo y tabla de contraste WCAG medida
index.html                        página de muestra (paleta, tipografía, piezas, motivos)
```

## Paleta

| Color | Hex | Uso |
|---|---|---|
| Nogal | `#1E1A16` | Fondo oscuro, texto en modo claro |
| Teca | `#3A2A1E` | Superficies, teclas |
| Dorado | `#D4AF37` | Acento principal |
| Dorado claro | `#E6C35C` | Hover, títulos |
| Dorado apagado | `#A8892C` | Bordes, etiquetas |
| Crema | `#EDE3CF` | Texto en modo oscuro |
| Papel | `#F4ECDC` | Fondo en modo claro |
| Mostaza | `#D9A441` | Ilustración |
| Naranja quemado | `#C8642D` | Avisos, ilustración |
| Teal | `#2E7D7A` | Ilustración |
| Oliva | `#7A8B4B` | Éxito, ilustración |

Para texto sobre papel: bronce `#7D661B`, óxido `#A55225`, teal profundo `#2B7471`, musgo `#616F3C` (todos AA).

**Regla clave:** texto sobre dorado siempre en nogal, nunca en crema.

## Fuentes

[Josefin Sans](https://fonts.google.com/specimen/Josefin+Sans) (títulos) · [Jost](https://fonts.google.com/specimen/Jost) (texto) · [Space Mono](https://fonts.google.com/specimen/Space+Mono) (código y teclas)

```html
<link href="https://fonts.googleapis.com/css2?family=Jost:wght@400;500;600&family=Josefin+Sans:wght@600;700&family=Space+Mono&display=swap" rel="stylesheet">
```

## Uso rápido

```html
<link rel="stylesheet" href="css/eichler-gold.css">
<body class="eg">                     <!-- modo nogal (oscuro) -->
<html data-theme="light">             <!-- modo papel (claro) -->
```

Las variables `--eg-*` se pueden mapear a cualquier librería (shadcn, Tailwind, etc.).
