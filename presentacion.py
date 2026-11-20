#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera el dossier de diseño en PDF (A4 horizontal) a partir de las pantallas."""
import pathlib, struct, subprocess, sys, json

ROOT = pathlib.Path(__file__).parent
PDFDIR = ROOT / "pantallas" / "pdf"
PDFDIR.mkdir(parents=True, exist_ok=True)

# ── páginas de pantalla (nombre, archivo, título, subtítulo) ──────────────
SHEETS = [
    ("sistema", "Sistema de diseño", "Marca · color · tipografía · recursos · componentes", 1600),
    ("home", "Inicio", "Presentación, servicios, cifras, socios y noticias", 1440),
    ("nosotros", "Quiénes somos", "Historia, misión y visión, socios y afiliaciones", 1440),
    ("agn", "AGN International", "Red global, cinco regiones y ventajas", 1440),
    ("servicios", "Servicios", "22 servicios filtrables, proceso y preguntas frecuentes", 1440),
    ("servicio-auditoria-financiera", "Detalle de servicio", "Plantilla de ficha con alcance, entregables y proceso", 1440),
    ("noticias", "Noticias", "Nota destacada, rejilla y buscador", 1440),
    ("noticia", "Nota", "Plantilla de artículo con autor y relacionadas", 1440),
    ("contacto", "Contáctenos", "Datos, formulario y ubicación", 1440),
]

PAGE_W, PAGE_H = 1122, 793      # A4 horizontal a 96 dpi
IMG_W = 864                     # ancho de la captura en la página
BANDS = json.loads((ROOT / "pantallas" / "bands.json").read_text())
MARGIN = 56


def size(png):
    d = open(png, "rb").read(33)
    return struct.unpack(">II", d[16:24])


def jpg(name, w):
    src, dst = ROOT / "pantallas" / f"{name}.png", PDFDIR / f"{name}.jpg"
    subprocess.run(["magick", str(src), "-resize", f"{w}x", "-quality", "84",
                    "-background", "white", "-flatten", str(dst)], check=True)
    return dst


def vertical(text):
    return f'<span class="vert">{text}</span>'


def band_page(img, name, title, idx, total, page, scale, offset):
    cap = f'<div class="vert"><b>{title}</b><span>{idx} / {total}</span></div>' if idx == 1 else ''
    return f"""
<div class="page band">
  <div class="shot"><img src="pantallas/pdf/{img}.jpg" style="width:{IMG_W}px;top:-{offset*scale:.1f}px"></div>
  <div class="gutter">
    {cap}
    <div class="pn">{page:02d}</div>
  </div>
</div>"""


