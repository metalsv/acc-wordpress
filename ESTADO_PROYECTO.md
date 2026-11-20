# ESTADO DEL PROYECTO — ACC · Maqueta web

> Leer esto antes de tocar cualquier archivo. Última actualización: **19 de noviembre de 2026**.
> Referencia larga de entrega: `ENTREGA.md`. Guía de método: skill `maqueta-web-cliente`.

---

## 1. Dónde vamos

| | |
|---|---|
| **Estado** | v1 entregada y verificada visualmente (8 pantallas + tablero + capturas) |
| **Cliente** | ACC Auditores y Consultores, Antiguo Cuscatlán, El Salvador |
| **Brief** | `PAGINA WEB ACC.md` (tabla de secciones + notas) · intención: `IDEA.md` |
| **Referencia visual del cliente** | demo *Consalt* (TemplateMonster 245667) — solo se tomó la estructura |
| **Dossier** | `ACC_dossier_diseno.pdf` — 32 páginas A4 horizontal, cerrado |
| **Siguiente paso** | revisión del cliente → ajustes de v2 (ver §6) |

**Nada está programado todavía**: es una maqueta estática en HTML/CSS/JS pensada para aprobar
diseño y contenido antes de pasar a WordPress / desarrollo.

---

## 2. Cómo abrir y cómo regenerar

```bash
cd ~/Documentos/mookup/acc
xdg-open index.html        # tablero de entrega (empezar aquí)
xdg-open home.html         # prototipo navegable
python3 build.py           # regenera los 9 HTML desde build.py
```

- Los HTML son **la salida**, no la fuente: se editan las funciones de `build.py`
  (`home_body()`, `nosotros_body()`, `servicios_body()`, etc.) y se vuelve a correr.
- Contenido repetido (servicios, socios, noticias, FAQ, categorías) vive en tablas al inicio de
  `build.py` (`SERVICES`, `CATS`, `SOCIOS`, `NEWS`, `FAQ`). **Editar ahí, nunca en el HTML.**
- No hay dependencias externas: tipografías autoalojadas en `assets/fonts/`, imágenes locales.
  El único elemento que pide internet es el iframe de Google Maps en `contacto.html` (tiene plano
  SVG de respaldo debajo).

---

## 3. Decisiones de diseño ya tomadas (no rehacer sin motivo)

**Idea rectora:** *el rigor de un estado financiero con calidez editorial.*
De ahí salen los recursos que dan unidad a las ocho pantallas:

- Retícula de líneas finas + secciones numeradas (`01 — 9 servicios`).
- **Marcas de corte** de imprenta en las esquinas de las fotografías (`.cropmark`).
- Cifras tabulares y etiquetas en monoespaciada (fechas, años, categorías, contadores).
- Fotografía en **duotono azul marino** en el hero; blanco y negro con color al pasar el cursor en
  el equipo.

**Paleta** (tokens en `assets/css/acc.css`)

| Token | Hex | Rol |
|---|---|---|
| `--navy` | `#0A2540` | principal: fondos, títulos, botones |
| `--navy-900` | `#06182B` | franjas y pie de página |
| `--orange` | `#E4702F` | CTA, acentos, numeración |
| `--sky` | `#8FC3E4` | datos sobre fondo oscuro |
| `--gray` | `#6C7C8C` | texto de apoyo |

**Tipografía:** Archivo (titulares y texto) · Instrument Serif itálica (acentos editoriales) ·
JetBrains Mono (etiquetas y cifras). Todas autoalojadas en `.woff2`.

**Marca provisional:** monograma de tres barras ascendentes + cuadro anaranjado, con firma
"AUDITORES Y CONSULTORES". Se sustituye cuando llegue el logotipo real.

---

## 4. Inventario de contenido

- **22 servicios** en 4 categorías: Auditoría (9), Consultoría Empresarial (2),
  Contabilidad e Impuestos (6), Otros (5). Salen del brief, literal.
- **8 preguntas frecuentes** redactadas (propuesta, no del cliente) → al final de `servicios.html`.
- **4 socios** de ejemplo con retratos de banco de imágenes (marcados como placeholder).
- **9 noticias** de ejemplo con fechas 2026, una destacada; `noticia.html` es la plantilla del
  artículo ("Reforma fiscal 2027").
- Cifras institucionales usadas: 18+ años, 65+ años de socios, 2018 ingreso a AGN, 193 firmas /
  85 países / 5 regiones.

---

## 5. Archivos

