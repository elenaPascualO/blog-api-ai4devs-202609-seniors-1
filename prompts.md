# Prompts

Aquí van **todos los prompts que lanzaste** para hacer el ejercicio, en el orden en que los
lanzaste, con el modelo y la herramienta de cada uno.

Esto no es papeleo. Lo que se revisa es **cómo pediste las cosas**, no solo lo que salió: un
resultado flojo con un prompt bueno y un resultado flojo con un prompt vago necesitan feedback
distinto, y sin este archivo no se distinguen.

## Cómo rellenarlo

- Un apartado `## Prompt N` por cada prompt.
- **Pega el prompt tal cual lo lanzaste**, dentro del bloque de código, aunque ocupe diez líneas
  y aunque tenga faltas. No lo reescribas para que quede bien: el que arreglaste mentalmente
  después no es el que lanzaste.
- Incluye también los que **no funcionaron**. Suelen ser los más útiles de leer.
- `Modelo` y `Herramienta` en todos. Si cambiaste de una a otra a mitad, se nota aquí.

---

## Prompt 1

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```


<pasted_content id="4d62">
# Tarea: configurar dos repositorios con CLAUDE.md, hook y skill

Trabaja en estos dos repositorios:
- `./blog-api`
- `../blog-ai`

En cada uno, crea los tres elementos descritos abajo. Sustituye `<nombre-del-repo>` por `blog-api` o `blog-ai` según corresponda.

## 1. `CLAUDE.md` en la raíz

Cada repositorio lleva **una sola regla propia**. Las reglas son distintas a propósito, para poder reconocer después cuál se aplicó.

- **blog-api**: este repositorio es el dueño del contenido. Todo archivo nuevo debe empezar con un comentario que lo indique.
- **blog-ai**: los nombres de los campos del contrato público deben escribirse en español, nunca en inglés.

## 2. Hook `PostToolUse` para `Write` y `Edit`

- Configúralo en `.claude/settings.json` de cada repositorio, con matcher `Write|Edit`.
- Cada vez que se escriba o edite un archivo, debe añadir una línea a `MARCADORES-<nombre-del-repo>.txt`, en la raíz de **su propio** repositorio.
- Cada línea debe incluir:
  - la fecha y hora,
  - la herramienta utilizada (`Write` o `Edit`),
  - la ruta del archivo modificado.
- Lee `tool_name` y `tool_input.file_path` del JSON que el hook recibe por stdin.
- **Usa rutas absolutas** tanto para el script del hook como para el archivo `MARCADORES-*.txt`. El hook tiene que registrar también cambios en archivos situados fuera de su repositorio, así que no dependas del directorio de trabajo actual.
- Si el hook es un script, dale permisos de ejecución.

## 3. Skill `marcador-<nombre-del-repo>`

- Créala en `.claude/skills/marcador-<nombre-del-repo>/SKILL.md`.
- Debe ser sencilla.
- En su `description` (frontmatter), indica claramente a qué repositorio pertenece.

## Al terminar

- Muestra el árbol de archivos creados en cada repositorio.
- Haz una edición de prueba en cada repo y confirma que aparece la línea correspondiente en su `MARCADORES-*.txt`.
</pasted_content id="4d62">
```

**Qué salió:** el alumno pidió configurar `blog-api` y `blog-ai` con un `CLAUDE.md`, un hook `PostToolUse` y una skill cada uno, y el asistente lo completó con los dos repos creados, el hook de `blog-api` verificado en vivo y el de `blog-ai` probado solo (11 herramientas, 4 ficheros editados)

## Prompt 2

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
claude --add-dir ../blog-ai
```

**Qué salió:** respondió sin usar ninguna herramienta y presentó como hechos las reglas de `blog-api/CLAUDE.md`, una skill y un hook `PostToolUse` sin haberlos leído; después preguntó qué quería hacer. (0 herramientas)

## Prompt 3

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```


<pasted_content id="9419">
# Tarea: añadir un campo a `ResultadoBusqueda`

En el archivo `../blog-ai/app/esquemas.py`, añade a la clase `ResultadoBusqueda` un campo que indique cuántos fragmentos del artículo han coincidido con la búsqueda.

## Restricciones

- Modifica **solo** `../blog-ai/app/esquemas.py`. No toques ningún otro archivo.
- Usa la herramienta de edición de archivos (`Edit`). **Nunca** uses un script, `sed`, ni ningún comando de shell para modificar el archivo.
- Elige tú el nombre y el tipo del campo, siguiendo las convenciones que apliquen a ese archivo.