def build():
    head = f"""<!DOCTYPE html>
<html lang="es"><head><meta charset="utf-8">
<title>ACC · Dossier de diseño</title>
<link rel="stylesheet" href="assets/css/acc.css">
<style>
  @page{{size:297mm 210mm;margin:0}}
  html,body{{margin:0;padding:0;background:#fff}}
  body{{-webkit-print-color-adjust:exact;print-color-adjust:exact}}
  .page{{width:{PAGE_W}px;height:{PAGE_H}px;position:relative;overflow:hidden;
        break-after:page;page-break-after:always;background:#fff}}
  .page:last-child{{break-after:auto;page-break-after:auto}}

  /* ── banda de pantalla ── */
  .band{{padding-top:0}}
  .shot{{position:absolute;left:{MARGIN}px;top:0;width:{IMG_W}px;height:{PAGE_H}px;overflow:hidden}}
  .shot img{{position:absolute;left:0;display:block}}
  .gutter{{position:absolute;right:0;top:0;width:{PAGE_W-IMG_W-MARGIN}px;height:{PAGE_H}px}}
  .vert{{position:absolute;right:38px;top:34px;text-align:right;max-width:180px;
        font-family:var(--mono);font-size:8.5px;text-transform:uppercase;line-height:1.6}}
  .vert b{{display:block;font-weight:500;letter-spacing:.16em;color:var(--navy);opacity:.55}}
  .vert span{{display:block;margin-top:5px;letter-spacing:.22em;color:var(--gray-400)}}
  .pn{{position:absolute;right:38px;bottom:30px;font-family:var(--mono);font-size:9.5px;
      letter-spacing:.14em;color:var(--gray-400)}}
  .edge{{position:absolute;left:0;top:0;width:3px;height:100%;background:var(--orange);opacity:0}}
  .band:first-of-type .edge{{opacity:1}}

  /* ── portada ── */
  .cover{{background:var(--navy);color:#fff;display:flex;flex-direction:column;justify-content:space-between}}
  .cover__in{{padding:{MARGIN+18}px {MARGIN+10}px 0;position:relative;z-index:2}}
  .cover .eyebrow{{color:var(--sky)}}
  .cover .eyebrow::before{{background:var(--sky)}}
  .cover h1{{font-size:104px;font-weight:700;letter-spacing:-.05em;line-height:.86;margin-top:26px}}
  .cover h1 em{{font-family:var(--serif);font-style:italic;font-weight:400;color:var(--sky);letter-spacing:0}}
  .cover__sub{{margin-top:26px;max-width:52ch;color:rgba(255,255,255,.72);font-size:15px;line-height:1.7}}
  .cover__meta{{display:flex;gap:34px;margin-top:40px;flex-wrap:wrap}}
  .cover__meta div{{border-left:1px solid rgba(255,255,255,.22);padding-left:14px}}
  .cover__meta b{{display:block;font-family:var(--mono);font-size:8.5px;letter-spacing:.18em;
                 text-transform:uppercase;color:rgba(255,255,255,.45);font-weight:500;margin-bottom:6px}}
  .cover__meta span{{font-size:13px}}
  .cover__strip{{display:grid;grid-template-columns:2fr 1fr 1fr;gap:2px;height:196px;position:relative;z-index:2}}
  .cover__strip figure{{margin:0;overflow:hidden;position:relative}}
  .cover__strip img{{width:100%;height:100%;object-fit:cover;filter:grayscale(1) contrast(1.05)}}
  .cover__strip figure::after{{content:"";position:absolute;inset:0;background:rgba(10,37,64,.5);mix-blend-mode:multiply}}
  .cover__logo{{position:absolute;right:{MARGIN+10}px;top:{MARGIN+18}px;z-index:3;text-align:right}}
  .cover__logo svg{{width:52px;height:52px;margin-left:auto;display:block}}
  .cover__logo .brand__name{{font-size:20px;color:#fff;display:block;margin-top:12px;letter-spacing:-.03em}}
  .cover__logo .brand__sub{{font-family:var(--mono);font-size:7.5px;letter-spacing:.2em;
                           text-transform:uppercase;color:rgba(255,255,255,.55);display:block;margin-top:5px}}

  /* ── índice ── */
  .sheet{{padding:{MARGIN}px {MARGIN+10}px}}
  .sheet h2{{font-size:44px;font-weight:700;letter-spacing:-.035em;line-height:1;margin-top:14px}}
  .toc{{display:grid;grid-template-columns:1fr 1fr;grid-template-rows:repeat(5,auto);grid-auto-flow:column;gap:0 56px;margin-top:38px}}
  .toc__row{{display:grid;grid-template-columns:38px minmax(0,1fr);gap:14px;padding:13px 0;
            border-bottom:1px solid var(--line-soft);align-items:baseline}}
  .toc__row b{{font-family:var(--mono);font-size:9.5px;letter-spacing:.14em;color:var(--orange);font-weight:500}}
  .toc__row h3{{font-size:15px;font-weight:600;letter-spacing:-.01em}}
  .toc__row p{{font-size:11.5px;color:var(--gray);line-height:1.5;margin-top:3px}}
  .toc__pal>span:first-child{{font-family:var(--mono);font-size:9.5px;letter-spacing:.18em;text-transform:uppercase;color:var(--gray);font-weight:500}}
  .toc__pal{{display:flex;align-items:center;gap:18px;margin-top:38px;padding-top:18px;border-top:1px solid var(--line)}}
  .toc__chips{{display:flex;gap:0}}
  .toc__chips span{{width:44px;height:26px;display:block}}
  .toc__hex{{font-family:var(--mono);font-size:9px;letter-spacing:.12em;color:var(--gray-400)}}
  .toc__note{{margin-top:26px;font-size:11.5px;color:var(--gray);line-height:1.6;max-width:74ch}}

  /* ── cierre ── */
  .end{{background:var(--navy);color:#fff;display:flex;flex-direction:column;justify-content:flex-start;
       padding:{MARGIN+14}px {MARGIN+10}px}}
  .end h2{{font-size:64px;font-weight:700;letter-spacing:-.045em;line-height:.96;margin-top:22px}}
  .end h2 em{{font-family:var(--serif);font-style:italic;font-weight:400;color:var(--sky);letter-spacing:0}}
  .end__list{{display:grid;grid-template-columns:repeat(3,1fr);gap:32px;margin-top:56px;padding-top:26px;border-top:1px solid rgba(255,255,255,.14)}}
  .end__list h4{{font-family:var(--mono);font-size:9px;letter-spacing:.18em;text-transform:uppercase;
                color:var(--sky);font-weight:500;margin-bottom:10px}}
  .end__list p{{font-size:12.5px;line-height:1.65;color:rgba(255,255,255,.7)}}
  .end__foot{{margin-top:auto;display:flex;justify-content:space-between;gap:20px;font-family:var(--mono);font-size:9.5px;
             letter-spacing:.14em;text-transform:uppercase;color:rgba(255,255,255,.45);flex-wrap:wrap}}
</style></head><body>"""

    # portada
    pages = [f"""
<div class="page cover">
  <div class="cover__logo">
    <svg viewBox="0 0 44 44" aria-hidden="true">
      <rect width="44" height="44" fill="#fff"/>
      <rect x="9" y="22" width="4" height="13" fill="#0A2540"/>
      <rect x="16" y="16" width="4" height="19" fill="#0A2540"/>
      <rect x="23" y="10" width="4" height="25" fill="#0A2540"/>
      <rect x="30" y="10" width="6" height="6" fill="#E4702F"/>
    </svg>
    <span class="brand__name">ACC</span>
    <span class="brand__sub">Auditores y Consultores</span>
  </div>
  <div class="cover__in">
    <span class="eyebrow">Dossier de diseño · v1</span>
    <h1>Diseño del<br>sitio <em>web</em></h1>
    <p class="cover__sub">Nueve piezas: la hoja de sistema y las ocho pantallas del sitio, con su versión
    móvil. Una firma seria que no se ve fría: rigor de estado financiero con calidez editorial.</p>
    <div class="cover__meta">
      <div><b>Cliente</b><span>ACC Auditores y Consultores</span></div>
      <div><b>Piezas</b><span>Sistema + 8 pantallas + móvil</span></div>
      <div><b>Formato</b><span>Escritorio 1440 px · móvil 390 px</span></div>
      <div><b>Fecha</b><span>Noviembre 2026</span></div>
    </div>
  </div>
  <div class="cover__strip">
    <figure><img src="assets/img/p44.jpg" alt=""></figure>
    <figure><img src="assets/img/p21.jpg" alt=""></figure>
    <figure><img src="assets/img/p18.jpg" alt=""></figure>
  </div>
</div>"""]

    # índice
    rows = "".join(
        f'<div class="toc__row"><b>{i:02d}</b><div><h3>{t}</h3><p>{s}</p></div></div>'
        for i, (_, t, s, _) in enumerate(SHEETS, 1))
    pages.append(f"""
<div class="page sheet">
  <span class="eyebrow">Contenido</span>
  <h2>Las piezas de esta entrega</h2>
  <div class="toc">{rows}</div>
  <div class="toc__pal">
    <span class="label" style="margin:0">Paleta</span>
    <div class="toc__chips">
      <span style="background:#0A2540"></span><span style="background:#06182B"></span>
      <span style="background:#E4702F"></span><span style="background:#8FC3E4"></span>
      <span style="background:#6C7C8C"></span><span style="background:#F5F7F9;border:1px solid #EBEFF3"></span>
    </div>
    <span class="toc__hex">#0A2540 · #06182B · #E4702F · #8FC3E4 · #6C7C8C · #F5F7F9</span>
  </div>
  <p class="toc__note">Cada pieza se presenta a escala 60 % en páginas consecutivas: al recorrerlas se lee
  la pantalla completa, de arriba abajo, sin recortes arbitrarios. El recorrido interactivo —filtro de
  servicios, buscador de noticias, formulario— está en la versión navegable que acompaña a este dossier.</p>
</div>""")

    # bandas
    page = 3
    for name, title, sub, srcw in SHEETS:
        jpg(name, 1440 if srcw == 1440 else 1600)
        w, h = size(ROOT / "pantallas" / f"{name}.png")
        scale = IMG_W / w
        band = PAGE_H / scale
        tops = BANDS.get(name, {}).get("tops", [])
        # arranques de página: en un borde de sección si cae en el último cuarto
        starts, y = [], 0.0
        while y < h - 40:
            starts.append(y)
            nxt = [t for t in tops if t >= y + band * 0.72]
            y = (min(nxt) if nxt else y + band)
            if y > h: break
        total = len(starts)
        for i, off in enumerate(starts, 1):
            pages.append(band_page(name, title, f"{title}", i, total, page, scale, off))
            page += 1

    # cierre
    pages.append(f"""
<div class="page end">
  <div>
    <span class="eyebrow" style="color:var(--sky)">Siguiente paso</span>
    <h2>Del diseño<br>al sitio <em>publicado</em></h2>
  </div>
  <div class="end__list">
    <div><h4>01 · Revisión</h4><p>Comentarios del cliente por pantalla. Se ajusta lo que haga falta sobre el sistema, sin rehacer la identidad.</p></div>
    <div><h4>02 · Contenido</h4><p>Logotipo, fotografías reales, nombres de los socios y textos definitivos de misión, visión y valores.</p></div>
    <div><h4>03 · Producción</h4><p>Versión en inglés, publicación de noticias desde un usuario editor y conexión real del formulario.</p></div>
  </div>
  <div class="end__foot">
    <span>ACC Auditores y Consultores</span>
    <span>(503) 2535 9800 · info@grupoacc.com.sv</span>
    <span>Dossier de diseño · v1</span>
  </div>
</div>""")

    html = head + "\n".join(pages) + "\n</body></html>"
    (ROOT / "presentacion.html").write_text(html, encoding="utf-8")
    print(f"presentacion.html · {len(pages)} páginas")


if __name__ == "__main__":
    build()
