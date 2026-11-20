#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ACC — Generador de maqueta web.
Ejecutar:  python3 build.py
Genera los .html de la carpeta del proyecto a partir de un sistema único
(header, footer, contenido) para que todas las pantallas queden consistentes.
"""
import pathlib, textwrap

ROOT = pathlib.Path(__file__).parent
IMG = "assets/img"

# ══════════════════════════════════════════════════════════════════
#  ICONOS (trazo 1.5, 24×24)
# ══════════════════════════════════════════════════════════════════
I = {
 "shield": '<path d="M12 3 5 6v5.5c0 4.2 2.9 7.7 7 9.5 4.1-1.8 7-5.3 7-9.5V6l-7-3Z"/><path d="m9 12 2.2 2.2L15.5 10"/>',
 "chart": '<path d="M4 20V4M4 20h16"/><rect x="7.5" y="12" width="3" height="5"/><rect x="12.5" y="8.5" width="3" height="8.5"/><rect x="17.5" y="5.5" width="3" height="11.5"/>',
 "receipt": '<path d="M6 3h12v18l-3-2-3 2-3-2-3 2V3Z"/><path d="M9.5 8h5M9.5 12h5M9.5 16h2.5"/>',
 "layers": '<path d="m12 3 9 4.5-9 4.5-9-4.5L12 3Z"/><path d="m3 12 9 4.5 9-4.5"/><path d="m3 16.5 9 4.5 9-4.5"/>',
 "phone": '<path d="M6.6 3.5 4 4.4c-.9.3-1.4 1.2-1.2 2.1 1.1 7.9 7.4 14.2 15.3 15.3.9.2 1.8-.3 2.1-1.2l.9-2.6c.3-.8-.1-1.7-.9-2l-3-1.2c-.7-.3-1.5 0-1.9.6l-.9 1.3a13 13 0 0 1-5.3-5.3l1.3-.9c.6-.4.9-1.2.6-1.9l-1.2-3c-.3-.8-1.2-1.2-2-.9Z"/>',
 "mail": '<rect x="2.5" y="5" width="19" height="14" rx="1.5"/><path d="m3 6.5 9 6.5 9-6.5"/>',
 "pin": '<path d="M12 21.5s7-6.3 7-11.2A7 7 0 0 0 5 10.3c0 4.9 7 11.2 7 11.2Z"/><circle cx="12" cy="10" r="2.6"/>',
 "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7.5V12l3 2"/>',
 "arrow": '<path d="M4 12h15M13 5.5l6.5 6.5-6.5 6.5"/>',
 "arrow-up": '<path d="M12 20V4M5.5 10.5 12 4l6.5 6.5"/>',
 "search": '<circle cx="11" cy="11" r="7"/><path d="m16.5 16.5 4 4"/>',
 "check": '<path d="m4.5 12.5 5 5L20 7"/>',
 "check-circle": '<circle cx="12" cy="12" r="9"/><path d="m8 12.5 2.8 2.8L16.5 9"/>',
 "linkedin": '<path d="M4.5 8.5h3v10h-3zM6 4.2a1.8 1.8 0 1 0 0 3.6 1.8 1.8 0 0 0 0-3.6ZM10.5 18.5v-6c0-1.6.9-2.6 2.4-2.6 1.4 0 2.1.9 2.1 2.6v6h3v-6.4c0-3-1.6-4.4-3.9-4.4-1.5 0-2.6.7-3.6 2v-1.9h-3c.05 1.1 0 10 0 10Z"/>',
 "facebook": '<path d="M14.5 8.5H17V5h-2.5C12 5 10.5 6.6 10.5 9v1.5H8V14h2.5v7h3.2v-7h2.6l.4-3.5h-3V9.2c0-.5.2-.7.8-.7Z"/>',
 "instagram": '<rect x="3.5" y="3.5" width="17" height="17" rx="5"/><circle cx="12" cy="12" r="4"/><path d="M16.9 7.1h.01"/>',
 "x": '<path d="M4 4l7 8.2L4.6 20H7l5.2-6.2L17 20h3l-7.2-8.4L19.4 4h-2.4l-4.8 5.7L8.2 4H4Z"/>',
 "users": '<circle cx="9" cy="8" r="3.4"/><path d="M2.8 20c0-3.4 2.8-5.6 6.2-5.6s6.2 2.2 6.2 5.6"/><path d="M16 5.2a3.2 3.2 0 0 1 0 6.1M18.5 14.9c1.8.7 2.9 2.1 2.9 4.1"/>',
 "target": '<circle cx="12" cy="12" r="8.5"/><circle cx="12" cy="12" r="4.6"/><circle cx="12" cy="12" r="1"/>',
 "eye": '<path d="M2.5 12S6 5.8 12 5.8 21.5 12 21.5 12 18 18.2 12 18.2 2.5 12 2.5 12Z"/><circle cx="12" cy="12" r="3.1"/>',
 "scale": '<path d="M12 3.5V20M7 20h10M5 8h14M5 8l-2.6 5.6a3 3 0 0 0 5.2 0L5 8Zm14 0-2.6 5.6a3 3 0 0 0 5.2 0L19 8Z"/>',
 "building": '<path d="M4 20V6.5L12 3l8 3.5V20"/><path d="M4 20h16M9 20v-5h6v5"/><path d="M8 9h2M14 9h2M8 12.5h2M14 12.5h2"/>',
 "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.4 2.4 3.6 5.6 3.6 9s-1.2 6.6-3.6 9c-2.4-2.4-3.6-5.6-3.6-9S9.6 5.4 12 3Z"/>',
 "doc": '<path d="M6 3h8l4 4v14H6V3Z"/><path d="M14 3v4.5h4.5M9 12h6M9 15.5h6M9 8.5h2.5"/>',
 "briefcase": '<rect x="3" y="7.5" width="18" height="12.5" rx="1.6"/><path d="M9 7.5V5.8A1.8 1.8 0 0 1 10.8 4h2.4A1.8 1.8 0 0 1 15 5.8v1.7M3 12.5h18"/>',
 "tick": '<path d="m5 13 4.5 4.5L19 7"/>',
 "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
 "grid": '<rect x="3.5" y="3.5" width="7" height="7"/><rect x="13.5" y="3.5" width="7" height="7"/><rect x="3.5" y="13.5" width="7" height="7"/><rect x="13.5" y="13.5" width="7" height="7"/>',
 "compass": '<circle cx="12" cy="12" r="9"/><path d="m15.5 8.5-2 5-5 2 2-5 5-2Z"/>',
 "handshake": '<path d="m2.5 12 4-4 3 3 2.5-2.5L15 11l-1 6-2 1-2.5-2.5"/><path d="m21.5 10-4-4-3.2 3.2M8.5 8 12 4.5l4.5 4.5"/>',
 "spark": '<path d="M12 3v4M12 17v4M3 12h4M17 12h4M6 6l2.8 2.8M15.2 15.2 18 18M18 6l-2.8 2.8M8.8 15.2 6 18"/>',
}


def ico(name, cls=""):
    return (f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{I[name]}</svg>')


# ══════════════════════════════════════════════════════════════════
#  MARCA
# ══════════════════════════════════════════════════════════════════
LOGO = """<svg class="brand__mark" viewBox="0 0 44 44" aria-hidden="true">
  <rect width="44" height="44" fill="%s"/>
  <rect x="9" y="22" width="4" height="13" fill="%s"/>
  <rect x="16" y="16" width="4" height="19" fill="%s"/>
  <rect x="23" y="10" width="4" height="25" fill="%s"/>
  <rect x="30" y="10" width="6" height="6" fill="%s"/>
</svg>"""


def logo(dark=True):
    fg = "#FFFFFF" if dark else "#0A2540"
    return LOGO % ("#0A2540" if dark else "#0A2540", fg, fg, fg, "#E4702F")


def logo_mark_light():
    """Logo para fondos oscuros: el recuadro se vuelve blanco."""
    return """<svg class="brand__mark" viewBox="0 0 44 44" aria-hidden="true">
  <rect width="44" height="44" fill="#FFFFFF"/>
  <rect x="9" y="22" width="4" height="13" fill="#0A2540"/>
  <rect x="16" y="16" width="4" height="19" fill="#0A2540"/>
  <rect x="23" y="10" width="4" height="25" fill="#0A2540"/>
  <rect x="30" y="10" width="6" height="6" fill="#E4702F"/>
