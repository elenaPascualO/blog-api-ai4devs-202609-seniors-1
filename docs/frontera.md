<!-- blog-api: este repositorio es el dueño del contenido. -->

# Frontera entre repositorios

## Parte B

### 1. Respuesta de Claude a las tres preguntas

La sesión se lanzó desde `blog-api`, con `blog-ai` como directorio de trabajo adicional. La tarea fue añadir un campo a `ResultadoBusqueda` en `../blog-ai/app/esquemas.py`. Al terminar, Claude respondió esto:

> #### 1. Archivos `CLAUDE.md` cargados al iniciar la sesión
>
> Al empezar se cargaron dos:
>
> **`/Users/elena.pascual.ext/Development/PERSONAL/LIDR/blog/CLAUDE.md`**, la carpeta que contiene los repositorios. Su regla, REGLA-PADRE:
>
> > Este archivo no vive dentro de ningún repositorio: está en la carpeta que los contiene. Por eso, **toda respuesta que des aquí termina con esta línea, sola y literal**: `REGLA-PADRE aplicada: gobierno desde fuera de todos los repositorios.`
>
> **`/Users/elena.pascual.ext/Development/PERSONAL/LIDR/blog/blog-api/CLAUDE.md`**, el directorio de trabajo principal. Su regla:
>
> > Este repositorio es el dueño del contenido. Todo archivo nuevo debe empezar con un comentario que lo indique, por ejemplo: `// blog-api: este repositorio es el dueño del contenido.` Usa la sintaxis de comentario propia del tipo de archivo (`//`, `#`, `<!-- -->`, etc.), en la primera línea.
>
> `blog-ai/CLAUDE.md` **no** se cargó al iniciar, aunque `blog-ai` es un directorio de trabajo adicional. Lo leí yo durante la tarea con `cat`. Su regla dice que los campos del contrato público van en español, nunca en inglés. Además, la regla de blog-api no se aplicó en la tarea: no creé ningún archivo nuevo, y el que edité es de blog-ai.
>
> #### 2. Skills disponibles
>
> **Del espacio de trabajo:**
> - `marcador-blog-api`: skill del repositorio blog-api (no de blog-ai). Muestra las últimas líneas de `MARCADORES-blog-api.txt`, el registro de archivos escritos o editados que lleva el hook PostToolUse de blog-api.
> - `marcador-blog-ai`: skill del repositorio blog-ai (no de blog-api). Muestra las últimas líneas de `MARCADORES-blog-ai.txt`, el registro equivalente que lleva el hook PostToolUse de blog-ai.
>
> **Desarrollo y Claude Code:**
> - `feature-dev:feature-dev`: desarrollo guiado de funcionalidades, partiendo de entender el código y su arquitectura.
> - `code-review`: revisa el diff actual, un PR, una rama o una ruta en busca de errores de corrección, con niveles de esfuerzo de low a max y ultra (revisión en la nube), y opciones `--comment`, `--fix` y `--max-findings`.
> - `simplify`: revisa el código cambiado para reutilizar, simplificar y ganar eficiencia, y aplica las correcciones. Solo calidad, no busca errores.
> - `security-review`: revisión de seguridad de los cambios pendientes de la rama.
> - `init`: crea un `CLAUDE.md` con documentación del código.
> - `run`: lanza y maneja la aplicación del proyecto para ver un cambio funcionando.
> - `update-config`: configura el harness de Claude Code en `settings.json` (hooks, permisos, variables de entorno).
> - `keybindings-help`: personaliza los atajos de teclado en `~/.claude/keybindings.json`.
> - `fewer-permission-prompts`: busca en las transcripciones las llamadas de solo lectura más comunes y añade una lista de permitidos al `.claude/settings.json` del proyecto.
> - `loop`: ejecuta un prompt o un comando de barra cada cierto intervalo, o al ritmo que marque el modelo.
> - `schedule`: crea, actualiza, lista o ejecuta agentes programados en la nube (routines).
> - `claude-api`: referencia de la API de Claude y del SDK de Anthropic (modelos, precios, parámetros, streaming, herramientas, caché…).
> - `workflow-authoring`: referencia para escribir scripts para la herramienta Workflow.
> - `plugin-authoring`: crea, modifica o depura mods de la interfaz o del comportamiento de Claude (paneles, status line, comandos, hooks).
> - `claude-in-chrome`: automatiza Chrome (clics, formularios, capturas, consola).
> - `engineering:architecture`, `engineering:code-review`, `engineering:debug`, `engineering:deploy-checklist`, `engineering:documentation`, `engineering:incident-response`, `engineering:standup`, `engineering:system-design`, `engineering:tech-debt`, `engineering:testing-strategy`: sin descripción en el contexto.
>
> **Artifacts, diseño y frontend:**
> - `artifact-design`: guía de diseño y fundamentos para Artifacts. Se carga antes de escribir cualquier artifact.
> - `artifact-diagramming`: cómo hacer diagramas para Artifacts con SVG inline legible en tema claro y oscuro.
> - `artifact-capabilities`: capacidades de ejecución de un Artifact publicado (datos en vivo, estado compartido, saber quién lo ve, archivos, cámara…).
> - `dataviz`: guía para cualquier gráfico, visualización o dashboard (paleta, accesibilidad, coherencia entre temas).
> - `frontend-design:frontend-design`: dirección visual con intención para interfaces nuevas o rediseñadas.
> - `frontend-design-audit:frontend-design-audit`: evalúa y mejora la usabilidad de interfaces existentes, sea código local o una URL.
> - `frontend-design-audit:evaluate`: auditoría de usabilidad con informe, sin implementar nada.
> - `frontend-design-audit:improve`: implementa mejoras de una auditoría previa, comentando cada cambio con el usuario.
> - `frontend-design-audit:quick`: evalúa y corrige automáticamente los problemas de severidad 3-4 y los de severidad 2 que sean prácticos.
> - `design:accessibility-review`: auditoría WCAG 2.1 AA.
> - `design:design-critique`: crítica estructurada de un diseño.
> - `design:design-handoff`: especificaciones de entrega a desarrollo.
> - `design:design-system`: audita, documenta o amplía un sistema de diseño.
> - `design:research-synthesis`: sintetiza investigación de usuarios en temas e insights.
> - `design:user-research`: planifica, ejecuta y sintetiza investigación de usuarios.
> - `design:ux-copy`: escribe o revisa microcopy, mensajes de error y CTAs.
>
> **Documentos y archivos:**
> - `pdf-viewer:view-pdf`: visor interactivo de PDF para anotar, resaltar, rellenar o firmar.
> - `pdf-viewer:open`: abre un PDF en el visor.
> - `pdf-viewer:annotate`: anota un PDF en colaboración.
> - `pdf-viewer:fill-form`: rellena formularios PDF.
> - `pdf-viewer:sign`: coloca una firma o unas iniciales en un PDF.
> - `anthropic-skills:docs`, `docx`, `pdf`, `pptx`, `xlsx`, `google-workspace`, `deep-research`, `morning`, `skill-creator`, `built-in-browser`, `chrome-browser`, `computer-use`: sin descripción en el contexto.
> - `anthropic-skills:import-memory`: importa la memoria exportada desde otro asistente.
>
> **Marca y marketing:**
> - `brand-voice:discover-brand`: busca materiales de marca en las plataformas conectadas.
> - `brand-voice:generate-guidelines` y `brand-voice:guideline-generation`: generan guías de voz de marca a partir de documentos o transcripciones.
> - `brand-voice:enforce-voice` y `brand-voice:brand-voice-enforcement`: aplican la voz de marca al crear contenido.
> - `marketing:brand-review`, `campaign-plan`, `competitive-brief`, `content-creation`, `draft-content`, `email-sequence`, `performance-report`, `seo-audit`: sin descripción en el contexto.
>
> **Datos:**
> - `data:analyze`, `build-dashboard`, `create-viz`, `data-context-extractor`, `data-visualization`, `explore-data`, `sql-queries`, `statistical-analysis`, `validate-data`, `write-query`: sin descripción en el contexto.
>
> **Legal:**
> - `legal:brief`, `compliance-check`, `legal-response`, `legal-risk-assessment`, `meeting-briefing`, `review-contract`, `signature-request`, `triage-nda`, `vendor-check`: sin descripción en el contexto.
>
> **Ventas (`sales:*`):**
> - **Cuentas:**
>   - `account-context`: visión 360° de una cuenta.
>   - `account-plan`: plan estratégico de una cuenta.
>   - `account-research`: investiga un prospecto.
>   - `account-tiering`: puntúa y prioriza cuentas.
>   - `customer-health`: salud de una cuenta y preparación de la QBR.
>   - `expansion-whitespace`: oportunidades de expansión.
>   - `renewal-radar`: renovaciones próximas.
>   - `stakeholder-map`: mapa de interlocutores.
> - **Oportunidades y pipeline:**
>   - `deal-review`: análisis a fondo de una oportunidad.
>   - `deal-advance-gap`: qué falta para avanzar una oportunidad.
>   - `deal-signals`: alertas sobre la cartera.
>   - `deal-slip-scenario`: impacto de que se retrase una oportunidad.
>   - `close-plan`: business case y plan de acción mutuo.
>   - `forecast`: narrativa del forecast.
>   - `pipeline-review`: salud del pipeline.
>   - `team-pipeline`: vista de equipo para el líder.
>   - `update-opportunity`: actualiza una oportunidad.
>   - `crm-hygiene-check`: auditoría del CRM.
>   - `win-loss-review`: patrones de ganadas y perdidas.
> - **Llamadas y actividad:**
>   - `call-prep`: preparación de una llamada.
>   - `call-summary`: resumen y seguimiento de una llamada.
>   - `log-activity`: registra actividad en el CRM.
>   - `schedule-meeting`: agenda reuniones.
>   - `daily-briefing`: resumen de la mañana.
>   - `end-of-day`: cierre del día.
>   - `weekly-wrap`: resumen semanal.
> - **Prospección y contenido:**
>   - `draft-outreach`: emails de prospección.
>   - `inbox-sweep`: procesa el correo de clientes.
>   - `lead-triage`: puntúa leads.
>   - `route-lead`: asigna leads.
>   - `create-an-asset`: decks y one-pagers.
>   - `customer-voice`: citas de clientes.
>   - `competitive-intelligence`: análisis competitivo.
>   - `handle-objection`: respuesta a objeciones.
> - **Equipo y configuración:**
>   - `rep-context`: preparación de un 1:1 con un comercial.
>   - `setup`: configuración inicial.
>
> **Gestión de plugins:**
> - `cowork-plugin-management:cowork-plugin-customizer` y `cowork-plugin-management:create-cowork-plugin`: sin descripción en el contexto.
>
> #### 3. Nombre del campo
>
> Llamé al campo **`fragmentos_coincidentes`**, con tipo `int = Field(default=1, ge=1)`.
>
> - **En español:** el `CLAUDE.md` de blog-ai exige campos en español en el contrato público, y `ResultadoBusqueda` se publica en `/openapi.json`.
> - **Vocabulario del archivo:** ya usa `fragmento`, `fragmentos` y `fragmentos_indexados`, en `snake_case`. El nuevo nombre sigue ese patrón.
> - **El tipo:** `int` porque es un conteo, y `ge=1` porque un post que aparece en los resultados tiene al menos un fragmento coincidente.
> - **El valor por defecto:** sin `default=1`, `app/servicios/indice.py`, que crea `ResultadoBusqueda` sin este campo, fallaría al validar. No podía tocar ese archivo.
>
> REGLA-PADRE aplicada: gobierno desde fuera de todos los repositorios.

