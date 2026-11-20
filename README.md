# ACC · Sitio web — Auditores y Consultores

Base del proyecto del sitio web de **ACC Auditores y Consultores** (Antiguo Cuscatlán, El Salvador).

Este repositorio arranca con la **maqueta v1**: nueve pantallas estáticas en HTML/CSS/JS que fijan
diseño, retícula y contenido antes de pasar a producción.

> **Estado:** maqueta estática, pendiente de revisión del cliente. Todavía no hay código de WordPress.
> **Stack objetivo:** WordPress con tema propio. Sin plugins salvo los estrictamente esenciales.

---

## Estructura

```
.
├── index.html                              tablero de entrega (empezar aquí)
├── home.html                               prototipo navegable
├── nosotros.html  agn.html                 quiénes somos y red AGN International
├── servicios.html  servicio-auditoria-financiera.html
├── noticias.html  noticia.html             listado y plantilla de artículo
├── contacto.html  sistema.html             contacto y hoja de sistema de diseño
├── build.py                                generador único de los 9 HTML
├── presentacion.py  presentacion.html      dossier A4 de presentación
├── ACC_dossier_diseno.pdf                  dossier de 32 páginas para el cliente
├── assets/css/acc.css                      sistema de diseño (tokens, componentes)
├── assets/js/acc.js                        filtros, buscador, FAQ, menú, formulario
├── assets/fonts/                           Archivo · Instrument Serif · JetBrains Mono (woff2)
├── assets/img/                             16 fotografías optimizadas
├── pantallas/                              capturas de cada pantalla a 1440 px
└── pantallas/movil/                        tramos de viewport a 390 px
```

## Uso

Abrir `index.html` con doble clic: funciona sin internet y sin instalar nada
(el único elemento que pide red es el mapa de Google en `contacto.html`, que tiene un plano SVG de respaldo).

Regenerar las pantallas después de editar:

```bash
python3 build.py
```

## Reglas del proyecto

- **Los HTML son salida, no fuente.** Se editan las funciones de `build.py` (`home_body()`,
  `servicios_body()`…) y se vuelve a correr. El contenido repetido (servicios, socios, noticias,
  FAQ, categorías) vive en las tablas `SERVICES`, `CATS`, `SOCIOS`, `NEWS`, `FAQ` al inicio del archivo.
- **Sin CDN.** Todo recurso se autoaloja en `assets/`.
- **Nada de datos inventados en el HTML.** Cualquier cifra nueva entra en `build.py`.
- **Sin plugin de WordPress** sin justificarlo antes: si algo se resuelve en el tema, se resuelve en el tema.
- Los nombres, retratos y noticias de ejemplo se mantienen marcados como *placeholder*.

## Pendiente del cliente

- [ ] Logotipo original en vector y logotipos de AGN International / Camarasal.
- [ ] Fotografías reales de oficina y equipo.
- [ ] Nombres, cargos y años reales de los socios.
- [ ] Textos definitivos de misión, visión y valores.
- [ ] Dominio y correo destino del formulario, más política de datos.

Detalle completo del estado: `ESTADO_PROYECTO.md` · Documento de entrega: `ENTREGA.md` ·
Brief original: `PAGINA WEB ACC.md`.

---

Los archivos de la carpeta `_refs/` (capturas de la plantilla de pago usada solo como referencia
de estructura) **no** se versionan por ser material de terceros con licencia.