</svg>"""


NAV = [
    ("home.html", "Inicio"),
    ("nosotros.html", "Quiénes somos"),
    ("servicios.html", "Servicios"),
    ("noticias.html", "Noticias"),
    ("contacto.html", "Contáctenos"),
]

# ══════════════════════════════════════════════════════════════════
#  DATOS
# ══════════════════════════════════════════════════════════════════
CATS = {
    "auditoria": "Auditoría",
    "consultoria": "Consultoría Empresarial",
    "contabilidad": "Contabilidad e Impuestos",
    "otros": "Otros",
}

SERVICES = [
    ("auditoria", "Auditoría Financiera", "Dictamen independiente sobre la razonabilidad de los estados financieros, bajo NIIF y normas de auditoría vigentes.", "shield"),
    ("auditoria", "Auditoría Fiscal", "Revisión del cumplimiento tributario y conciliación entre la contabilidad y las declaraciones presentadas.", "receipt"),
    ("auditoria", "Due Diligence", "Análisis financiero, fiscal y legal previo a una compra, fusión o inversión.", "search"),
    ("auditoria", "Auditoría Forense", "Investigación de irregularidades, fraudes y malas prácticas con evidencia documentada.", "eye"),
    ("auditoria", "Auditoría Interna", "Evaluación de controles y procesos, con planes de mejora priorizados por riesgo.", "grid"),
    ("auditoria", "Valuación de Empresas", "Valoración de negocios, activos y participaciones para decisiones de inversión o sucesión.", "chart"),
    ("auditoria", "Estudios de Precios de Transferencia", "Documentación y análisis de operaciones entre partes relacionadas conforme a la normativa.", "scale"),
    ("auditoria", "Cumplimiento Ley de Lavado de Dinero", "Auditoría de cumplimiento de la Ley contra el Lavado de Dinero y de Activos.", "shield"),
    ("auditoria", "Auditorías de Cumplimiento", "Verificación del cumplimiento normativo, regulatorio y de políticas internas.", "check-circle"),
    ("consultoria", "Asesoría Legal Mercantil", "Constitución, transformación y contratos societarios con acompañamiento permanente.", "scale"),
    ("consultoria", "Asesoría Empresarial", "Administración, finanzas, contabilidad, auditoría, fiscal y legal, con enfoque en cumplimiento.", "briefcase"),
    ("contabilidad", "Outsourcing de Contabilidad", "Contabilidad mensual, estados financieros y libros legales bajo responsabilidad de la firma.", "doc"),
    ("contabilidad", "Impuestos e Informes de Hacienda", "Elaboración de impuestos y presentación de informes ante el Ministerio de Hacienda.", "receipt"),
    ("contabilidad", "Planillas y Cálculo de Renta", "Elaboración de planillas y cálculo anual de renta de los colaboradores.", "users"),
    ("contabilidad", "Planilla Única (ISSS, AFP, IPSFA)", "Cálculo y presentación de la planilla única y sus obligaciones asociadas.", "layers"),
    ("contabilidad", "Declaraciones de Alcaldías", "Presentación de declaraciones municipales y pago de tasas.", "building"),
    ("contabilidad", "Trámites del CNR", "Renovación de matrículas de comercio y otros trámites ante el Centro Nacional de Registros.", "doc"),
    ("otros", "Constitución de Sociedades", "Constitución de sociedades, nombramientos y formalización ante el CNR.", "building"),
    ("otros", "Liquidación de Sociedades", "Proceso de liquidación, avisos y cierre ordenado de operaciones.", "doc"),
    ("otros", "Diseño e Implementación de NIIF", "Diagnóstico, conversión y capacitación para la adopción de normas NIIF.", "chart"),
    ("otros", "Análisis Financieros", "Modelos, indicadores y proyecciones para decisiones de negocio y financiamiento.", "target"),
    ("otros", "Análisis y Planificación Fiscal", "Estrategia fiscal anual, revisión de contingencias y optimización legal de la carga tributaria.", "compass"),
]

SOCIOS = [
    ("p9.jpg", "Lic. Ricardo Méndez", "Socio Director · Auditoría", "22 años"),
    ("p54.jpg", "Lcda. Claudia Rivera", "Socia · Impuestos y Legal", "18 años"),
    ("socio3.jpg", "Lic. Andrés Portillo", "Socio · Consultoría", "15 años"),
    ("socia4.jpg", "Lcda. Beatriz Ayala", "Socia · Contabilidad", "12 años"),
]

NEWS = [
    ("p25.jpg", "Fiscal", "18 Nov 2026", "Reforma fiscal 2027: lo que cambia para las empresas salvadoreñas",
     "Nuevos plazos de presentación, ajustes en retenciones y el impacto en la planificación anual de las sociedades.", True),
    ("p24.jpg", "Normas", "06 Nov 2026", "NIIF 18: claves para presentar estados financieros con el nuevo formato",
     "La norma entra en vigor en 2027 y cambia la estructura de resultados. Le explicamos por dónde empezar.", False),
    ("p23.jpg", "Cumplimiento", "28 Oct 2026", "Prevención de lavado de dinero: nuevas exigencias de la UIF",
     "Los sujetos obligados deben reforzar su matriz de riesgo, sus controles y la evidencia documental.", False),
    ("p2.jpg", "Auditoría", "14 Oct 2026", "Due diligence: cuándo conviene iniciarlo y qué documentos pedir",
     "El mejor momento para auditar una adquisición es antes de firmar la carta de intención.", False),
    ("p21.jpg", "Contabilidad", "30 Sep 2026", "Planilla única: cinco errores que generan observaciones de ISSS y AFP",
     "Desde salarios incompletos hasta incapacidades mal registradas, los detalles que más se repiten.", False),
    ("p15.jpg", "Impuestos", "12 Sep 2026", "Precios de transferencia: la documentación que su grupo debe tener lista",
     "Quiénes están obligados, qué debe contener el estudio y cómo se respalda ante Hacienda.", False),
    ("p6.jpg", "Opinión", "28 Ago 2026", "Por qué una auditoría no es un gasto, sino un instrumento de gestión",
     "Un dictamen limpio abre puertas con bancos, inversionistas y socios comerciales.", False),
    ("p27.jpg", "Firma", "10 Ago 2026", "ACC participa en la reunión regional de AGN International",
     "Nuestro equipo compartió experiencias sobre transformación digital en firmas de auditoría.", False),
    ("p18.jpg", "Auditoría", "24 Jul 2026", "Auditoría interna: cómo priorizar los riesgos que realmente importan",
     "Una matriz de riesgo bien construida evita auditar por costumbre y concentra el esfuerzo donde hay exposición.", False),
]

FAQ = [
    ("¿Qué documentos necesito para iniciar una auditoría financiera?",
     "Los estados financieros del período, libros legales, conciliaciones bancarias, inventarios, contratos relevantes y las declaraciones de impuestos presentadas. En la reunión inicial entregamos una lista de requerimientos adaptada a su empresa."),
    ("¿Cuánto tiempo toma una auditoría?",
     "Una auditoría de estados financieros anuales de una empresa mediana suele tomar entre tres y cinco semanas desde la entrega completa de la información. El plazo se define en la carta de compromiso y depende del volumen de operaciones y de la calidad de los registros."),
    ("¿Atienden empresas fuera de San Salvador?",
     "Sí. Trabajamos con clientes en todo el país y coordinamos la entrega de documentación de forma digital, con visitas programadas cuando el trabajo lo requiere."),
    ("¿Trabajan con personas naturales o solo sociedades?",
     "Atendemos personas naturales con actividad económica, profesionales independientes y sociedades de todos los tamaños, incluidas organizaciones sin fines de lucro."),
    ("¿Qué es AGN International y cómo me beneficia?",
     "AGN International es una asociación mundial de firmas independientes de contadores y asesores de negocios. Ser miembros nos permite atender operaciones internacionales, acceder a especialistas en 85 países y aplicar estándares globales de trabajo."),
    ("¿Pueden llevar la contabilidad completa de mi empresa?",
     "Sí, mediante nuestro servicio de outsourcing contable: registro mensual, libros legales, estados financieros, planillas y cumplimiento de obligaciones ante Hacienda, ISSS, AFP y alcaldías."),
    ("¿Ofrecen acompañamiento ante inspecciones de Hacienda?",
     "Sí. Preparamos la documentación de respaldo, acompañamos al cliente durante el proceso y elaboramos la respuesta técnica a los requerimientos de la administración tributaria."),
    ("¿Cómo manejan la confidencialidad de la información?",
     "Todo el equipo firma acuerdos de confidencialidad. La información se resguarda en repositorios con acceso restringido y se mantiene la independencia exigida por el código de ética profesional."),
]


# ══════════════════════════════════════════════════════════════════
#  PLANTILLA
# ══════════════════════════════════════════════════════════════════
def shell(title, active, body, desc="ACC — Auditores y Consultores. Más de 18 años en auditoría, consultoría, impuestos y contabilidad en El Salvador."):
    nav_html = "".join(
        f'<a href="{href}"{" class=\"is-active\"" if href == active else ""}>{label}</a>'
        for href, label in NAV
    )
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="stylesheet" href="assets/css/acc.css">
</head>
<body>

<div class="topbar">
  <div class="wrap-wide">
    <div class="topbar__list">
      <a href="contacto.html">{ico('pin')} Urb. Madreselva II, #57, Antiguo Cuscatlán</a>
      <a href="tel:+50325359800">{ico('phone')} (503) 2535 9800</a>
      <a href="mailto:info@grupoacc.com.sv">{ico('mail')} info@grupoacc.com.sv</a>
    </div>
    <div class="topbar__right">
      <div class="lang" role="group" aria-label="Idioma">
        <button class="is-on" data-lang="es">ES</button><span>/</span><button data-lang="en">EN</button>
      </div>
      <div class="social">
        <a href="#" data-pending aria-label="LinkedIn">{ico('linkedin')}</a>
        <a href="#" data-pending aria-label="Facebook">{ico('facebook')}</a>
        <a href="#" data-pending aria-label="Instagram">{ico('instagram')}</a>
      </div>
    </div>
  </div>
</div>

<header class="header">
  <div class="wrap-wide header__inner">
    <a class="brand" href="home.html" aria-label="ACC, inicio">
      {logo()}
      <span class="brand__txt">
        <span class="brand__name">ACC</span>
        <span class="brand__sub">Auditores y Consultores</span>
      </span>
    </a>
    <nav class="nav" id="nav">{nav_html}</nav>
    <div class="header__cta">
      <a class="btn btn--navy" href="contacto.html">Solicitar una cita {ico('arrow')}</a>
      <button class="icon-btn burger" aria-label="Abrir menú" aria-expanded="false">{ico('menu')}</button>
    </div>
  </div>
</header>

<main>
{body}
</main>

<section class="newsletter">
  <div class="wrap newsletter__in">
    <div>
      <h3>Análisis fiscal y contable, una vez al mes</h3>
      <p>Suscríbase al boletín de ACC. Sin publicidad, solo información útil para su empresa.</p>
    </div>
    <form class="nl-form" novalidate>
      <input type="email" placeholder="Su correo electrónico" aria-label="Correo electrónico" required>
      <button type="submit">Suscribirme</button>
    </form>
  </div>
</section>

<footer class="footer">
  <div class="wrap">
    <div class="footer__grid">
      <div class="footer__about">
        <a class="brand" href="home.html" aria-label="ACC, inicio">
          {logo_mark_light()}
          <span class="brand__txt">
            <span class="brand__name" style="color:#fff">ACC</span>
            <span class="brand__sub" style="color:rgba(255,255,255,.55)">Auditores y Consultores</span>
          </span>
        </a>
        <p>Firma salvadoreña con más de 18 años de experiencia en auditoría, consultoría, impuestos y contabilidad. Miembro de AGN International desde 2018.</p>
        <div class="social">
          <a href="#" data-pending aria-label="LinkedIn">{ico('linkedin')}</a>
          <a href="#" data-pending aria-label="Facebook">{ico('facebook')}</a>
          <a href="#" data-pending aria-label="Instagram">{ico('instagram')}</a>
        </div>
      </div>
      <div>
        <h4>Firma</h4>
        <ul class="footer__list">
          <li><a href="nosotros.html">Quiénes somos</a></li>
          <li><a href="nosotros.html#profesionales">Nuestros socios</a></li>
          <li><a href="agn.html">AGN International</a></li>
          <li><a href="noticias.html">Noticias</a></li>
          <li><a href="contacto.html">Contáctenos</a></li>
        </ul>
      </div>
      <div>
        <h4>Servicios</h4>
        <ul class="footer__list">
          <li><a href="servicios.html#auditoria">Auditoría</a></li>
          <li><a href="servicios.html#consultoria">Consultoría Empresarial</a></li>
          <li><a href="servicios.html#contabilidad">Contabilidad e Impuestos</a></li>
          <li><a href="servicios.html#otros">Otros servicios</a></li>
          <li><a href="servicios.html#faq">Preguntas frecuentes</a></li>
        </ul>
      </div>
      <div>
        <h4>Contacto</h4>
        <ul class="footer__contact">
          <li>{ico('pin')}<span>Urb. Madreselva II, #57,<br>Antiguo Cuscatlán, La Libertad,<br>El Salvador</span></li>
          <li>{ico('phone')}<a href="tel:+50325359800">(503) 2535 9800</a></li>
          <li>{ico('mail')}<a href="mailto:info@grupoacc.com.sv">info@grupoacc.com.sv</a></li>
          <li>{ico('clock')}<span>Lunes a viernes, 8:00 – 17:00</span></li>
        </ul>
      </div>
    </div>
    <div class="footer__bottom">
      <span>© <span data-year>2026</span> ACC Auditores y Consultores. Todos los derechos reservados.</span>
      <nav>
        <a href="#" data-pending>Aviso de privacidad</a>
        <a href="#" data-pending>Términos de uso</a>
        <a href="contacto.html">Contáctenos</a>
      </nav>
    </div>
  </div>
</footer>

<script src="assets/js/acc.js"></script>
</body>
</html>
"""