### 2. Qué muestran los archivos de marcadores

Cada repositorio tiene su propio hook `PostToolUse` con matcher `Write|Edit`, declarado en su `.claude/settings.json`:

- `blog-api/.claude/hooks/marcador.py` escribe en `blog-api/MARCADORES-blog-api.txt`.
- `blog-ai/.claude/hooks/marcador.py` escribe en `blog-ai/MARCADORES-blog-ai.txt`.

Los dos usan rutas absolutas, así que registran cualquier archivo que se escriba, esté dentro o fuera de su repositorio.

#### Lo que hay en cada archivo

En los dos marcadores aparece un historial de creación de archivos nuevos (`Write`) y, después, de edición de esos mismos archivos (`Edit`).

`MARCADORES-blog-api.txt`:

```text
2026-10-28T09:56:17	Write	.../blog-api/CLAUDE.md
2026-10-28T09:56:18	Write	.../blog-ai/CLAUDE.md
2026-10-28T09:56:18	Write	.../blog-api/.claude/skills/marcador-blog-api/SKILL.md
2026-10-28T09:56:18	Write	.../blog-ai/.claude/skills/marcador-blog-ai/SKILL.md
2026-10-28T09:56:23	Edit	.../blog-api/CLAUDE.md
2026-10-28T09:56:24	Edit	.../blog-ai/CLAUDE.md
2026-10-28T10:06:28	Edit	.../blog-ai/app/esquemas.py
```

