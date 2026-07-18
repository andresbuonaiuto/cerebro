La mayoría de herramientas de "chatea con tus PDFs" tienen un problema que casi nadie menciona: no acumulan nada.

Preguntas algo hoy, la IA busca en tus archivos, responde. Preguntas algo parecido mañana, vuelve a buscar desde cero. Nada se construye. Nada se recuerda.

Llevaba tiempo dándole vueltas a esto porque quería algo distinto: bases de conocimiento concretas que pudiera citar de verdad al tomar decisiones. Un cerebro de libros de negocio para validar ideas. Otro de gestión y contabilidad para decisiones críticas.

Así que construí cerebro: un kit open source que convierte tus libros y PDFs en un wiki en Markdown que la IA escribe y mantiene por ti.

La diferencia con RAG es esta: la IA lee cada fuente una vez y la integra en un wiki interconectado, no vuelve a redescubrirla en cada pregunta. Los enlaces cruzados ya están ahí. Las contradicciones entre fuentes quedan marcadas, no escondidas. Y si le preguntas algo que el cerebro no cubre, te lo dice en vez de inventar una respuesta con confianza.

Funciona con Claude (skill instalable), con cualquier agente que lea AGENTS.md (Codex, Cursor, Gemini CLI), y hasta con ChatGPT para consultas.

Es la implementación de un patrón que describió Andrej Karpathy, el "LLM Wiki". Yo lo convertí en algo que se instala y se usa: documento normativo, skill lista, plantillas, y un cerebro de ejemplo completo para verlo funcionando sin instalar nada.

Repo, gratis, MIT: github.com/andresbuonaiuto/cerebro

Si trabajas con IA y documentos todos los días, prueba la diferencia entre buscar y recordar.