def pagehead(crumbs, title, lead, stats=None):
    c = "".join(f'<a href="{h}">{t}</a><span>/</span>' if h else f'<span style="color:#fff">{t}</span>' for h, t in crumbs)
    st = ""
    if stats:
        st = '<div class="pagehead__stat">' + "".join(
            f'<div><b>{v}</b><span>{l}</span></div>' for v, l in stats) + "</div>"
    return f"""<section class="pagehead">
  <div class="wrap pagehead__in">
    <div>
      <div class="crumbs">{c}</div>
      <h1>{title}</h1>
      <p>{lead}</p>
    </div>
    {st}
  </div>
</section>"""


def sechead(eyebrow, title, aside="", center=False):
    cls = "sechead sechead--center" if center else "sechead"
    a = f'<div class="sechead__aside">{aside}</div>' if aside else ""
    return f"""<div class="{cls}">
  <div><span class="eyebrow">{eyebrow}</span><h2 class="h2">{title}</h2></div>
  {a}
</div>"""


def cta_band(title, text, primary=("contacto.html", "Agendar una cita"), secondary=("servicios.html", "Ver servicios")):
    return f"""<section class="cta">
  <div class="wrap cta__in">
    <div>
      <span class="eyebrow" style="color:var(--sky)">Siguiente paso</span>
      <h2 class="h2" style="margin-top:16px">{title}</h2>
      <p>{text}</p>
    </div>
    <div class="cta__actions">
      <a class="btn btn--primary" href="{primary[0]}">{primary[1]} {ico('arrow')}</a>
      <a class="btn btn--ghost" href="{secondary[0]}">{secondary[1]}</a>
    </div>
  </div>
</section>"""


# ══════════════════════════════════════════════════════════════════
#  1. HOME
# ══════════════════════════════════════════════════════════════════
def home_body():
    cat_cards = ""
    for i, (key, label) in enumerate(CATS.items(), 1):
        n = sum(1 for s in SERVICES if s[0] == key)
        sample = [s for s in SERVICES if s[0] == key][:3]
        items = "".join(f"<li>{s[1]}</li>" for s in sample)
        icons = {"auditoria": "shield", "consultoria": "briefcase", "contabilidad": "receipt", "otros": "layers"}
        descs = {
            "auditoria": "Dictámenes independientes, revisión de controles y estudios especializados con evidencia documentada.",
            "consultoria": "Acompañamiento en decisiones de negocio, estructura legal y cumplimiento normativo.",
            "contabilidad": "Contabilidad al día, planillas, impuestos y trámites ante Hacienda y el CNR.",
            "otros": "Constitución y liquidación de sociedades, NIIF, análisis y planificación fiscal.",
        }
        cat_cards += f"""<a class="card reveal" href="servicios.html#{key}">
      <div class="card__idx">{i:02d} — {n} servicios</div>
      <div class="card__ico">{ico(icons[key])}</div>
      <h3>{label}</h3>
      <p>{descs[key]}</p>
      <ul class="card__list">{items}</ul>
      <span class="link-arrow">Ver categoría {ico('arrow')}</span>
    </a>"""

    members = ""
    for ph, name, role, yrs in SOCIOS:
        members += f"""<div class="member reveal">
      <div class="member__ph"><img src="{IMG}/{ph}" alt="{name}" loading="lazy"></div>
      <div class="member__body"><b>{name}</b><span>{role}</span><em>{yrs}</em></div>
    </div>"""

    news = ""
    for ph, cat, date, title, exc, feat in NEWS[:3]:
        news += f"""<a class="post reveal" href="noticia.html">
      <div class="post__ph"><img src="{IMG}/{ph}" alt="" loading="lazy"><span class="post__cat">{cat}</span></div>
      <div class="post__body">
        <div class="post__meta"><span>{date}</span><span>5 min de lectura</span></div>
        <h3>{title}</h3>
        <p>{exc}</p>
        <span class="link-arrow">Leer nota {ico('arrow')}</span>
      </div>
    </a>"""

    return f"""
<section class="hero">
  <div class="hero__grid">
    <div class="hero__copy">
      <span class="eyebrow">Firma de auditoría y consultoría · El Salvador</span>
      <h1 class="display">Cifras claras,<br>decisiones <em>sólidas.</em></h1>
      <p class="hero__lead">Más de 18 años acompañando a empresas salvadoreñas en auditoría, consultoría, impuestos y contabilidad. Rigor técnico, criterio de negocio y el respaldo de una red global.</p>
      <div class="hero__actions">
        <a class="btn btn--primary" href="contacto.html">Solicitar una cita {ico('arrow')}</a>
        <a class="btn btn--ghost" href="servicios.html">Nuestros servicios</a>
      </div>
    </div>
    <div class="hero__media">
      <img src="{IMG}/p44.jpg" alt="Firma de documentación contable">
      <div class="hero__tag">
        <strong>Miembros de AGN International</strong>
        <span>193 firmas en 85 países, un solo estándar de trabajo.</span>
      </div>
      <div class="hero__ghost">18</div>
    </div>
  </div>
</section>

<section class="trust">
  <div class="wrap">
    <div class="trust__label">Respaldo internacional<br>y gremial</div>
    <div class="trust__logos">
      <a href="agn.html" aria-label="AGN International">
        <span class="logo-mark">
          <span class="logo-mark__box">AGN</span>
          <span class="logo-mark__txt"><b>INTERNATIONAL</b><small>Miembro desde 2018</small></span>
        </span>
      </a>
      <a href="#" data-pending aria-label="CAMARASAL">
        <span class="logo-mark">
          <span class="logo-mark__box" style="border-radius:50%">C</span>
          <span class="logo-mark__txt"><b>CAMARASAL</b><small>Cámara de Comercio e Industria</small></span>
        </span>
      </a>
      <a href="#" data-pending aria-label="Colegio de Contadores">
        <span class="logo-mark" style="opacity:.85">
          <span class="logo-mark__txt" style="text-align:left"><b>CONSEJO DE VIGILANCIA</b><small>Contaduría Pública · SV</small></span>
        </span>
      </a>
    </div>
    <a class="link-arrow" href="nosotros.html" style="color:#fff">Conocer la firma {ico('arrow')}</a>
  </div>
</section>

<section class="section">
  <div class="wrap">
    {sechead("Lo que hacemos",
             "Cuatro áreas, un mismo estándar de trabajo",
             '<p class="lead" style="margin-bottom:18px">Auditoría, consultoría, impuestos y contabilidad trabajando de forma coordinada: el mismo equipo conoce su operación completa.</p><a class="link-arrow" href="servicios.html">Ver los 22 servicios ' + ico('arrow') + '</a>')}
    <div class="cards" style="margin-top:46px">{cat_cards}</div>
  </div>
</section>

<section class="section bg-2">
  <div class="wrap">
    <div class="split" style="align-items:stretch">
      <div class="figure figure--fill reveal">
        <span class="cropmark cropmark--tl"></span><span class="cropmark cropmark--br"></span>
        <img src="{IMG}/p21.jpg" alt="Reunión de trabajo con documentación contable">
        <div class="figure__tag"><span>Desde 2001</span><b>Dos prácticas que se volvieron una firma</b></div>
      </div>
      <div>
        <span class="eyebrow">Por qué elegirnos</span>
        <h2 class="h2" style="margin-top:18px">El detalle técnico<br>se nota en los resultados</h2>
        <p class="lead" style="margin-top:20px">Nuestros socios suman más de 65 años de experiencia profesional en bancos, empresas industriales, comerciales y de servicios, además de proyectos gubernamentales y de ONG.</p>
        <div class="feats" style="margin-top:40px;grid-template-columns:1fr">
          <div class="feat">
            <span class="feat__num">01</span>
            <h3>Criterio, no solo cumplimiento</h3>
            <p>Traducimos los hallazgos en decisiones: qué corregir, en qué orden y con qué impacto en el negocio.</p>
          </div>
          <div class="feat">
            <span class="feat__num">02</span>
            <h3>Un solo equipo para todo el ciclo</h3>
            <p>Auditoría, impuestos y contabilidad bajo el mismo responsable, sin traspasos de información ni reprocesos.</p>
          </div>
          <div class="feat">
            <span class="feat__num">03</span>
            <h3>Estándar internacional</h3>
            <p>Metodologías alineadas a AGN International y a las normas NIIF, con revisión de calidad independiente.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="bg-navy section--tight" style="padding-top:clamp(40px,4vw,56px)">
  <div class="wrap">
    <div class="stats">
      <div class="stat"><b>18<i>+</i></b><span>Años de experiencia en el mercado salvadoreño</span></div>
      <div class="stat"><b>22</b><span>Servicios especializados en cuatro áreas</span></div>
      <div class="stat"><b>65<i>+</i></b><span>Años de experiencia acumulada de nuestros socios</span></div>
      <div class="stat"><b>85</b><span>Países cubiertos por la red AGN International</span></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="split" style="grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr)">
      <div>
        <span class="eyebrow">Nuestro equipo</span>
        <h2 class="h2" style="margin-top:18px">Quiénes firman<br>su dictamen</h2>
        <p class="lead" style="margin-top:20px">Cuatro socios con experiencia en firmas internacionales y en sectores regulados. Detrás de cada trabajo hay un socio responsable identificable.</p>
        <a class="btn btn--outline" href="nosotros.html#profesionales" style="margin-top:28px">Conocer al equipo {ico('arrow')}</a>
      </div>
      <div class="team team--duo">{members}</div>
    </div>
  </div>
</section>

<section class="bg-2">
  <div class="wrap quote">
    <div class="quote__split">
      <div>
        <span class="eyebrow eyebrow--plain">Nuestra forma de trabajar</span>
        <blockquote style="margin-top:24px">“Una auditoría bien hecha no busca errores: <em>ordena la casa</em> para que la empresa pueda crecer.”</blockquote>
        <div class="quote__who">
          <img src="{IMG}/p9.jpg" alt="">
          <div><b>Lic. Ricardo Méndez</b><span>Socio Director</span></div>
        </div>
      </div>
      <div class="feats" style="grid-template-columns:1fr;gap:22px">
        <div class="feat"><span class="feat__num">NIIF</span><h3>Normas internacionales aplicadas</h3><p>Estados financieros comparables y defendibles ante bancos, inversionistas y reguladores.</p></div>
        <div class="feat"><span class="feat__num">UIF</span><h3>Cumplimiento de lavado de dinero</h3><p>Matriz de riesgo, controles y evidencia documental para sujetos obligados.</p></div>
        <div class="feat"><span class="feat__num">CNR</span><h3>Trámites societarios y registrales</h3><p>Constitución, matrículas de comercio y liquidaciones sin salir de la firma.</p></div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    {sechead("Actualidad", "Noticias y análisis de la firma",
             '<a class="link-arrow" href="noticias.html">Ver todas las noticias ' + ico('arrow') + '</a>')}
    <div class="news" style="margin-top:42px">{news}</div>
  </div>
</section>

{cta_band("Conversemos sobre el próximo cierre fiscal de su empresa",
          "Una primera reunión sin costo para revisar su situación y definir el alcance del trabajo.")}
"""


