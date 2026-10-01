---
title: "🤖 Modelos Together AI para Obsidian - Cuenta Básica"
date: 2026-05-25
tags: [obsidian, together-ai, llm, api, config]
author: Diego Polanco
version: 1.0
---

# 🤖 Modelos Together AI para Obsidian - Cuenta Básica

> [!INFO] Metadata
> **Actualizado:** Mayo 2026  
> **Fuente oficial:** [Together AI Models](https://www.together.ai/models) | [Documentación API](https://docs.together.ai/)  
> **Estado de cuenta:** Básica (Free Tier con $25 créditos iniciales)

---

## 📋 Información General de la Cuenta Básica

Together AI ofrece una cuenta gratuita con **$25 en créditos iniciales** para nuevos usuarios, lo que equivale aproximadamente a ~5-10 millones de tokens dependiendo del modelo utilizado.

```yaml
# Configuración básica de la cuenta
- Créditos iniciales: $25 USD
- Modelo de cobro: Pay-per-token (sin mínimos mensuales)
- Compatibilidad API: OpenAI-compatible (drop-in replacement)
- Rate limits: Aplicados por modelo, no por tier de cuenta
- Acceso global: Disponible con latencia optimizada
- Soporte: Comunidad + documentación oficial
```


---

## 🔑 Configuración en Obsidian

### Plugins compatibles con Together AI

|Plugin|Funcionalidad principal|Configuración Together AI requerida|
|---|---|---|
|**Copilot for Obsidian**|Chat, sugerencias inline, web search|Base URL: `https://api.together.ai/v1`|
|**Smart Connections**|Búsqueda semántica, descubrimiento de conexiones|Requiere modelo de embedding compatible|
|**AI Providers**|Gestión centralizada de claves API|Guarda credenciales para múltiples plugins|
|**Text Generator**|Generación de texto con templates|Endpoint personalizado + modelo|

### Pasos de configuración (Copilot for Obsidian)

1. Instalar el plugin desde _Community Plugins_ en Obsidian
2. Ir a `Settings → Copilot → Basic Settings`
3. En **API Provider**, seleccionar _OpenAI Compatible_
4. Configurar los siguientes campos:
				
				Base URL: https://api.together.ai/v1
				API Key: tu_clave_de_together_ai
				Model: meta-llama/Llama-3.3-70B-Instruct-Turbo
    
5. Opcional: Configurar temperatura, max_tokens y system prompt
6. ¡Listo! Puedes chatear con tus notas desde el panel lateral

> [!TIP] Obtén tu API Key Visita [Together AI Dashboard](https://api.together.ai/settings/api-keys) para generar y gestionar tus claves. Nunca compartas tu clave en notas públicas o repositorios.

---

## 🧠 Modelos de Chat Recomendados (Cuenta Básica)

### ✨ Mejores opciones costo-rendimiento para uso diario

| Modelo            | API String                                | Contexto | Input/1M | Output/1M | Func. Calling | Uso recomendado                                         |
| ----------------- | ----------------------------------------- | -------- | -------- | --------- | ------------- | ------------------------------------------------------- |
| **Llama 3.3 70B** | `meta-llama/Llama-3.3-70B-Instruct-Turbo` | 128K     | $0.88    | $0.88     | ✅             | Chat general, razonamiento complejo, análisis académico |
| **Qwen3.5 9B**    | `Qwen/Qwen3.5-9B`                         | 256K     | $0.10    | $0.15     | ✅             | Tareas rápidas, borradores, bajo costo                  |
| **Gemma 4 31B**   | `google/gemma-4-31B-it`                   | 256K     | $0.20    | $0.50     | ✅             | Análisis de texto, resumen, multilingüe                 |
| **GPT-OSS 20B**   | `openai/gpt-oss-20b`                      | 128K     | $0.05    | $0.20     | ✅             | Prototipado, pruebas, desarrollo                        |
| **LFM2 24B**      | `LiquidAI/LFM2-24B-A2B`                   | 32K      | $0.03    | $0.12     | ❌             | Procesamiento batch económico, extracción simple        |

> [!TIP] Estrategia de costos Para maximizar tus créditos gratuitos, comienza con `Qwen/Qwen3.5-9B` ($0.10/1M tokens) para tareas simples y escala a modelos más potentes solo cuando sea necesario.

### 🚀 Modelos avanzados (usar con moderación por costo)

| Modelo              | API String                    | Contexto | Input/1M | Output/1M | Características especiales                          |
| ------------------- | ----------------------------- | -------- | -------- | --------- | --------------------------------------------------- |
| **Qwen3.5 397B**    | `Qwen/Qwen3.5-397B-A17B`      | 256K     | $0.60    | $3.60     | Visión, razonamiento complejo, multilingüe avanzado |
| **Kimi K2.6**       | `moonshotai/Kimi-K2.6`        | 256K     | $1.20    | $4.50     | Caché de input ($0.20/1M), contexto ultra-largo     |
| **DeepSeek-V4-Pro** | `deepseek-ai/DeepSeek-V4-Pro` | 512K     | $2.10    | $4.40     | Caché de input, razonamiento matemático             |
| **GLM-5.1**         | `zai-org/GLM-5.1`             | 202K     | $1.40    | $4.40     | Function calling avanzado, agentic workflows        |

---

## 🔍 Modelos de Embedding para Búsqueda Semántica

Para plugins como **Smart Connections** que requieren embeddings para búsqueda vectorial:

| Modelo                    | API String                                | Dimensión | Contexto | Precio/1M tokens | Idiomas                |
| ------------------------- | ----------------------------------------- | --------- | -------- | ---------------- | ---------------------- |
| **Multilingual-e5-large** | `intfloat/multilingual-e5-large-instruct` | 1024      | 514      | $0.02            | 100+ (incluye español) |

> [!NOTE] Limitación de embeddings Actualmente Together AI ofrece un modelo de embedding vía serverless. Para más opciones o uso offline, considera usar modelos locales con Ollama o integrar con otros proveedores de embeddings.

---

## 🎨 Modelos Multimodales Disponibles

### Generación de Imágenes

##### Precios por megapíxel (MP) - Generación de imágenes
- FLUX.1 [schnell]: $0.0027/MP (4 pasos por defecto)
- FLUX.1 [pro]: $0.04/MP (calidad premium)
- Qwen Image: $0.0058/MP
- Stable Diffusion 3: $0.0019/MP
> [!CALC] Fórmula de costo FLUX `Costo = MP × Precio/MP × (Pasos_reales ÷ Pasos_defecto)`  
> Ejemplo: Imagen 1024×1024 (~1MP) con FLUX.1 [schnell] a 8 pasos = 1 × $0.0027 × (8÷4) = $0.0054

### Visión (Análisis de imágenes con texto)

| Modelo       | API String               | Input/1M | Output/1M | Notas                                        |
| ------------ | ------------------------ | -------- | --------- | -------------------------------------------- |
| Qwen3.5 397B | `Qwen/Qwen3.5-397B-A17B` | $0.60    | $3.60     | Mejor precisión en OCR y razonamiento visual |
| Qwen3.5 9B   | `Qwen/Qwen3.5-9B`        | $0.10    | $0.15     | Opción económica para análisis básico        |

### Audio y Transcripción

| Modelo           | Tipo           | API String                | Precio         | Caso de uso                                 |
| ---------------- | -------------- | ------------------------- | -------------- | ------------------------------------------- |
| Whisper Large v3 | Speech-to-Text | `openai/whisper-large-v3` | $0.0015/min    | Transcripción de entrevistas, notas de voz  |
| Kokoro           | Text-to-Speech | `hexgrad/Kokoro-82M`      | $4.00/1M chars | Lectura en voz alta de notas, accesibilidad |

---

## ⚙️ Ejemplo de Consulta API (Python)

```python
from together import Together
import os

# Inicializar cliente con configuración Together AI
client = Together(
    api_key=os.environ.get("TOGETHER_API_KEY"),
    base_url="https://api.together.ai/v1"  # Endpoint compatible con OpenAI
)

# Ejemplo de chat completion
response = client.chat.completions.create(
    model="meta-llama/Llama-3.3-70B-Instruct-Turbo",
    messages=[
        {"role": "system", "content": "Eres un asistente útil para tomar notas en Obsidian. Responde en español con formato markdown."},
        {"role": "user", "content": "Resume los puntos clave de esta nota sobre economía chilena..."}
    ],
    max_tokens=1024,
    temperature=0.7,
    stream=False  # Cambiar a True para streaming en tiempo real
)

# Imprimir respuesta
print(response.choices[0].message.content)
```


> [!BOOK] Recursos de desarrollo
> 
> - [Together AI Python SDK](https://github.com/togethercomputer/together-python)
> - [Referencia de API REST](https://docs.together.ai/reference/models)
> - [Cookbooks y ejemplos prácticos](https://docs.together.ai/docs/cookbooks)

---

## 💰 Estrategias para Optimizar Créditos Gratuitos

1. **Usa modelos pequeños para tareas simples**: `Qwen/Qwen3.5-9B` es 8x más económico que modelos grandes para tareas de resumen o clasificación básica.
2. **Aprovecha el caching de input**: Modelos como Kimi K2.6 y DeepSeek-V4-Pro ofrecen input caching con ~80-90% de descuento en tokens repetidos.
3. **Batch processing para tareas no urgentes**: Usa la API Batch con hasta 50% de descuento para procesamiento asincrónico de grandes volúmenes.
4. **Monitoriza tu uso en tiempo real**: Revisa el dashboard de Together AI (`Settings → Usage`) para tracking detallado por modelo y endpoint.
5. **Configura alertas de gasto**: Establece límites y notificaciones en `Settings → Billing` para evitar consumos inesperados.
6. **Reutiliza system prompts**: Guarda prompts del sistema eficientes en snippets de Obsidian para reducir tokens de contexto repetidos.
7. **Trunca contexto innecesario**: Antes de enviar notas largas, pre-procesa para incluir solo secciones relevantes a la consulta.

---

## 🔗 Recursos Adicionales

- [📦 Catálogo completo de modelos](https://www.together.ai/models)
- [📚 Documentación técnica oficial](https://docs.together.ai/)
- [💵 Guía de precios actualizada](https://www.together.ai/pricing)
- [⚡ Rate limits por modelo](https://docs.together.ai/docs/serverless/rate-limits)
- [🍳 Cookbooks y ejemplos de código](https://docs.together.ai/docs/cookbooks)
- [💬 Comunidad Obsidian + AI](https://forum.obsidian.md/c/help/7)
- [🔧 Plugin Copilot for Obsidian](https://github.com/logancyang/obsidian-copilot)

---

## 🗂️ Plantilla de Nota para Consultas Rápidas

 ```markdown
 ---
ai_provider: together_ai
model: meta-llama/Llama-3.3-70B-Instruct-Turbo
temperature: 0.7
max_tokens: 2048
top_p: 0.9
frequency_penalty: 0.1
language: es
---

## 📝 Consulta
{{SELECCIÓN_O_NOTA}}

## 🎯 Instrucciones para el modelo
- Responde en español neutro
- Usa formato markdown con headers y listas
- Cita fuentes o referencias cuando sea relevante
- Mantén un tono académico pero accesible
- Si la información es incierta, indícalo explícitamente

## ✨ Respuesta generada
<!-- El plugin insertará aquí la respuesta del modelo -->
 ``` 

---

## 🔄 Historial de Actualizaciones

|Versión|Fecha|Cambios|
|---|---|---|
|1.0|2026-05-25|Versión inicial con modelos disponibles, configuración y estrategias de costo|

---

> [!DISCLAIMER] Descargo de responsabilidad Los precios, disponibilidad de modelos y límites de tasa pueden cambiar sin previo aviso. Verifica siempre la [documentación oficial de Together AI](https://docs.together.ai/) antes de implementar en producción. Esta nota está diseñada para uso educativo, de investigación personal y gestión de conocimiento en Obsidian. No constituye asesoramiento técnico profesional.

_Última revisión: {{date:YYYY-MM-DD}}_  
_Autor: Diego Polanco_  
_Afiliación: Department of Economics, UMass Amherst_ ```