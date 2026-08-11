# Onboarding interactivo — UX Team Glovo

Contexto del proyecto para retomarlo en cualquier momento (por Miguel o por otra sesión de Claude).

## Objetivo

Sustituir el onboarding actual del equipo UX (un documento con checklists y puntos de contacto, "bastante triste") por una experiencia interactiva: una página HTML autocontenida por cada persona nueva, con checklist marcable, progreso visual, badges y una pequeña celebración al completarlo.

## Fuente de contenido

Google Doc **"Staff onboarding"** (ID `1tjoeC--oQ3EVSY-agE_l9uJ8m8buD4eCwS9UUTuB5qs`), accesible vía el conector de Google Drive. Es un doc **vivo** — se sigue editando — así que antes de generar el onboarding de alguien nuevo conviene releerlo con `read_file_content` (o `download_file_content` + decodificar base64 si `read_file_content` viene truncado; ya nos pasó una vez).

Tiene dos tabs:

- **"Onboarding to UX team"** — checklist cronológico (Week 1, Week 2 en el momento de escribir esto; puede que Weeks 3-4 vuelva a aparecer). Incluye: buddy de onboarding, tareas de acceso/herramientas, "key projects to shadow", y varios grupos de "gente a conocer" (UX Design, UX Research, PMs/EMs, resto del equipo UX).
- **"Staff Product Designer - Onboarding documentation"** — hub de recursos, bastante estable/genérico para cualquier persona del equipo UX: Organización, Procesos, Competency Framework, UX Leads, UX Research, Localization, Pintxo Design System, A11y, y el OKR de Delivery (con el "Stream 2 - Accelerate execution" que en el doc trae `Lead: [Nombre]` como placeholder — está pensado para rellenarse por persona).

**Importante:** al principio interpretamos mal cuál tab era cuál (los nombres internos "Tab 1"/"Tab 2" del export no coinciden con el orden visual). Guiarse siempre por el **título** de la tab, no por el número.

## Qué existe hoy

`Onboarding-Luli-EN.html` en la carpeta — el onboarding de Luli (Staff Product Designer, Stream 2). Es un archivo único, sin dependencias externas, pensado para abrirse directamente en el navegador.

Estructura de la página:

1. **Hero** amarillo con el logo de Glovo, saludo personalizado, y un banner fijo con el buddy de onboarding (Miguel Olivera) con link a su Slack.
2. **Barra de progreso + badges** — un icono por módulo, se colorea al completarlo.
3. **11 módulos** en acordeón, en este orden:
   - *Your first weeks*: Week 1 (accesos, herramientas, laptop, docs clave) y Week 2 (principios UX, UXR, Pintxo DS, proyectos a shadowear). Cada semana incluye "peopleGroups" — gente a conocer, sin checkbox, solo directorio.
   - *Resource hub*: los 9 módulos de referencia (Org, Procesos, Competency Framework, Leads, Research, Localization, Pintxo DS, A11y, OKR). El módulo de OKR tiene un "spotlight" especial con el Stream de Luli y sus 4 iniciativas.
4. **Celebración final** con confetti al completar el 100%.

No tiene botón de "editar perfil" — el nombre/rol de Luli está fijo en el código (se quitó a petición del usuario porque cada persona nueva tendrá su propio archivo, no un template compartido).

## Decisiones clave (por si hay que justificarlas o revertirlas)

- **Un HTML por persona**, no una plantilla genérica reutilizable. El contenido y los módulos pueden variar según el rol/equipo de cada nueva persona — se decide caso por caso, conversando con Miguel.
- **Solo inglés** a partir de cierto punto de la conversación (se generaron y luego se borraron versiones en español).
- **Enlaces a personas → Slack, no email.** Se usó el conector de Slack (`slack_search_users`) para resolver el ID real de cada persona mencionada y enlazar a `https://deliveryhero.enterprise.slack.com/team/<ID>` (perfil de esa persona). **Limitación conocida:** esto abre el *perfil*, no el DM directamente — falta un clic en "Message". Un enlace que abra el DM sin clics extra necesitaría el Team ID del workspace o el ID del canal de DM, y no hay herramienta disponible para obtenerlos sin enviar un mensaje real. Quedó pendiente probar `/app_redirect?channel=<ID>` como alternativa (no verificado, requiere navegador).
- **Tipografía real de Glovo Sans**, embebida como base64 (`@font-face`) directamente en el HTML — los archivos `.otf` están en `Onboarding/fonts/`. Si se regenera el archivo desde cero, hay que re-embeberlos (ver snippet de Python usado, buscar en el historial o pedírselo a Claude).
- **Paleta y componentes** siguiendo el skill `glovo-ui-reference` (Pintxo Design System): amarillo `#FFC042`, verde `#009E81`, tipografía Glovo Sans, radios de 24px/pill, etc.
- **Sin librerías externas ni CDN** — todo vanilla HTML/CSS/JS para que el archivo funcione offline, abierto directamente desde Finder.
- **Progreso guardado en `localStorage`** del navegador (no hay backend). Si Luli lo abre en otro navegador/ordenador, el progreso no se sincroniza.
- **El Resource Hub no cuenta como tareas.** Solo los módulos de *Your first weeks* (Week 1 y Week 2) tienen checkbox y suman para la barra de progreso, el badge shelf y la celebración final. Los 9 módulos del Resource Hub son de consulta libre: sin checkbox, sin contador, sin estado "done" — se marcan con `trackable:false` en el array `MODULES` del HTML (ver funciones `isTrackable`/`trackableModules` en el `<script>`). Al generar el onboarding de la próxima persona, mantener este mismo flag en los módulos de referencia.

## Cómo generar el onboarding de la siguiente persona

No hay un generador automático — es un proceso conversacional:

1. Miguel le cuenta a Claude quién es la persona nueva: nombre, rol, equipo, buddy, y qué le aplica (puede que algún módulo del resource hub no aplique, o que haga falta uno nuevo).
2. Claude relee el Google Doc por si cambió, ajusta el contenido de las semanas 1-2 y el resource hub según el rol, resuelve los Slacks de la gente mencionada, y genera un HTML nuevo con su propio nombre de archivo (`Onboarding-<Nombre>-EN.html`).
3. Se prueba con un test en Node usando `jsdom` (no hay Chrome/Puppeteer disponible en este sandbox — arquitectura arm64 sin build de Chrome compatible) antes de entregarlo.

## Limitaciones técnicas del entorno (por si se repiten)

- No hay navegador Chrome conectado (`Claude in Chrome` no disponible en esta sesión) — no se pueden hacer capturas de pantalla reales ni probar comportamiento real de Slack deep links.
- Puppeteer no funciona en el sandbox (descarga Chrome x64, el sandbox es arm64) — para QA funcional se usa `jsdom` simulando clics y verificando el DOM resultante.
- Los archivos en la carpeta `Onboarding` no se pueden borrar/renombrar sin pedir permiso (`allow_cowork_file_delete`), pero sí se pueden sobrescribir con el mismo nombre.
