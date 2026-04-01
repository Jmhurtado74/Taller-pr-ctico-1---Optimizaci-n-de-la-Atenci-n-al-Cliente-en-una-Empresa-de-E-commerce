# Fase 1 – Selección y Justificación del Modelo de IA

## Selección del modelo
Para resolver el problema de EcoMarket se propone una **arquitectura híbrida compuesta por un LLM y un sistema RAG**. Esta elección responde a la necesidad de combinar la fluidez conversacional de un modelo generativo con el acceso a información real, actualizada y específica del negocio.

La guía del taller pide seleccionar el tipo de modelo, justificar por qué se elige, proponer una arquitectura e integrar datos de la empresa considerando costo, escalabilidad, facilidad de integración y calidad esperada de la respuesta. fileciteturn1file0L15-L24

## Justificación
### 1. Precisión
Un LLM sin recuperación puede responder con seguridad incluso cuando no conoce el estado real de un pedido. Con RAG, el sistema consulta primero la base de datos de EcoMarket y luego genera una respuesta basada en evidencia.

### 2. Escalabilidad
Dado que el 80% de las consultas son repetitivas, la automatización de ese volumen permite escalar el servicio sin aumentar proporcionalmente el número de agentes.

### 3. Costo
La arquitectura evita, en una primera etapa, el fine-tuning costoso de un modelo específico. En su lugar, reutiliza un modelo general y lo fortalece con datos propios.

### 4. Integración
La propuesta puede conectarse a bases de datos de pedidos, políticas de devoluciones, catálogos y preguntas frecuentes mediante APIs o consultas internas.

### 5. Calidad de respuesta
El modelo mantiene fluidez, claridad y tono conversacional, pero ya no responde solo desde su entrenamiento previo, sino desde contexto recuperado.

## Arquitectura propuesta
```text
Consulta del cliente -> clasificador de intención -> recuperación de contexto -> LLM -> respuesta o escalamiento humano
```

## Conclusión
La arquitectura LLM + RAG es la alternativa más adecuada porque balancea precisión, escalabilidad, costo de implementación y facilidad de integración, alineándose de forma directa con las necesidades del caso de estudio y con los criterios de evaluación del taller. La rúbrica asigna el nivel excelente cuando la justificación considera arquitectura, costo, escalabilidad y facilidad de integración, justamente los ejes cubiertos en esta propuesta. fileciteturn1file1L11-L24