# ══════════════════════════════════════════════════════════════════
#  2. QUIÉNES SOMOS
# ══════════════════════════════════════════════════════════════════
def nosotros_body():
    socios = ""
    for ph, name, role, yrs in SOCIOS:
        socios += f"""<div class="member reveal">
      <div class="member__ph"><img src="{IMG}/{ph}" alt="{name}" loading="lazy"></div>
      <div class="member__body"><b>{name}</b><span>{role}</span><em>{yrs}</em></div>
    </div>"""

    return f"""
{pagehead([("home.html", "Inicio"), (None, "Quiénes somos")],
          "Una firma que creció<br>con sus clientes",
          "ACC es una firma con más de 18 años de experiencia en el mercado, ofreciendo servicios de auditoría, consultoría, impuestos y contabilidad.",
          [("18+", "años de experiencia"), ("2018", "miembros de AGN"), ("4", "socios")])}

<section class="section">
  <div class="wrap">
    <div class="split" style="align-items:start">
      <div>
        <span class="eyebrow">La firma</span>
        <h2 class="h2" style="margin-top:18px">Experiencia individual,<br>capacidad colectiva</h2>
        <p class="lead" style="margin-top:24px">Grupo ACC surge a partir de la fusión de dos prácticas exitosas que trabajaban en conjunto desde el año 2001, con la visión de combinar los conocimientos y la experiencia individual para crecer, ampliar y mejorar los servicios a nuestros clientes.</p>
        <p style="margin-top:18px;color:var(--gray)">A partir de junio de 2018 formamos parte de <a href="agn.html" style="color:var(--navy);text-decoration:underline;text-decoration-color:var(--sky);text-underline-offset:3px">AGN International</a>, una asociación mundial de firmas independientes de contadores y asesores de negocios, lo que nos permite atender operaciones internacionales con estándares globales.</p>
        <a class="btn btn--navy" href="agn.html" style="margin-top:30px">Ver nuestra red internacional {ico('arrow')}</a>
      </div>
      <div>
        <div class="figure figure--crop reveal" style="margin-bottom:26px">
          <span class="cropmark cropmark--tl"></span><span class="cropmark cropmark--br"></span>
          <img src="{IMG}/p42.jpg" alt="Oficinas de ACC en Antiguo Cuscatlán">
        </div>
        <div class="info" style="grid-template-columns:1fr">
          <div class="info__item"><div class="info__ico">{ico('building')}</div><div><b>Oficina</b><p>Urb. Madreselva II, #57, Antiguo Cuscatlán, La Libertad. A tres cuadras de Avianca Santa Elena.</p></div></div>
          <div class="info__item"><div class="info__ico">{ico('users')}</div><div><b>Equipo</b><p>Personal graduado de Licenciatura en Contaduría Pública y estudiantes de último año de la misma carrera.</p></div></div>
        </div>
      </div>
    </div>

    <div class="timeline">
      <div class="tl reveal"><span class="tl__year">2001</span><h3>Dos prácticas, un mismo método</h3><p>Comienzan a trabajar en conjunto dos firmas de auditoría y consultoría con cartera compartida.</p></div>
      <div class="tl reveal"><span class="tl__year">Fusión</span><h3>Nace Grupo ACC</h3><p>Se integran los equipos y se unifica la metodología bajo un solo estándar de calidad técnica.</p></div>
      <div class="tl reveal"><span class="tl__year">Junio 2018</span><h3>Miembros de AGN International</h3><p>La firma se incorpora a una red de 193 firmas en 85 países, con acceso a especialistas por industria.</p></div>
    </div>
  </div>
</section>

<section class="bg-navy section">
  <div class="wrap">
    {sechead("Misión, visión y valores", "Lo que sostiene cada trabajo",
             '<p class="lead" style="color:rgba(255,255,255,.62)">Tres definiciones que operan como criterio de revisión de nuestro propio trabajo, no como texto de pared.</p>')}
    <div class="mvv" style="margin-top:44px">
      <div>
        <h3>Misión</h3>
        <p>Brindar servicios de auditoría, consultoría, impuestos y contabilidad con excelencia técnica, aportando información confiable y oportuna para la toma de decisiones de nuestros clientes.</p>
      </div>
      <div>
        <h3>Visión</h3>
        <p>Ser la firma de referencia en El Salvador por la calidad de nuestro trabajo y por la cercanía con que acompañamos el crecimiento de las empresas que confían en nosotros.</p>
      </div>
      <div>
        <h3>Valores</h3>
        <ul>
          <li>Independencia e integridad profesional</li>
          <li>Confidencialidad en el manejo de la información</li>
          <li>Rigor técnico y mejora continua</li>
          <li>Compromiso con los plazos acordados</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section" id="profesionales">
  <div class="wrap">
    {sechead("Nuestros profesionales", "Nuestros socios",
             '<p class="lead">Amplia experiencia en auditoría, consultoría, impuestos y contabilidad. En conjunto suman más de 65 años de experiencia profesional.</p>')}
    <p style="margin-top:20px;color:var(--gray);max-width:72ch">Anterior a ACC habían trabajado en prestigiosas firmas de auditoría, lo que les permitió trabajar en muchos rubros: bancos, empresas industriales, comerciales y de servicios de diferentes tamaños, además de ejecutar proyectos gubernamentales y de ONG.</p>
    <div class="team team--four" style="margin-top:40px">{socios}</div>

    <div class="split" style="margin-top:clamp(56px,7vw,96px);align-items:center">
      <div class="figure figure--crop reveal">
        <span class="cropmark cropmark--tl"></span><span class="cropmark cropmark--br"></span>
        <img src="{IMG}/p44.jpg" alt="Revisión y firma de documentación contable">
        <div class="figure__tag"><span>Nuestro personal</span><b>Formación continua en NIIF y normativa fiscal</b></div>
      </div>
      <div>
        <span class="eyebrow">Nuestro personal</span>
        <h2 class="h2" style="margin-top:18px">Un equipo que<br>crece con la firma</h2>
        <p class="lead" style="margin-top:20px">Contamos con personal capacitado, en su mayoría graduados de la Licenciatura en Contaduría Pública y, en un porcentaje menor, estudiantes universitarios en sus últimos años de estudio de la misma carrera.</p>
        <div class="feats" style="grid-template-columns:1fr 1fr;margin-top:34px">
          <div class="feat"><span class="feat__num">01</span><h3>Supervisión por socio</h3><p>Cada trabajo tiene un responsable y una revisión de calidad antes de la entrega.</p></div>
          <div class="feat"><span class="feat__num">02</span><h3>Capacitación permanente</h3><p>Actualización anual en NIIF, auditoría y reformas tributarias.</p></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="bg-2 section">
  <div class="wrap">
    {sechead("Afiliaciones", "Somos miembros de", "", center=True)}
    <div style="display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:24px;margin-top:44px;max-width:900px;margin-left:auto;margin-right:auto">
      <a href="agn.html" class="card" style="padding:38px 32px">
        <div class="logo-mark" style="color:var(--navy)">
          <span class="logo-mark__box">AGN</span>
          <span class="logo-mark__txt"><b>INTERNATIONAL</b><small>Miembro desde junio 2018</small></span>
        </div>
        <h3 style="margin-top:22px">AGN International</h3>
        <p>Asociación mundial de firmas independientes de contadores y asesores de negocios: 193 firmas en 85 países.</p>
        <span class="link-arrow">Conocer la red {ico('arrow')}</span>
      </a>
      <div class="card" style="padding:38px 32px">
        <div class="logo-mark" style="color:var(--navy)">
          <span class="logo-mark__box" style="border-radius:50%">C</span>
          <span class="logo-mark__txt"><b>CAMARASAL</b><small>Cámara de Comercio e Industria de El Salvador</small></span>
        </div>
        <h3 style="margin-top:22px">Camarasal</h3>
        <p>Miembros activos del gremio empresarial que representa al sector comercio e industria del país.</p>
        <span class="mono muted" style="margin-top:16px">Afiliación vigente</span>
      </div>
    </div>
  </div>
</section>

{cta_band("¿Quiere conocer a quién llevaría su caso?",
          "Agende una reunión con el socio responsable del área que necesita y revise su situación con calma.")}
"""