```
acc/
├── index.html … contacto.html   9 páginas (salida de build.py)
├── build.py                     generador único del sitio
├── ENTREGA.md                   documento de entrega para el cliente
├── ACC_dossier_diseno.pdf       dossier de 32 páginas para enviar
├── presentacion.html            origen del dossier (páginas A4)
├── presentacion.py              arma el dossier a partir de las capturas
├── ESTADO_PROYECTO.md           este archivo
├── PAGINA WEB ACC.md            brief original del cliente
├── assets/css/acc.css           sistema de diseño (~660 líneas)
├── assets/js/acc.js             filtros, buscador, FAQ, formulario, menú, toast
├── assets/fonts/                woff2 + fonts.css
├── assets/img/                  16 fotos optimizadas (p*.jpg, socio3, socia4)
├── pantallas/                   8 PNG página completa 1440 px + thumbs/ (jpg 900 px)
├── pantallas/movil/             tramos de viewport 390 px: home 1-5, servicios 1-3,
│                                nosotros 1-3, contacto 1-3
└── _refs/                       capturas del tema Consalt y referencias ya recortadas
```

---

## 6. Pendiente del cliente (bloquea la v2)

- [ ] Logotipo original en vector.
- [ ] Fotografías reales de oficina y equipo (las actuales son stock).
- [ ] Nombres, cargos y años reales de los socios.
- [ ] Textos definitivos de misión / visión / valores (el brief pedía cambiar la redacción).
- [ ] Logotipos vectoriales de AGN International y Camarasal.
- [ ] Confirmar ubicación del FAQ (hoy al final de Servicios; el brief dice "confirmar").
- [ ] Enlace real al sitio de AGN y a las redes sociales.
- [ ] Correo/dominio destino del formulario y política de datos.

## 7. Próximos pasos sugeridos (v2)

1. **Versión en inglés** — hoy el selector ES/EN solo avisa; falta traducir las 8 pantallas.
2. **CMS** — noticias con usuario editor y buscador servidor-side (hoy el buscador filtra en cliente).
3. **Formulario real** — endpoint, antispam, correo de acuse y aviso de privacidad.
4. **SEO** — metadatos por página, Open Graph, `sitemap.xml`, datos estructurados de `LocalBusiness`.
5. **Accesibilidad** — foco visible, skip-link, contraste del texto blanco al 72 % sobre marino.
6. **Página 404** y variante de servicio para las otras 21 fichas (hoy una sola plantilla de muestra).

---

## 8. Bitácora de correcciones (no repetir)

| Problema | Causa | Solución aplicada |
|---|---|---|
| Rejilla a 2 columnas en móvil | `.svc--cta{grid-column:span 2}` crea columna implícita | `grid-column:auto` en el breakpoint de 680 px |
| Scroll horizontal en móvil | panel de navegación fijo con `translateX(100%)` | `overflow-x:clip` en `html` y `body` |
| Secciones vacías en capturas | `.reveal` esperando IntersectionObserver | `.is-in` forzado antes de exportar + gate `.js-anim` |
| Huecos blancos en fotos exportadas | `loading="lazy"` fuera del viewport | pasar a `eager` y recorrer la página antes de capturar |
| Grid con 2 columnas que no se corregía | fila superior con `span 2` | ver primera fila |
| Dos socios con la misma cara | banco de imágenes repetido | verificar el mosaico final de retratos |
| Retrato masculino con nombre femenino | foto asumida sin mirar | revisar cada retrato contra su nombre |
| PNG móvil ilegible / corrupto | página completa de 10 441 px | capturar en tramos de viewport |
| Mapa gris en la captura | el iframe no pinta en captura estática | plano SVG dibujado debajo del iframe |

---

## 9. Criterios de calidad a mantener al ajustar

- Toda pantalla se revisa **mirando la página completa**, no solo el pliegue.
- Cualquier cifra o dato nuevo entra en `build.py`, no escrito a mano en el HTML.
- Nada de CDN: si se agrega un recurso, se autoaloja.
- Los nombres, fotos y noticias de ejemplo se declaran como placeholder en `ENTREGA.md`.
- El dossier se rearma con `python3 presentacion.py` después de exportar las capturas; los cortes
  de página usan `pantallas/bands.json` (bordes de sección medidos), así que si cambia el alto de
  una sección hay que volver a medir ese archivo.
- El PDF se imprime con el navegador (page.printToPDF, preferCSSPageSize) porque Firefox headless
  falla al rasterizar en este equipo.
