# Principios de Eichler Gold

Eichler Gold viene de las casas Eichler de los 50, los muebles Eames, la madera de teca y los afiches de la era atómica. La idea no es "retro": es **calidez, artesanía y geometría**, con el dorado como firma.

## Lo que lo hace reconocible

1. **Fondo de madera, no de pantalla.** El nogal `#1E1A16` es marrón, no gris ni negro. Nada de `#000`, `#111` o grises fríos.
2. **El dorado es la firma, y se usa poco.** Va en el acento, la selección, una línea bajo un título, el botón principal. Si todo es dorado, nada lo es.
3. **Texto sobre dorado siempre en nogal.** Nunca crema ni blanco (1.65:1, ilegible).
4. **Paneles con borde dorado apagado** de 2px y esquinas de 18px, sobre fondo nogal. Es la pieza que une GRUB, el escritorio y los atajos.
5. **Etiquetas en versalitas con mucho tracking** (`S I S T E M A`) en Josefin Sans y dorado apagado. Orden editorial, no "badges".
6. **Geometría de la era atómica como ilustración:** starburst, destellos de 4 puntas, boomerangs, círculos superpuestos en mostaza, naranja, teal y oliva. Formas planas, sin degradados.
7. **Grano sutil** sobre fondos grandes. Da textura de papel impreso.
8. **Tres fuentes, cada una con su papel:** Josefin Sans para títulos, Jost para texto, Space Mono para código, teclas y datos.

## Qué evitar (lo que hace que algo "se vea hecho con IA")

- Degradados morados, azules o arcoíris, y fondos con "blobs" difuminados.
- Glassmorphism: vidrio esmerilado, transparencias con blur.
- Inter, Roboto o la fuente del sistema como identidad.
- Tarjetas idénticas en rejilla de 3, todas con la misma sombra suave y `rounded-2xl`.
- Emojis como íconos o viñetas.
- Sombras de colores o con glow neón.
- Blanco puro `#FFFFFF` y negro puro `#000000`.
- Héroes con titular gigante centrado + subtítulo gris + dos botones, por defecto.
- Ilustraciones 3D genéricas o "isométricas de startup".

**Mejor:** composiciones asimétricas como el wallpaper (los motivos a un lado y el contenido al otro), jerarquía tipográfica clara, mucho aire, un solo acento por pantalla y detalles hechos a mano: filetes, teclas, sellos.

## Contraste (WCAG)

Modo **Nogal** (oscuro):

| Texto / fondo | Contraste | Uso |
|---|---|---|
| Crema / nogal | 13.6 | Texto normal |
| Dorado claro / nogal | 10.2 | Títulos |
| Dorado / nogal | 8.2 | Acentos, enlaces |
| Nogal / dorado | 8.2 | Texto de botón primario |
| Dorado apagado / nogal | 5.2 | Texto secundario, etiquetas |
| Oliva / nogal | 4.6 | Éxito |
| Naranja / nogal | 4.4 | Solo texto grande o íconos |
| Teal / nogal | 3.6 | Solo texto grande o ilustración |
| Crema / dorado | 1.65 | **Nunca** |

Modo **Papel** (claro), fondo `#F4ECDC`:

| Texto | Hex | Contraste |
|---|---|---|
| Nogal | `#1E1A16` | 14.7 |
| Bronce (en lugar del dorado) | `#7D661B` | 4.7 |
| Óxido (en lugar del naranja) | `#A55225` | 4.7 |
| Teal profundo | `#2B7471` | 4.7 |
| Musgo (en lugar del oliva) | `#616F3C` | 4.7 |

En modo papel, el dorado `#D4AF37` sigue sirviendo como **relleno** (botones, sellos), con texto nogal encima.