# ══════════════════════════════════════════════════════════════════
#  3. AGN
# ══════════════════════════════════════════════════════════════════
def dot_sphere():
    """Globo de medios tonos + 5 nodos (uno por región) unidos al nodo central."""
    import math
    cx = cy = 210.0
    dots, r, ring = [], 62.0, 0
    while r <= 190:
        n = max(10, int(2 * math.pi * r / 15))
        off = (ring % 2) * (math.pi / n)
        for k in range(n):
            a = 2 * math.pi * k / n + off
            x = cx + r * math.sin(a)
            y = cy + r * math.cos(a)
            dr = 0.85 + (r - 62) / 128 * 1.4
            op = 0.15 + (r - 62) / 128 * 0.45
            dots.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{dr:.2f}" fill="#8FC3E4" opacity="{op:.2f}"/>')
        r += 13.5
        ring += 1
    nodes, arcs = [], []
    for ang in (-128, -64, 6, 66, 146):
        a = math.radians(ang)
        x = cx + 150 * math.sin(a)
        y = cy + 150 * math.cos(a)
        mx = cx + 150 * math.sin(a) * 0.5 + 30 * math.cos(a)
        my = cy + 150 * math.cos(a) * 0.5 - 30 * math.sin(a)
        arcs.append(f'<path d="M{cx:.0f} {cy:.0f} Q{mx:.1f} {my:.1f} {x:.1f} {y:.1f}" fill="none" stroke="#E4702F" stroke-width="1" stroke-dasharray="2.5 4" opacity=".6"/>')
        nodes.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="9" fill="#E4702F" opacity=".14"/><circle cx="{x:.1f}" cy="{y:.1f}" r="4" fill="#E4702F"/>')
    center = '<circle cx="210" cy="210" r="7.5" fill="#fff"/><circle cx="210" cy="210" r="3.4" fill="#0A2540"/>'
    return ('<svg viewBox="0 0 420 420" style="width:100%;height:auto;display:block" aria-hidden="true">'
            + "".join(dots) + "".join(arcs) + "".join(nodes) + center + '</svg>')


def agn_body():
    regions = [
        ("Norteamérica", "Estados Unidos y Canadá", "Firmas con práctica en SEC y normativa local."),
        ("Latinoamérica", "Incluye El Salvador", "Cobertura en Centro y Suramérica, en español y portugués."),
        ("Europa", "Unión Europea y Reino Unido", "Especialistas en NIIF, auditoría de grupos y compliance."),
        ("África y Medio Oriente", "Mercados en expansión", "Acompañamiento en inversiones y operaciones locales."),
        ("Asia-Pacífico", "Asia, Australia y Oceanía", "Soporte para cadenas de suministro y manufactura."),
    ]
    regs = "".join(f"""<div class="feat reveal">
      <span class="feat__num">{i:02d}</span>
      <h3 style="font-size:17px">{n}</h3>
      <p style="color:var(--navy);font-size:12.5px;margin-bottom:8px">{s}</p>
      <p style="font-size:13.5px">{d}</p>
    </div>""" for i, (n, s, d) in enumerate(regions, 1))

    return f"""
{pagehead([("home.html", "Inicio"), ("nosotros.html", "Quiénes somos"), (None, "AGN International")],
          "Una firma local<br>con alcance global",
          "Desde junio de 2018 formamos parte de AGN International: una asociación mundial de firmas independientes de contadores y asesores de negocios.")}

<section class="section">
  <div class="wrap">
    <div class="split" style="align-items:center">
      <div>
        <span class="eyebrow">La red</span>
        <h2 class="h2" style="margin-top:18px">193 firmas.<br>85 países. 5 regiones.</h2>
        <p class="lead" style="margin-top:22px">Los miembros de AGN International proveen auditorías, outsourcing de contabilidad y servicios de asesoría fiscal alrededor del mundo, con altos estándares de trabajo y servicio al cliente.</p>
        <p style="margin-top:18px;color:var(--gray)">A nivel regional y mundial, las firmas miembros colaboran para conocer las necesidades de los clientes y mejorar el servicio a través del intercambio de experiencia, conocimiento y la comprensión de cada mercado.</p>
        <div style="display:flex;gap:14px;margin-top:30px;flex-wrap:wrap">
          <a class="btn btn--navy" href="#" data-pending>Sitio de AGN International {ico('arrow')}</a>
          <a class="btn btn--outline" href="contacto.html">Consultar una operación internacional</a>
        </div>
      </div>
      <div class="figure reveal" style="background:var(--navy);padding:clamp(24px,4vw,48px);display:grid;place-items:center">
        <div style="width:100%;max-width:430px">{dot_sphere()}</div>
        <div style="position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);text-align:center;color:#fff">
          <b style="display:block;font-size:clamp(44px,6vw,72px);font-weight:700;letter-spacing:-.05em;line-height:1">193</b>
          <span class="mono" style="color:var(--sky);font-size:10px;letter-spacing:.2em">firmas miembros</span>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="bg-navy section--tight" style="padding-bottom:56px">
  <div class="wrap">
    <div class="stats">
      <div class="stat"><b>193</b><span>Firmas miembros en la red</span></div>
      <div class="stat"><b>85</b><span>Países con presencia</span></div>
      <div class="stat"><b>5</b><span>Regiones coordinadas</span></div>
      <div class="stat"><b>2018</b><span>Año de incorporación de ACC</span></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    {sechead("Cobertura", "Cinco regiones, un solo estándar",
             '<p class="lead">AGN International se encuentra entre las organizaciones de firmas de contadores más grandes del mundo. Cada región opera con metodologías homologadas y revisión de calidad cruzada.</p>')}
    <div class="feats" style="margin-top:44px;grid-template-columns:repeat(5,minmax(0,1fr));gap:24px">{regs}</div>
  </div>
</section>

<section class="bg-2 section">
  <div class="wrap">
    <div class="sechead sechead--center">
      <div><span class="eyebrow">Qué significa para su empresa</span><h2 class="h2">Ventajas concretas</h2></div>
    </div>
    <div class="cards" style="grid-template-columns:repeat(3,1fr);margin-top:44px;border:0;background:none;gap:24px">
      <div class="card" style="border:1px solid var(--line)">
        <div class="card__ico">{ico('globe')}</div>
        <h3>Operaciones en el exterior</h3>
        <p>Si su grupo tiene filiales o proveedores fuera del país, coordinamos el trabajo con la firma AGN local: una sola metodología y un solo informe.</p>
      </div>
      <div class="card" style="border:1px solid var(--line)">
        <div class="card__ico">{ico('users')}</div>
        <h3>Acceso a especialistas</h3>
        <p>Consultas directas con expertos por industria y por jurisdicción cuando el caso lo requiere, sin intermediarios.</p>
      </div>
      <div class="card" style="border:1px solid var(--line)">
        <div class="card__ico">{ico('shield')}</div>
        <h3>Revisión de calidad independiente</h3>
        <p>Nuestros trabajos pueden someterse a revisión por pares de otras firmas de la red, con estándares internacionales.</p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap" style="max-width:880px">
    <div class="quote" style="border-left:2px solid var(--orange);border-top:0;border-bottom:0;padding:0 0 0 32px">
      <blockquote style="font-size:clamp(22px,2.6vw,32px);max-width:none">“Una empresa salvadoreña puede auditarse con el mismo rigor que una empresa en Fráncfort. Eso es lo que aporta la red.”</blockquote>
      <div class="quote__who"><img src="{IMG}/socio3.jpg" alt=""><div><b>Lic. Andrés Portillo</b><span>Socio · Consultoría</span></div></div>
    </div>
  </div>
</section>

{cta_band("¿Su empresa opera fuera de El Salvador?",
          "Conversemos sobre cómo coordinar auditoría, impuestos y cumplimiento en más de un país.", ("contacto.html", "Hablar con un socio"), ("nosotros.html", "Volver a Quiénes somos"))}
"""


# ══════════════════════════════════════════════════════════════════
#  4. SERVICIOS
# ══════════════════════════════════════════════════════════════════
def servicios_body():
    svcs = ""
    for i, (cat, name, desc, icon) in enumerate(SERVICES, 1):
        svcs += f"""<a class="svc" data-cat="{cat}" href="servicio-auditoria-financiera.html">
      <span class="svc__bar"></span>
      <span class="svc__top"><span class="svc__cat">{CATS[cat]}</span><span class="svc__n">{i:02d}</span></span>
      <h3>{name}</h3>
      <p>{desc}</p>
      <span class="svc__go">Ver detalle {ico('arrow')}</span>
    </a>"""
    svcs += f"""<div class="svc svc--cta">
      <span class="svc__top"><span class="svc__cat">¿No encuentra lo que busca?</span><span class="svc__n">+</span></span>
      <h3>Armamos un alcance a la medida</h3>
      <p>Hay trabajos que no caben en un listado: revisiones puntuales, peritajes, informes para bancos o acompañamiento en una fiscalización.</p>
      <a class="link-arrow" href="contacto.html" style="margin-top:auto;padding-top:14px;font-size:13px">Cuéntenos su caso {ico('arrow')}</a>
    </div>"""

    filters = '<button class="filter is-on" data-filter="todos" aria-pressed="true">Todos <span data-count="todos">22</span></button>'
    for k, label in CATS.items():
        filters += f'<button class="filter" data-filter="{k}" aria-pressed="false">{label} <span data-count="{k}">0</span></button>'

    faq = ""
    for q, a in FAQ:
        faq += f"""<div class="faq__item">
      <button class="faq__q" aria-expanded="false"><span>{q}</span><span class="faq__ic"></span></button>
      <div class="faq__a"><p>{a}</p></div>
    </div>"""

    return f"""
{pagehead([("home.html", "Inicio"), (None, "Servicios")],
          "Servicios de auditoría,<br>consultoría e impuestos",
          "22 servicios organizados en cuatro áreas. Filtre por categoría para encontrar lo que su empresa necesita.",
          [("22", "servicios"), ("4", "categorías"), ("65+", "años de experiencia")])}

<section class="section--tight" style="padding-top:clamp(36px,4vw,52px)">
  <div class="wrap">
    <div class="filters">{filters}</div>
  </div>
</section>

<section style="padding-bottom:clamp(56px,6vw,90px)">
  <div class="wrap">
    <div class="svc-grid" data-services>{svcs}</div>
    <div class="empty">No hay servicios en esta categoría.</div>
  </div>
</section>

<section class="bg-2 section">
  <div class="wrap">
    <div class="split" style="align-items:center">
      <div>
        <span class="eyebrow">Cómo trabajamos</span>
        <h2 class="h2" style="margin-top:18px">Un proceso claro,<br>sin sorpresas</h2>
        <p class="lead" style="margin-top:20px">Cada servicio inicia con una carta de compromiso donde quedan definidos el alcance, los responsables, el calendario y los entregables.</p>
        <a class="btn btn--navy" href="contacto.html" style="margin-top:28px">Solicitar una propuesta {ico('arrow')}</a>
      </div>
      <div class="steps">
        <div class="step"><div><b>Reunión inicial</b><p>Entendemos la operación, el sector y el objetivo del trabajo.</p></div></div>
        <div class="step"><div><b>Propuesta y alcance</b><p>Carta de compromiso con honorarios, plazos y equipo asignado.</p></div></div>
        <div class="step"><div><b>Ejecución</b><p>Trabajo de campo, pruebas y comunicación de avances al cliente.</p></div></div>
        <div class="step"><div><b>Informe y hallazgos</b><p>Entrega del dictamen o informe con recomendaciones priorizadas.</p></div></div>
        <div class="step"><div><b>Seguimiento</b><p>Acompañamiento en la implementación de las mejoras acordadas.</p></div></div>
      </div>
    </div>
  </div>
</section>

<section class="section" id="faq">
  <div class="wrap" style="max-width:1040px">
    <div class="sechead sechead--center">
      <div><span class="eyebrow">Dudas frecuentes</span><h2 class="h2">Preguntas frecuentes</h2></div>
    </div>
    <div class="faq" style="margin-top:40px">{faq}</div>
    <p class="center muted" style="margin-top:28px;font-size:14px">¿Su pregunta no está aquí? <a href="contacto.html" style="color:var(--navy);font-weight:600;text-decoration:underline">Escríbanos</a> y le respondemos en un día hábil.</p>
  </div>
</section>

{cta_band("Su próxima auditoría puede empezar esta semana",
          "Cuéntenos qué necesita y le enviamos una propuesta con alcance y honorarios.")}
"""