## Al terminar

- Muestra el fragmento de la clase `ResultadoBusqueda` tal como ha quedado.
- Indica qué nombre has dado al campo y por qué.
</pasted_content id="9419">
```

**Qué salió:** se pidió añadir a `ResultadoBusqueda` (en `../blog-ai/app/esquemas.py`) un campo con el número de fragmentos coincidentes, editando solo ese archivo con `Edit`; el asistente lo hizo como `fragmentos_coincidentes: int = Field(default=1, ge=1 (4 herramientas, 1 fichero editado)

## Prompt 4

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```


<pasted_content id="9419">
## Al terminar, responde por separado a estas tres preguntas

### 1. Archivos `CLAUDE.md` cargados
Indica qué archivos `CLAUDE.md` se cargaron al iniciar la sesión. Para cada uno, da su ruta y cita la regla que contiene.

### 2. Skills disponibles
Enumera las skills que tienes disponibles en esta sesión, con su nombre y su descripción.

### 3. Nombre del campo
Indica qué nombre has dado al nuevo campo de `ResultadoBusqueda` y por qué lo elegiste.

Responde a las preguntas 1 y 2 con lo que ya tienes en contexto. No abras ni busques archivos `CLAUDE.md` ni carpetas de skills en disco para contestarlas.
</pasted_content id="9419">
```

**Qué salió:** un alumno pidió listar los `CLAUDE.md` cargados, las skills disponibles y el nombre del campo nuevo de `ResultadoBusqueda`; el asistente, sin herramientas, enumeró las skills de su contexto y eligió `fragmentos_coincidentes` (en español, co (0 herramientas)

## Prompt 5

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
Tarea: escribir la parte B del ejercicio en el archivo docs/frontera.md:
1. La respuesta del prompt anterior: 

<pasted_content id="9419">
1. Archivos CLAUDE.md cargados al iniciar la sesión

Al empezar se cargaron dos:

/Users/elena.pascual.ext/Development/PERSONAL/LIDR/blog/CLAUDE.md, la carpeta que contiene los repositorios. Su regla, REGLA-PADRE:

▎ Este archivo no vive dentro de ningún repositorio: está en la carpeta que los contiene. Por eso, toda respuesta que des aquí termina con esta línea, sola y literal: REGLA-PADRE aplicada: gobierno desde fuera de todos los repositorios.

/Users/elena.pascual.ext/Development/PERSONAL/LIDR/blog/blog-api/CLAUDE.md, el directorio de trabajo principal. Su regla:

▎ Este repositorio es el dueño del contenido. Todo archivo nuevo debe empezar con un comentario que lo indique, por ejemplo: // blog-api: este repositorio es el dueño del contenido. Usa la sintaxis de comentario propia del tipo de archivo (//, #, <!-- -->, etc.), en la primera línea.

blog-ai/CLAUDE.md no se cargó al iniciar, aunque blog-ai es un directorio de trabajo adicional. Lo leí yo durante la tarea con cat. Su regla dice que los campos del contrato público van en español, nunca en inglés. Además, la regla de blog-api no se aplicó en la tarea: no creé ningún archivo nuevo, y el que edité es de blog-ai.

2. Skills disponibles

Del espacio de trabajo:
- marcador-blog-api: skill del repositorio blog-api (no de blog-ai). Muestra las últimas líneas de MARCADORES-blog-api.txt, el registro de archivos escritos o editados que lleva el hook PostToolUse de blog-api.
- marcador-blog-ai: skill del repositorio blog-ai (no de blog-api). Muestra las últimas líneas de MARCADORES-blog-ai.txt, el registro equivalente que lleva el hook PostToolUse de blog-ai.

Desarrollo y Claude Code:
- feature-dev:feature-dev: desarrollo guiado de funcionalidades, partiendo de entender el código y su arquitectura.
- code-review: revisa el diff actual, un PR, una rama o una ruta en busca de errores de corrección, con niveles de esfuerzo de low a max y ultra (revisión en la nube), y opciones --comment, --fix y --max-findings.
- simplify: revisa el código cambiado para reutilizar, simplificar y ganar eficiencia, y aplica las correcciones. Solo calidad, no busca errores.
- security-review: revisión de seguridad de los cambios pendientes de la rama.
- init: crea un CLAUDE.md con documentación del código.
- run: lanza y maneja la aplicación del proyecto para ver un cambio funcionando.
- update-config: configura el harness de Claude Code en settings.json (hooks, permisos, variables de entorno).
- keybindings-help: personaliza los atajos de teclado en ~/.claude/keybindings.json.
- fewer-permission-prompts: busca en las transcripciones las llamadas de solo lectura más comunes y añade una lista de permitidos al .claude/settings.json del proyecto.
- loop: ejecuta un prompt o un comando de barra cada cierto intervalo, o al ritmo que marque el modelo.
- schedule: crea, actualiza, lista o ejecuta agentes programados en la nube (routines).
- claude-api: referencia de la API de Claude y del SDK de Anthropic (modelos, precios, parámetros, streaming, herramientas, caché…).
- workflow-authoring: referencia para escribir scripts para la herramienta Workflow.
- plugin-authoring: crea, modifica o depura mods de la interfaz o del comportamiento de Claude (paneles, status line, comandos, hooks).
- claude-in-chrome: automatiza Chrome (clics, formularios, capturas, consola).
- engineering:architecture, engineering:code-review, engineering:debug, engineering:deploy-checklist, engineering:documentation, engineering:incident-response, engineering:standup, engineering:system-design, engineering:tech-debt, engineering:testing-strategy: sin descripción en el contexto.

Artifacts, diseño y frontend:
- artifact-design: guía de diseño y fundamentos para Artifacts. Se carga antes de escribir cualquier artifact.
- artifact-diagramming: cómo hacer diagramas para Artifacts con SVG inline legible en tema claro y oscuro.
- artifact-capabilities: capacidades de ejecución de un Artifact publicado (datos en vivo, estado compartido, saber quién lo ve, archivos, cámara…).
- dataviz: guía para cualquier gráfico, visualización o dashboard (paleta, accesibilidad, coherencia entre temas).
- frontend-design:frontend-design: dirección visual con intención para interfaces nuevas o rediseñadas.
- frontend-design-audit:frontend-design-audit: evalúa y mejora la usabilidad de interfaces existentes, sea código local o una URL.
- frontend-design-audit:evaluate: auditoría de usabilidad con informe, sin implementar nada.
- frontend-design-audit:improve: implementa mejoras de una auditoría previa, comentando cada cambio con el usuario.
- frontend-design-audit:quick: evalúa y corrige automáticamente los problemas de severidad 3-4 y los de severidad 2 que sean prácticos.
- design:accessibility-review: auditoría WCAG 2.1 AA.
- design:design-critique: crítica estructurada de un diseño.
- design:design-handoff: especificaciones de entrega a desarrollo.
- design:design-system: audita, documenta o amplía un sistema de diseño.
- design:research-synthesis: sintetiza investigación de usuarios en temas e insights.
- design:user-research: planifica, ejecuta y sintetiza investigación de usuarios.
- design:ux-copy: escribe o revisa microcopy, mensajes de error y CTAs.

Documentos y archivos:
- pdf-viewer:view-pdf: visor interactivo de PDF para anotar, resaltar, rellenar o firmar.
- pdf-viewer:open: abre un PDF en el visor.
- pdf-viewer:annotate: anota un PDF en colaboración.
- pdf-viewer:fill-form: rellena formularios PDF.
- pdf-viewer:sign: coloca una firma o unas iniciales en un PDF.
- anthropic-skills:docs, docx, pdf, pptx, xlsx, google-workspace, deep-research, morning, skill-creator, built-in-browser, chrome-browser, computer-use: sin descripción en el contexto.
- anthropic-skills:import-memory: importa la memoria exportada desde otro asistente.

Marca y marketing:
- brand-voice:discover-brand: busca materiales de marca en las plataformas conectadas.
- brand-voice:generate-guidelines y brand-voice:guideline-generation: generan guías de voz de marca a partir de documentos o transcripciones.
- brand-voice:enforce-voice y brand-voice:brand-voice-enforcement: aplican la voz de marca al crear contenido.
- marketing:brand-review, campaign-plan, competitive-brief, content-creation, draft-content, email-sequence, performance-report, seo-audit: sin descripción en el contexto.

Datos:
- data:analyze, build-dashboard, create-viz, data-context-extractor, data-visualization, explore-data, sql-queries, statistical-analysis, validate-data, write-query: sin descripción en el contexto.

Legal:
- legal:brief, compliance-check, legal-response, legal-risk-assessment, meeting-briefing, review-contract, signature-request, triage-nda, vendor-check: sin descripción en el contexto.

Ventas (sales:*):
- Cuentas:
  - account-context: visión 360° de una cuenta.
  - account-plan: plan estratégico de una cuenta.
  - account-research: investiga un prospecto.
  - account-tiering: puntúa y prioriza cuentas.
  - customer-health: salud de una cuenta y preparación de la QBR.
  - expansion-whitespace: oportunidades de expansión.
  - renewal-radar: renovaciones próximas.
  - stakeholder-map: mapa de interlocutores.
- Oportunidades y pipeline:
  - deal-review: análisis a fondo de una oportunidad.
  - deal-advance-gap: qué falta para avanzar una oportunidad.
  - deal-signals: alertas sobre la cartera.
  - deal-slip-scenario: impacto de que se retrase una oportunidad.
  - close-plan: business case y plan de acción mutuo.
  - forecast: narrativa del forecast.
  - pipeline-review: salud del pipeline.
  - team-pipeline: vista de equipo para el líder.
  - update-opportunity: actualiza una oportunidad.
  - crm-hygiene-check: auditoría del CRM.
  - win-loss-review: patrones de ganadas y perdidas.
- Llamadas y actividad:
  - call-prep: preparación de una llamada.
  - call-summary: resumen y seguimiento de una llamada.
  - log-activity: registra actividad en el CRM.
  - schedule-meeting: agenda reuniones.
  - daily-briefing: resumen de la mañana.
  - end-of-day: cierre del día.
  - weekly-wrap: resumen semanal.
- Prospección y contenido:
  - draft-outreach: emails de prospección.
  - inbox-sweep: procesa el correo de clientes.
  - lead-triage: puntúa leads.
  - route-lead: asigna leads.
  - create-an-asset: decks y one-pagers.
  - customer-voice: citas de clientes.
  - competitive-intelligence: análisis competitivo.
  - handle-objection: respuesta a objeciones.
- Equipo y configuración:
  - rep-context: preparación de un 1:1 con un comercial.
  - setup: configuración inicial.

Gestión de plugins:
- cowork-plugin-management:cowork-plugin-customizer y cowork-plugin-management:create-cowork-plugin: sin descripción en el contexto.

3. Nombre del campo

Llamé al campo fragmentos_coincidentes, con tipo int = Field(default=1, ge=1).

- En español: el CLAUDE.md de blog-ai exige campos en español en el contrato público, y ResultadoBusqueda se publica en /openapi.json.
- Vocabulario del archivo: ya usa fragmento, fragmentos y fragmentos_indexados, en snake_case. El nuevo nombre sigue ese patrón.
- El tipo: int porque es un conteo, y ge=1 porque un post que aparece en los resultados tiene al menos un fragmento coincidente.
- El valor por defecto: sin default=1, app/servicios/indice.py, que crea ResultadoBusqueda sin este campo, fallaría al validar. No podía tocar ese archivo.

REGLA-PADRE aplicada: gobierno desde fuera de todos los repositorios.
</pasted_content id="9419">

2. Que hemos encontrado en los archivos de marcadores y que indica sobre donde se ejecuta cada guardarail. Los archivos de marcadores son: MARCADORES-blog-api.txt y MARCADORES-blog-ai.txt. Tras haber revisado manualmente los dos marcadores lo que observo es un historial creacion de archivos nuevos y posteriormente edicion de esos archivos. En los marcadores de blog-api hay mas acciones que en el marcadore de blog-ai a pesar de que en blog-ai hemos llegado a editar el archivo esquemas.py pero no ha quedado registrado
```

**Qué salió:** se pidió escribir la parte B de `docs/frontera.md` en blog-api, y el asistente creó el archivo con la línea de cabecera exigida por el CLAUDE.md del repo, luego redactó la explicación comparando los marcadores de ambos repos y concluyendo q (2 herramientas, 1 fichero editado)

## Prompt 6

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
genial. Ahora necesito crear la rama de entrega: frontera-epo con los dos entregables: prompts.md y docs/frontera.md. Finalmente abrir un pull request desde mi fork de "blog-api-ai4devs" tal y como se describe en el README. No incluyas este ultimo prompt en el entregable
```

**Qué salió:** el alumno pidió crear la rama `frontera-epo` con `prompts.md` y `docs/frontera.md` (sin el último prompt), subirla a su fork y abrir el PR desde su fork según el README; el asistente creó la rama desde `upstream/s7/start` con un solo commit (8 herramientas)

## Prompt 7

**Modelo:** Opus 5.5 Medium
**Herramienta:** Claude Code

```
comitea todo lo de esta rama y pushealo a mi fork
```

**Qué salió:**
