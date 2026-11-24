# Natalidad, crecimiento económico y mercado laboral en Nariño, 2005–2024

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/santacruzdavid1201-web/natalidad-narino/blob/main/natalidad_narino.ipynb)

Código reproducible del artículo final de **Seminario de Investigación Regional II** (Programa de Economía, Universidad de Nariño).
Pregunta: ¿en qué magnitud y dirección se ha asociado la natalidad rezagada con el crecimiento del PIB real per cápita y con el mercado laboral de Nariño entre 2005 y 2024, y en qué se diferencia esa relación de la observada en los demás departamentos?

## Cómo ejecutarlo

1. Haga clic en **Abrir en Colab** (arriba).
2. En Colab: **Entorno de ejecución → Ejecutar todas**. La primera celda clona este repositorio (con los datos) y tarda de 3 a 5 minutos en total.
3. Cada archivo se pide primero a su URL oficial. El DANE rechaza las conexiones desde servidores en la nube (error 401); en ese caso se usa la copia original de `datos/raw/`. La tabla de la sección 1 informa qué fuente se usó.
4. La sección 9 abre los **paneles interactivos** (series, mapa, pirámides y re-estimación del modelo).
5. La sección 10 descarga `salidas.zip` con las figuras y tablas numeradas como en el artículo.

**En un computador propio** (Python 3.10+):

```bash
git clone https://github.com/santacruzdavid1201-web/natalidad-narino.git
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

## Estructura

```
├── natalidad_narino.ipynb   # notebook único: datos → análisis → figuras/tablas → paneles interactivos
├── requirements.txt
├── datos/
│   ├── FUENTES.md           # URL oficial, entidad y fecha de consulta de cada archivo
│   └── raw/                 # copias originales de las fuentes oficiales
└── salidas/
    ├── figuras/             # Figura_1 … Figura_9
    ├── tablas/              # Tablas 2, 5, 6, 6c, 7, 7b, 8a, 8b, 9 (Excel y CSV)
    └── resultados_clave.json
```

Autores: Francisco Quiroz Oñate y Santiago Enríquez Villarreal. Docente: Julio César Riascos Hermoza.