# ══════════════════════════════════════════════════════════════════
#  5. DETALLE DE SERVICIO
# ══════════════════════════════════════════════════════════════════
def servicio_body():
    otros = "".join(f'<li><a href="#">{n} {ico("arrow")}</a></li>' for _, n, _, _ in SERVICES[1:7])
    return f"""
{pagehead([("home.html", "Inicio"), ("servicios.html", "Servicios"), ("servicios.html#auditoria", "Auditoría"), (None, "Auditoría Financiera")],
          "Auditoría Financiera",
          "Dictamen independiente sobre la razonabilidad de los estados financieros de su empresa, conforme a NIIF y a normas de auditoría aceptadas.")}

<section class="section">
  <div class="wrap">
    <div style="display:grid;grid-template-columns:minmax(0,1.55fr) minmax(0,.85fr);gap:clamp(28px,4vw,64px);align-items:start">
      <div>
        <div class="figure figure--crop reveal" style="margin-bottom:36px">
          <span class="cropmark cropmark--tl"></span><span class="cropmark cropmark--br"></span>
          <img src="{IMG}/p18.jpg" alt="Documentación de auditoría">
        </div>
        <span class="eyebrow">Qué incluye</span>
        <h2 class="h2" style="margin:16px 0 22px">Un dictamen que resiste preguntas</h2>
        <p class="lead">Revisamos los estados financieros con procedimientos de auditoría diseñados según el riesgo de su operación. El resultado no es solo un documento para el banco: es un diagnóstico de sus controles.</p>
        <ul class="article" style="margin-top:26px">
          <li>Planeación y evaluación de riesgos por rubro y por proceso.</li>
          <li>Pruebas sustantivas sobre saldos y transacciones significativas.</li>
          <li>Circularización de bancos, clientes y proveedores.</li>
          <li>Revisión del cumplimiento tributario y de las conciliaciones fiscales.</li>
          <li>Evaluación del control interno y carta de recomendaciones.</li>
          <li>Dictamen e informe de estados financieros auditados.</li>
        </ul>

        <div style="margin-top:52px">
          <span class="eyebrow">Entregables</span>
          <div class="cards" style="grid-template-columns:repeat(2,1fr);margin-top:24px">
            <div class="card"><div class="card__ico">{ico('doc')}</div><h3>Dictamen de auditoría</h3><p>Estados financieros auditados con notas, listos para presentar a bancos, socios o reguladores.</p></div>
            <div class="card"><div class="card__ico">{ico('shield')}</div><h3>Carta de control interno</h3><p>Hallazgos y recomendaciones priorizadas por riesgo, con responsable sugerido y plazo.</p></div>
          </div>
        </div>

        <div style="margin-top:52px">
          <span class="eyebrow">Proceso</span>
          <div class="steps" style="margin-top:20px">
            <div class="step"><div><b>Diagnóstico y planeación</b><p>Reunión con la administración, revisión de información preliminar y definición de materialidad.</p></div></div>
            <div class="step"><div><b>Trabajo de campo</b><p>Ejecución de procedimientos en sus instalaciones o de forma remota, según el rubro.</p></div></div>
            <div class="step"><div><b>Cierre y hallazgos</b><p>Discusión de ajustes y observaciones con la administración antes de emitir el dictamen.</p></div></div>
            <div class="step"><div><b>Entrega</b><p>Dictamen firmado, carta de recomendaciones y reunión de presentación de resultados.</p></div></div>
          </div>
        </div>
      </div>

      <aside>
        <div class="aside" style="background:var(--navy);color:#fff;border:0">
          <h4 style="color:var(--sky)">Solicitar este servicio</h4>
          <p style="font-size:14.5px;line-height:1.65;color:rgba(255,255,255,.78)">Cuéntenos el tamaño de su operación y el período a auditar. Le enviamos alcance y honorarios en un día hábil.</p>
          <a class="btn btn--primary" href="contacto.html" style="margin-top:20px;width:100%;justify-content:center">Agendar una reunión {ico('arrow')}</a>
          <a class="btn btn--ghost" href="tel:+50325359800" style="margin-top:10px;width:100%;justify-content:center">{ico('phone')} (503) 2535 9800</a>
        </div>
        <div class="aside">
          <h4>Categoría</h4>
          <p style="font-size:14px;font-weight:600">Auditoría</p>
          <p style="font-size:13px;color:var(--gray);margin-top:6px">9 servicios en esta categoría</p>
        </div>
        <div class="aside">
          <h4>Otros servicios de auditoría</h4>
          <ul>{otros}</ul>
        </div>
      </aside>
    </div>
  </div>
</section>

{cta_band("¿Necesita el dictamen para un plazo específico?",
          "Trabajamos con calendarios definidos desde la carta de compromiso. Consúltenos disponibilidad.")}
"""


# ══════════════════════════════════════════════════════════════════
#  6. NOTICIAS
# ══════════════════════════════════════════════════════════════════
def noticias_body():
    feat = NEWS[0]
    f = f"""<a class="post post--feature reveal" href="noticia.html" data-news-item>
      <div class="post__ph"><img src="{IMG}/{feat[0]}" alt=""><span class="post__cat">Destacado · {feat[1]}</span></div>
      <div class="post__body">
        <div class="post__meta"><span>{feat[2]}</span><span>6 min de lectura</span></div>
        <h3>{feat[3]}</h3>
        <p style="font-size:15px">{feat[4]}</p>
        <span class="link-arrow">Leer la nota completa {ico('arrow')}</span>
      </div>
    </a>"""

    grid = ""
    for ph, cat, date, title, exc, _ in NEWS[1:]:
        grid += f"""<a class="post reveal" href="noticia.html" data-news-item>
      <div class="post__ph"><img src="{IMG}/{ph}" alt="" loading="lazy"><span class="post__cat">{cat}</span></div>
      <div class="post__body">
        <div class="post__meta"><span>{date}</span><span>4 min</span></div>
        <h3>{title}</h3>
        <p>{exc}</p>
        <span class="link-arrow">Leer nota {ico('arrow')}</span>
      </div>
    </a>"""

    return f"""
{pagehead([("home.html", "Inicio"), (None, "Noticias")],
          "Noticias y análisis",
          "Reformas fiscales, normas contables y criterios de la firma. Publicaciones a cargo de nuestros socios.")}

<section class="section--tight" style="padding-top:clamp(32px,4vw,44px)">
  <div class="wrap" style="display:flex;align-items:center;justify-content:space-between;gap:24px;flex-wrap:wrap">
    <div class="filters">
      <button class="filter is-on">Todas</button>
      <button class="filter">Fiscal</button>
      <button class="filter">Auditoría</button>
      <button class="filter">Normas</button>
      <button class="filter">Contabilidad</button>
      <button class="filter">Firma</button>
    </div>
    <label class="searchbox">
      {ico('search')}
      <input type="search" placeholder="Buscar una noticia…" data-news-search aria-label="Buscar noticias">
      <button type="button" data-pending>Buscar</button>
    </label>
  </div>
</section>

<section style="padding-bottom:clamp(56px,6vw,88px)">
  <div class="wrap">
    <div style="display:flex;align-items:center;justify-content:space-between;gap:16px;margin:4px 0 24px;font-family:var(--mono);font-size:10.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--gray)">
      <span>9 publicaciones</span><span>Ordenadas por fecha</span>
    </div>
    {f}
    <div class="news" style="margin-top:clamp(26px,3vw,38px)">{grid}</div>
    <div class="empty" data-news-empty style="padding:70px 0">No encontramos noticias con ese término. Intente con “NIIF”, “planilla” o “auditoría”.</div>

    <div style="display:flex;justify-content:center;gap:8px;margin-top:52px">
      <button class="filter is-on" style="padding:10px 15px">1</button>
      <button class="filter" style="padding:10px 15px">2</button>
      <button class="filter" style="padding:10px 15px">3</button>
      <button class="filter" style="padding:10px 15px" data-pending>siguiente {ico('arrow')}</button>
    </div>
  </div>
</section>

{cta_band("Reciba estos análisis en su correo",
          "Un correo al mes con lo que cambia en materia fiscal y contable, explicado sin tecnicismos.", ("#", "Suscribirme"), ("contacto.html", "Contáctenos"))}
"""


