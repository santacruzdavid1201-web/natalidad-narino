# Natalidad, ventana demográfica, crecimiento económico y mercado laboral en Nariño, 2005–2024

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/natalidad-narino/natalidad-narino/blob/main/natalidad_narino.ipynb)
[![Asistente RAG en Colab](https://img.shields.io/badge/Asistente_RAG-Colab-eb6834?logo=googlecolab)](https://colab.research.google.com/github/natalidad-narino/natalidad-narino/blob/main/rag/consulta_rag.ipynb)
[![Observatorio](https://img.shields.io/badge/Observatorio-web-2a78d6)](https://natalidad-narino.github.io/natalidad-narino/)

Código reproducible del artículo final de **Seminario de Investigación Regional II** (Programa de Economía, Universidad de Nariño).
Pregunta: ¿la caída de la natalidad amplió la ventana demográfica de Nariño entre 2005 y 2024, en qué magnitud se asoció esa ventana con el crecimiento del PIB real per cápita y con la participación laboral, y en qué se diferencia esa relación de la observada en los demás departamentos?

## Cómo ejecutarlo

1. Haga clic en **Abrir en Colab** (arriba).
2. En Colab: **Entorno de ejecución → Ejecutar todas**. La primera celda clona este repositorio (con los datos) y tarda de 3 a 5 minutos en total.
3. Cada archivo se pide primero a su URL oficial. El DANE rechaza las conexiones desde servidores en la nube (error 401); en ese caso se usa la copia original de `datos/raw/`. La tabla de la sección 1 informa qué fuente se usó.
4. La sección 9 abre los **paneles interactivos** (series, mapa, pirámides y re-estimación del modelo).
5. La sección 10 descarga `salidas.zip` con las figuras y tablas numeradas como en el artículo.

**En un computador propio** (Python 3.10+):

```bash
git clone https://github.com/natalidad-narino/natalidad-narino.git
cd natalidad-narino
pip install -r requirements.txt
jupyter notebook natalidad_narino.ipynb
```

## Cuatro métodos sobre la misma pregunta

| Método | Variación que usa | Sección del notebook |
|---|---|---|
| Panel con efectos fijos de departamento y año (errores agrupados, bootstrap salvaje, placebos) | Dentro de cada departamento, año a año | 5 y 6 |
| Diferencias largas entre departamentos (HC3) | Entre departamentos, 1991–2009 → 2006–2024 | 5 |
| Panel dinámico System GMM (instrumentos colapsados, Hansen, AR(2)) | Dentro y entre, con persistencia del crecimiento | 5b |
| ARDL y prueba de límites para Nariño | Serie de tiempo de un departamento | 7 |

La sección 8 confronta los cuatro estimadores del mismo parámetro (Figura 9, Tabla 9).

## Productos tecnológicos

| Producto | Dónde | Qué hace |
|---|---|---|
| Código reproducible | `natalidad_narino.ipynb` | Descarga, armoniza, estima los cuatro métodos y genera cada tabla y figura del artículo (en español y en inglés: `salidas/figuras_en/`). |
| Observatorio estadístico | `docs/` · https://natalidad-narino.github.io/natalidad-narino/ | Sitio web con series por departamento, mapa, transición demográfica, confrontación de métodos, estado de las fuentes y descargas. |
| Rastreador de datos | `rastreador/` + `.github/workflows/rastreador.yml` | Cada lunes revisa las fuentes oficiales (encabezados HTTP, huellas SHA-256, páginas índice, API del Banco Mundial), registra el resultado en `rastreador/registro.csv`, vuelve a ejecutar el notebook y actualiza el observatorio. |
| Asistente de consulta (RAG) | `rag/consulta_rag.ipynb` | Chat en Colab sobre el corpus del proyecto (artículo ES/EN, documentación, tablas, referencias) con recuperación híbrida BM25 + embeddings multilingües, modelo abierto Qwen2.5 y citas por documento, sección y página; incluye evaluación de la recuperación. |

El artículo final está en `articulo/` (versiones en español e inglés).

## Estructura

```
├── natalidad_narino.ipynb   # notebook único: datos → análisis → figuras/tablas → paneles interactivos
├── articulo/                # artículo final en español e inglés (PDF)
├── docs/                    # observatorio web (GitHub Pages)
├── observatorio/construir.py
├── rastreador/              # verificación semanal de fuentes oficiales y registro
├── rag/                     # asistente de consulta: núcleo, configuración y notebook de Colab
├── config/                  # traducción de las figuras al inglés
├── requirements.txt
├── datos/
│   ├── FUENTES.md           # URL oficial, entidad y fecha de consulta de cada archivo
│   └── raw/                 # copias originales de las fuentes oficiales
└── salidas/
    ├── figuras/             # Figura_1 … Figura_9
    ├── figuras_en/          # las mismas figuras con textos en inglés
    ├── tablas/              # Tablas 2, 5, 6, 6c, 7, 7b, 8a, 8b, 9 (Excel y CSV)
    ├── datos/               # bases armonizadas (CSV) que usan el observatorio y el RAG
    └── resultados_clave.json
```

Autores: Francisco Quiroz Oñate y Santiago Enríquez Villarreal. Docente: Julio César Riascos Hermoza.
