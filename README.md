# EcoAssist AI Pro – Sistema de Atención al Cliente con RAG

## Descripción
EcoAssist AI Pro es una propuesta de solución basada en IA generativa para optimizar la atención al cliente de **EcoMarket**, una empresa de e-commerce sostenible que enfrenta un alto volumen de consultas repetitivas y tiempos de respuesta promedio de 24 horas. El caso del taller indica que el 80% de las consultas son repetitivas y el 20% restante requiere atención humana por su complejidad o necesidad de empatía.

La solución propuesta utiliza una arquitectura **LLM + RAG (Retrieval Augmented Generation)** para responder con información contextualizada a partir de una base de conocimiento empresarial, manteniendo la escalabilidad, la trazabilidad y el control de la información.

---

## Objetivo
Diseñar una solución de IA generativa que acelere y mejore la calidad de las respuestas en el servicio de atención al cliente de EcoMarket, cumpliendo las tres fases del taller: selección y justificación del modelo, análisis crítico de fortalezas/limitaciones/riesgos éticos, e implementación de prompts efectivos. El taller exige precisamente esas tres fases y la entrega mediante un repositorio de GitHub.

---

## Arquitectura propuesta

```text
Cliente -> Interfaz (Chat/Web) -> Router de intención -> Retriever -> Base de conocimiento
                                                    -> LLM -> Respuesta final
                                                    -> Escalamiento humano si aplica
```

### Componentes
- **Interfaz conversacional**: recibe consultas por chat.
- **Router de intención**: clasifica si la consulta puede resolverse automáticamente o si debe escalarse.
- **Retriever**: busca información relevante en pedidos, políticas y catálogo.
- **Base de conocimiento**: pedidos, devoluciones, preguntas frecuentes y políticas.
- **LLM**: redacta respuestas naturales, claras y consistentes.
- **Escalamiento humano**: atiende quejas, reclamos sensibles y casos ambiguos.

---

## Estructura del repositorio

```text
ecoassist-rag-pro/
├── README.md
├── requirements.txt
├── fase1.md
├── fase2.md
├── fase3.md
├── .env.example
├── data/
│   ├── pedidos.json
│   ├── politicas.json
│   └── faq.json
├── src/
│   ├── rag_core.py
│   ├── prompts.py
│   ├── app_streamlit.py
│   └── demo_cli.py
└── notebooks/
    └── demo.ipynb
```

---

## Ejecución rápida

### 1) Crear entorno e instalar dependencias
```bash
pip install -r requirements.txt
```

### 2) Ejecutar demo por consola
```bash
python src/demo_cli.py
```

### 3) Ejecutar interfaz web
```bash
streamlit run src/app_streamlit.py
```

---

## Nota técnica
Esta versión incluye una simulación funcional de RAG local basada en recuperación por coincidencia semántica simple. También deja preparada una estructura para evolucionar a una versión conectada a un LLM real mediante API.

---

## Autor

Juan Manuel Hurtado Angulo  
Manuel Alberto González González  
William Alberto Reina García  

---

## Docente

David Miguel Ávila Crúz, MSc  

---

## Asignatura

Electiva V IA Generativa

Maestría en Inteligencia Artificial Aplicada – Universidad ICESI