# ══════════════════════════════════════════════════════════════════
#  7. NOTICIA (artículo)
# ══════════════════════════════════════════════════════════════════
def noticia_body():
    rel = ""
    for ph, cat, date, title, exc, _ in NEWS[1:4]:
        rel += f"""<a class="post" href="noticia.html">
      <div class="post__ph"><img src="{IMG}/{ph}" alt="" loading="lazy"><span class="post__cat">{cat}</span></div>
      <div class="post__body"><div class="post__meta"><span>{date}</span></div><h3 style="font-size:17px">{title}</h3><span class="link-arrow">Leer {ico('arrow')}</span></div>
    </a>"""
    return f"""
<section class="pagehead" style="padding-bottom:clamp(40px,4vw,56px)">
  <div class="wrap" style="max-width:900px">
    <div class="crumbs"><a href="home.html">Inicio</a><span>/</span><a href="noticias.html">Noticias</a><span>/</span><span style="color:#fff">Fiscal</span></div>
    <h1 style="font-size:clamp(30px,3.6vw,48px);line-height:1.08;margin-top:18px">Reforma fiscal 2027: lo que cambia para las empresas salvadoreñas</h1>
    <div style="display:flex;gap:24px;align-items:center;margin-top:26px;flex-wrap:wrap;color:rgba(255,255,255,.6);font-family:var(--mono);font-size:11px;letter-spacing:.1em;text-transform:uppercase">
      <span style="display:flex;align-items:center;gap:9px"><img src="{IMG}/p54.jpg" alt="" style="width:32px;height:32px;border-radius:50%;object-fit:cover"> Lcda. Claudia Rivera</span>
      <span>18 noviembre 2026</span><span>6 min de lectura</span>
    </div>
  </div>
</section>

<div class="wrap" style="max-width:1180px;margin-top:-1px">
  <div class="figure" style="aspect-ratio:21/9;overflow:hidden"><img src="{IMG}/p25.jpg" alt="Documentos fiscales sobre un escritorio"></div>
</div>

<section class="section" style="padding-top:clamp(44px,5vw,64px)">
  <div class="wrap">
    <div class="article">
      <a class="link-arrow" href="noticias.html" style="margin-bottom:28px">{ico('arrow-up')} Volver a noticias</a>
      <p class="article__lead">La reforma fiscal que entra en vigor en enero de 2027 modifica tres frentes que afectan directamente la operación de las empresas: los plazos de presentación, el tratamiento de retenciones y la documentación de respaldo exigida para deducciones. Ninguno es un cambio menor si la contabilidad se lleva al día.</p>
      <p>En la práctica, las empresas que ya trabajan con un cierre mensual ordenado tienen poco que ajustar. Las que concentran todo en el cierre anual son las que sentirán el impacto, porque los nuevos plazos no admiten prórrogas administrativas automáticas.</p>

      <h2>1. Plazos de presentación más cortos</h2>
      <p>El calendario tributario se adelanta y unifica vencimientos que antes estaban dispersos. Para el área contable esto significa reorganizar el cierre de mes: si el informe de resultados se entregaba el día 15, ahora debe estar disponible antes.</p>
      <blockquote>“El cambio no es de tasa, es de ritmo: quien tenga la información a tiempo no tendrá ningún problema.”</blockquote>

      <h2>2. Retenciones y su conciliación</h2>
      <p>Las retenciones de renta e IVA deberán conciliarse contra el detalle de proveedores en cada período. Recomendamos revisar el catálogo de proveedores y depurar duplicados antes de diciembre: la mayoría de diferencias que encontramos en auditoría nace ahí.</p>
      <ul>
        <li>Depurar el catálogo de proveedores y sus datos de identificación.</li>
        <li>Verificar la retención aplicada en cada factura del período.</li>
        <li>Documentar los casos de exención con el respaldo correspondiente.</li>
      </ul>

      <h2>3. Documentación de respaldo</h2>
      <p>La administración tributaria refuerza la exigencia de evidencia para gastos deducibles. Un comprobante de crédito fiscal no es suficiente: se requiere poder demostrar que el gasto corresponde a la operación.</p>
      <figure>
        <img src="{IMG}/p2.jpg" alt="Revisión de documentación financiera">
        <figcaption>Archivo de respaldo: la prueba documental define el resultado de una fiscalización.</figcaption>
      </figure>

      <h2>Qué hacer este trimestre</h2>
      <p>Nuestra recomendación es simple: haga un diagnóstico de su calendario actual contra el nuevo, identifique los tres procesos que se verán más presionados y ajuste desde ahora. Un cierre fiscal no se arregla en diciembre.</p>
      <p>Si necesita apoyo para esa revisión, nuestro equipo de impuestos puede acompañarle con un plan de trabajo de cuatro a seis semanas.</p>

      <div class="share">
        <b>Compartir</b>
        <a href="#" data-pending aria-label="LinkedIn">{ico('linkedin')}</a>
        <a href="#" data-pending aria-label="Facebook">{ico('facebook')}</a>
        <a href="#" data-pending aria-label="Correo">{ico('mail')}</a>
      </div>
    </div>
  </div>
</section>

<section class="bg-2 section">
  <div class="wrap">
    {sechead("Seguir leyendo", "Otras publicaciones", '<a class="link-arrow" href="noticias.html">Todas las noticias ' + ico('arrow') + '</a>')}
    <div class="news" style="margin-top:38px">{rel}</div>
  </div>
</section>

{cta_band("¿Cómo impacta esta reforma a su empresa?",
          "Revisamos su calendario tributario actual y le entregamos un plan de ajuste por escrito.")}
"""


# ══════════════════════════════════════════════════════════════════
#  8. CONTACTO
# ══════════════════════════════════════════════════════════════════
def map_svg():
    """Plano estilizado: respaldo visual si el iframe de Google Maps no carga."""
    grid = [(30, 30, 150, 90), (200, 30, 120, 90), (340, 30, 180, 60), (540, 30, 230, 110),
            (30, 150, 110, 120), (160, 150, 160, 70), (340, 110, 80, 110),
            (440, 150, 70, 90), (540, 160, 230, 80), (30, 300, 200, 120),
            (250, 250, 120, 80), (390, 260, 190, 70), (600, 260, 170, 160)]
    blocks = "".join(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#fff" stroke="#DDE5EC"/>'
                     for x, y, w, h in grid)
    streets = ('<path d="M0 140h800M0 285h800M0 405h800" stroke="#DDE5EC" stroke-width="14"/>'
               '<path d="M0 140h800M0 285h800M0 405h800" stroke="#F7FAFC" stroke-width="10"/>'
               '<path d="M330 0v450M520 0v450M730 0v450" stroke="#DDE5EC" stroke-width="12"/>'
               '<path d="M330 0v450M520 0v450M730 0v450" stroke="#F7FAFC" stroke-width="8"/>'
               '<path d="M0 470 L800 -20" stroke="#CFE0EC" stroke-width="24"/>'
               '<path d="M0 470 L800 -20" stroke="#EAF4FB" stroke-width="17"/>')
    labels = ('<text x="344" y="122" font-family="JetBrains Mono,monospace" font-size="9" fill="#9AA8B5" letter-spacing="1.5">AV. SANTA ELENA</text>'
              '<text x="58" y="278" font-family="JetBrains Mono,monospace" font-size="9" fill="#9AA8B5" letter-spacing="1.5">ANTIGUO CUSCATLÁN</text>'
              '<text x="556" y="404" font-family="JetBrains Mono,monospace" font-size="9" fill="#9AA8B5" letter-spacing="1.5">LA LIBERTAD</text>')
    marker = ('<g transform="translate(520,186)">'
              '<circle r="36" fill="#E4702F" opacity=".10"/>'
              '<circle r="19" fill="#E4702F" opacity=".17"/>'
              '<path d="M0-24c-8.6 0-15 6.4-15 14.4C-15 0 0 15 0 15s15-15 15-24.6C15-17.6 8.6-24 0-24Zm0 20.4a5.4 5.4 0 1 1 0-10.8 5.4 5.4 0 0 1 0 10.8Z" fill="#0A2540"/>'
              '<circle cx="0" cy="-9" r="3.4" fill="#fff"/></g>')
    return ('<svg viewBox="0 0 800 450" preserveAspectRatio="xMidYMid slice" aria-hidden="true" '
            'style="position:absolute;inset:0;width:100%;height:100%">'
            '<rect width="800" height="450" fill="#F1F5F8"/>' + streets + blocks + labels + marker + '</svg>')


def contacto_body():
    svc_opts = "".join(f"<option>{n}</option>" for _, n, _, _ in SERVICES)
    return f"""
{pagehead([("home.html", "Inicio"), (None, "Contáctenos")],
          "Hablemos de su caso",
          "Escríbanos o llámenos. Respondemos en un día hábil con una propuesta de siguiente paso concreta.")}

<section class="section">
  <div class="wrap">
    <div style="display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr);gap:clamp(32px,4vw,64px);align-items:start">

      <div>
        <span class="eyebrow">Formulario</span>
        <h2 class="h2" style="margin:16px 0 10px">Cuéntenos qué necesita</h2>
        <p class="lead" style="margin-bottom:30px">Toda la información que comparta es confidencial y solo se usa para responder su solicitud.</p>
        <form class="form" data-demo novalidate>
          <div class="field"><label for="n">Nombre completo *</label><input id="n" name="nombre" placeholder="Ej. Ana Martínez" required></div>
          <div class="field"><label for="e">Empresa</label><input id="e" name="empresa" placeholder="Nombre de la sociedad"></div>
          <div class="field"><label for="c">Correo electrónico *</label><input id="c" type="email" name="correo" placeholder="nombre@empresa.com" required></div>
          <div class="field"><label for="t">Teléfono</label><input id="t" name="telefono" placeholder="(503) 0000 0000"></div>
          <div class="field field--full"><label for="s">Servicio de interés</label>
            <select id="s" name="servicio"><option value="">Seleccione una opción</option>{svc_opts}<option>Otro / no estoy seguro</option></select>
          </div>
          <div class="field field--full"><label for="m">Mensaje *</label><textarea id="m" name="mensaje" placeholder="Describa brevemente su necesidad, el período a revisar o el plazo que tiene."></textarea></div>
          <div class="field field--full">
            <label class="check"><input type="checkbox" required><span>He leído y acepto la <a href="#" data-pending style="color:var(--navy);text-decoration:underline">política de tratamiento de datos</a> de ACC.</span></label>
          </div>
          <div class="field field--full" style="flex-direction:row;align-items:center;gap:18px;flex-wrap:wrap">
            <button class="btn btn--primary" type="submit">Enviar mensaje {ico('arrow')}</button>
            <span class="muted" style="font-size:12.5px">Respuesta en un día hábil</span>
          </div>
          <div class="form__ok field--full">{ico('check-circle')}<div><b>Mensaje enviado.</b><br>Gracias por escribirnos. Un socio le responderá en un plazo máximo de un día hábil.</div></div>
        </form>
      </div>

      <div>
        <div class="info">
          <div class="info__item"><div class="info__ico">{ico('phone')}</div><div><b>Teléfono</b><a href="tel:+50325359800">(503) 2535 9800</a></div></div>
          <div class="info__item"><div class="info__ico">{ico('mail')}</div><div><b>Correo</b><a href="mailto:info@grupoacc.com.sv">info@grupoacc.com.sv</a></div></div>
          <div class="info__item" style="grid-column:1/-1"><div class="info__ico">{ico('pin')}</div><div><b>Dirección</b><p>Urb. Madreselva II, #57, Antiguo Cuscatlán, La Libertad, El Salvador.<br><span class="muted" style="font-size:13px">A tres cuadras de Avianca Santa Elena.</span></p></div></div>
          <div class="info__item"><div class="info__ico">{ico('clock')}</div><div><b>Horario</b><p>Lunes a viernes<br>8:00 – 17:00</p></div></div>
          <div class="info__item"><div class="info__ico">{ico('briefcase')}</div><div><b>Reuniones</b><p>Presenciales o virtuales, con cita previa.</p></div></div>
        </div>

        <div style="margin-top:14px">
          <a class="btn btn--navy" href="https://maps.google.com/?q=13.6646111,-89.2543333" target="_blank" rel="noopener" style="width:100%;justify-content:center">{ico('pin')} Ver en Google Maps {ico('arrow')}</a>
        </div>

        <div class="aside" style="margin-top:20px;background:var(--sky-100);border-color:var(--sky)">
          <h4 style="color:var(--navy-700)">¿Necesita una cotización?</h4>
          <p style="font-size:14px;line-height:1.65;color:var(--navy)">Indíquenos el tamaño de su operación (ingresos anuales aproximados y número de empleados) y el servicio requerido. Con eso podemos darle honorarios estimados sin una reunión previa.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section style="padding-bottom:clamp(56px,6vw,90px)">
  <div class="wrap">
    <div class="map">
      {map_svg()}
      <iframe title="Ubicación de ACC en Antiguo Cuscatlán" loading="lazy" src="https://www.google.com/maps?q=13.6646111,-89.2543333&z=16&output=embed"></iframe>
      <div class="map__card">
        <b>ACC Auditores y Consultores</b>
        <span>Urb. Madreselva II, #57, Antiguo Cuscatlán, La Libertad.</span>
      </div>
    </div>
  </div>
</section>

{cta_band("Prefiere que lo llamemos nosotros",
          "Deje su número en el formulario y coordinamos una llamada con el socio del área que necesita.")}
"""