`MARCADORES-blog-ai.txt`:

```text
2026-10-28T09:56:37	Edit	.../blog-ai/CLAUDE.md
```

El marcador de blog-api tiene muchas más acciones que el de blog-ai, y entre ellas hay archivos que viven en blog-ai. La más reveladora es la edición de `blog-ai/app/esquemas.py` (10:06:28), hecha en la tarea de la parte A: es un archivo de blog-ai, pero **no quedó registrada en `MARCADORES-blog-ai.txt`**. Solo aparece en el de blog-api.

#### Qué indica sobre dónde se ejecuta cada guardarraíl

Lo que decide qué guardarraíles actúan es **desde dónde se lanza la sesión**, no dónde vive el archivo que se toca.

- **Hooks:** solo se ejecutan los del `.claude/settings.json` del proyecto desde el que se arranca la sesión. Esta sesión se arrancó en `blog-api`, así que se ejecutó el hook de blog-api, incluso al editar un archivo de blog-ai. El hook de blog-ai no se ejecutó, aunque `blog-ai` estaba añadido como directorio de trabajo adicional. La única línea de `MARCADORES-blog-ai.txt` (09:56:37) corresponde a una sesión lanzada desde dentro de `blog-ai`.
- **`CLAUDE.md`:** pasa lo mismo. Se cargaron el del proyecto de arranque (`blog-api/CLAUDE.md`) y el de la carpeta padre (`blog/CLAUDE.md`), porque Claude Code recorre los directorios hacia arriba desde donde se lanza. El de `blog-ai` no se cargó, y su regla de nombres en español solo se respetó porque Claude abrió el archivo a mano. El guardarraíl del repositorio dueño del archivo no protegió ese archivo.
- **Skills:** son la excepción. `marcador-blog-ai` sí apareció entre las skills disponibles, así que las skills de un directorio de trabajo adicional se descubren aunque sus hooks y su `CLAUDE.md` no se apliquen.

En resumen, un guardarraíl declarado en un repositorio no protege sus archivos cuando se editan desde una sesión lanzada en otro. Si una regla tiene que cumplirse siempre, hay que declararla en el proyecto desde el que se trabaja, en la carpeta padre común, o en un control que no dependa de la sesión (CI, hooks de git).
