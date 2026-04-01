# Taller práctico #1 - Optimización de la Atención al Cliente en una Empresa de E-commerce
# EcoAssist AI – Sistema de Atención al Cliente con RAG

## Descripción del proyecto

EcoAssist AI es una solución basada en Inteligencia Artificial Generativa que utiliza una arquitectura **Retrieval Augmented Generation (RAG)** para optimizar el servicio de atención al cliente en la empresa EcoMarket.

El sistema permite automatizar la atención de consultas frecuentes, mejorar los tiempos de respuesta y garantizar respuestas precisas basadas en información real.

---

## Problema

EcoMarket enfrenta:

* Alto volumen de consultas
* 80% de preguntas repetitivas
* Tiempo de respuesta promedio de 24 horas
* Baja satisfacción del cliente

---

## Solución propuesta

Se implementa un sistema basado en:

* Modelo de Lenguaje (LLM)
* Sistema RAG (recuperación de información)
* Base de datos de pedidos

El sistema responde automáticamente consultas como:

* Estado de pedidos
* Procesos de devolución
* Información de productos

---

## Arquitectura

```plaintext
Usuario → Chatbot → LLM → RAG → Base de datos → Respuesta
```

---

## Estructura del proyecto

```plaintext
ecoassist-rag/
├── fase1.md
├── fase2.md
├── fase3.md
├── src/
├── data/
└── notebooks/
```

---

## Cómo ejecutar

1. Clonar repositorio:

```bash
git clone https://github.com/tu-usuario/ecoassist-rag.git
cd ecoassist-rag
```

2. Instalar dependencias:

```bash
pip install -r requirements.txt
```

3. Ejecutar simulación:

```bash
python src/rag_simulation.py
```

---

## Ejemplo de uso

```python
generar_respuesta_pedido("12347")
```

---

## Consideraciones éticas

* Protección de datos del usuario
* Mitigación de sesgos
* Supervisión humana
* Transparencia del sistema

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