# ══════════════════════════════════════════════════════════════════
#  9. INDEX — tablero de entrega
# ══════════════════════════════════════════════════════════════════
def index_page():
    screens = [
        ("home.html", "01", "Home", "Hero a dos columnas, franja de afiliaciones, 4 categorías de servicio, diferenciales, cifras, socios, cita y noticias.", "home"),
        ("nosotros.html", "02", "Quiénes somos", "Historia, línea de tiempo 2001–2018, misión/visión/valores, socios, personal y afiliaciones.", "nosotros"),
        ("agn.html", "03", "AGN International", "Página interna enlazada desde Quiénes somos: red global, 5 regiones y ventajas.", "agn"),
        ("servicios.html", "04", "Servicios (filtrable)", "Los 22 servicios con filtro por categoría, proceso de trabajo y FAQ de 8 preguntas.", "servicios"),
        ("servicio-auditoria-financiera.html", "05", "Detalle de servicio", "Plantilla de servicio: alcance, entregables, proceso y barra lateral de contacto.", "servicio-auditoria-financiera"),
        ("noticias.html", "06", "Noticias", "Buscador funcional, nota destacada, rejilla de publicaciones y paginación.", "noticias"),
        ("noticia.html", "07", "Nota / artículo", "Plantilla de artículo con autor, imagen, cuerpo, compartir y relacionadas.", "noticia"),
        ("contacto.html", "08", "Contáctenos", "Datos, formulario con validación, mapa de la oficina y aviso de confidencialidad.", "contacto"),
        ("sistema.html", "09", "Sistema de diseño", "Hoja de identidad aplicada: monograma, paleta, tipografía, recursos gráficos y biblioteca de componentes.", "sistema"),
    ]
    cards = ""
    for href, num, title, desc, thumb in screens:
        cards += f"""<a class="scard" href="{href}">
      <span class="scard__num">{num}</span>
      <div class="scard__ph"><img src="pantallas/thumbs/{thumb}.jpg" alt="Pantalla {title}" loading="lazy"></div>
      <div class="scard__body"><h3>{title}</h3><p>{desc}</p><span class="link-arrow">Abrir pantalla {ico('arrow')}</span></div>
    </a>"""

    return f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>ACC · Maqueta web — entrega de pantallas</title>
<link rel="stylesheet" href="assets/css/acc.css">
<style>
  body{{background:var(--paper-2)}}
  .board{{background:var(--navy);color:#fff;padding:clamp(48px,6vw,80px) 0;position:relative;overflow:hidden}}
  .board::before{{content:"";position:absolute;inset:0;opacity:.35;background-image:repeating-linear-gradient(90deg,rgba(255,255,255,.07) 0 1px,transparent 1px 90px);mask-image:linear-gradient(180deg,#000,transparent)}}
  .board .wrap{{position:relative;z-index:2}}
  .board h1{{font-size:clamp(34px,4.4vw,58px);letter-spacing:-.04em;line-height:1.02;margin-top:18px;max-width:20ch}}
  .board p{{color:rgba(255,255,255,.7);margin-top:18px;max-width:60ch;font-size:16px}}
  .board__meta{{display:flex;gap:28px;flex-wrap:wrap;margin-top:30px;font-family:var(--mono);font-size:10.5px;letter-spacing:.13em;text-transform:uppercase;color:rgba(255,255,255,.5)}}
  .board__meta b{{color:#fff}}
  .grid-screens{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:clamp(20px,2.6vw,32px);margin-top:clamp(36px,4vw,52px)}}
  .scard{{background:#fff;border:1px solid var(--line);display:flex;flex-direction:column;position:relative;transition:transform .4s var(--ease),box-shadow .4s}}
  .scard:hover{{transform:translateY(-4px);box-shadow:var(--shadow)}}
  .scard__num{{position:absolute;right:16px;top:14px;z-index:3;font-family:var(--mono);font-size:11px;letter-spacing:.12em;background:#fff;padding:4px 8px}}
  .scard__ph{{aspect-ratio:16/10;overflow:hidden;border-bottom:1px solid var(--line);background:var(--paper-3)}}
  .scard__ph img{{width:100%;height:100%;object-fit:cover;object-position:top center}}
  .scard__body{{padding:22px 24px 24px;display:flex;flex-direction:column;gap:9px;flex:1}}
  .scard__body h3{{font-size:19px;letter-spacing:-.02em}}
  .scard__body p{{font-size:13.5px;color:var(--gray);line-height:1.6}}
  .scard__body .link-arrow{{margin-top:auto;padding-top:10px;font-size:13px}}
  .legend{{margin-top:clamp(40px,5vw,64px);display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:24px;border-top:1px solid var(--line);padding-top:32px}}
  .legend div h4{{font-family:var(--mono);font-size:10.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--gray);margin-bottom:10px;font-weight:500}}
  .legend div p{{font-size:13.5px;color:var(--gray);line-height:1.6}}
  .swatches{{display:flex;gap:0;border:1px solid var(--line);margin-top:6px}}
  .swatches span{{flex:1;height:44px}}
  @media(max-width:900px){{.grid-screens{{grid-template-columns:1fr}}.legend{{grid-template-columns:1fr 1fr}}}}
</style>
</head>
<body>

<section class="board">
  <div class="wrap">
    <span class="eyebrow" style="color:var(--sky)">Maqueta de diseño · v1</span>
    <h1>ACC — Propuesta de sitio web</h1>
    <p>Nueve piezas: las ocho pantallas del sitio y la hoja de sistema que las unifica. Navegación funcional entre páginas, filtro de servicios, buscador de noticias y formulario operativo. Todas las pantallas son responsivas.</p>
    <div class="board__meta">
      <span><b>Cliente</b> ACC Auditores y Consultores</span>
      <span><b>Pantallas</b> 9</span>
      <span><b>Idioma</b> ES / EN</span>
      <span><b>Formato</b> Desktop 1440 px</span>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="grid-screens">{cards}</div>

    <div class="legend">
      <div>
        <h4>Paleta</h4>
        <div class="swatches">
          <span style="background:#0A2540" title="Azul marino"></span>
          <span style="background:#06182B" title="Marino profundo"></span>
          <span style="background:#8FC3E4" title="Celeste"></span>
          <span style="background:#E4702F" title="Anaranjado"></span>
          <span style="background:#6C7C8C" title="Gris"></span>
          <span style="background:#FFFFFF;border-left:1px solid #eee" title="Blanco"></span>
        </div>
        <p style="margin-top:12px">Marino como color principal, blanco de fondo, anaranjado y celeste como secundarios, gris para texto de apoyo.</p>
      </div>
      <div>
        <h4>Tipografía</h4>
        <p><b style="font-family:var(--sans);font-size:17px;color:var(--navy)">Archivo</b> — titulares y texto.<br><i style="font-family:var(--serif);font-size:17px;color:var(--navy)">Instrument Serif</i> — acentos editoriales.<br><span style="font-family:var(--mono);font-size:12px">JetBrains Mono</span> — datos y etiquetas.</p>
      </div>
      <div>
        <h4>Qué es funcional</h4>
        <p>Filtro de servicios por categoría, buscador de noticias, acordeón de FAQ, menú móvil, formulario con confirmación, selector ES/EN, suscripción al boletín.</p>
      </div>
      <div>
        <h4>Pendiente del cliente</h4>
        <p>Logotipo y fotografías reales, nombres de socios, textos de misión/visión definitivos, logotipos de AGN y Camarasal, y confirmación de la ubicación del FAQ.</p>
      </div>
    </div>
  </div>
</section>

</body>
</html>
"""


# ══════════════════════════════════════════════════════════════════
#  ESCRITURA
# ══════════════════════════════════════════════════════════════════
def main():
    pages = {
        "home.html": ("ACC · Auditores y Consultores en El Salvador", "home.html", home_body()),
        "nosotros.html": ("Quiénes somos · ACC", "nosotros.html", nosotros_body()),
        "agn.html": ("AGN International · ACC", "nosotros.html", agn_body()),
        "servicios.html": ("Servicios · ACC", "servicios.html", servicios_body()),
        "servicio-auditoria-financiera.html": ("Auditoría Financiera · ACC", "servicios.html", servicio_body()),
        "noticias.html": ("Noticias · ACC", "noticias.html", noticias_body()),
        "noticia.html": ("Reforma fiscal 2027 · ACC", "noticias.html", noticia_body()),
        "contacto.html": ("Contáctenos · ACC", "contacto.html", contacto_body()),
    }
    for fn, (title, active, body) in pages.items():
        (ROOT / fn).write_text(shell(title, active, body), encoding="utf-8")
        print("✓", fn)
    (ROOT / "index.html").write_text(index_page(), encoding="utf-8")
    print("✓ index.html")


if __name__ == "__main__":
    main()
