# Fuentes de datos

Todos los archivos de `raw/` se descargaron el 7 de noviembre de 2026 desde los enlaces oficiales indicados y se conservan sin modificaciones. El notebook vuelve a intentar cada enlace antes de usar la copia local.

| Archivo en `raw/` | Contenido | Entidad | URL oficial |
|---|---|---|---|
| `pib_total.xlsx` | PIB por departamento, base 2015, 2005–2025pr: precios corrientes (Cuadro 1), volumen encadenado (Cuadro 2) y PIB por habitante (Cuadro 3). Actualizado el 3 de julio de 2026 | DANE, Cuentas Nacionales Departamentales | https://www.dane.gov.co/files/operaciones/PIB/anex-PIBDep-TotalDep-2025pr.xlsx |
| `pib_actividad.xlsx` | Valor agregado por actividad económica y departamento, 2005–2025pr | DANE, Cuentas Nacionales Departamentales | https://www.dane.gov.co/files/operaciones/PIB/anex-PIBDep-Activecono-2025pr.xlsx |
| `pob_1985_1992.xlsx` | Retroproyecciones de población departamental por área, sexo y edad simple, 1985–1992 (base CNPV 2018) | DANE, Demografía y población | https://www.dane.gov.co/files/censo2018/proyecciones-de-poblacion/Departamental/DCD-area-sexo-edad-proypoblacion-dep-1985-1992.xlsx |
| `pob_1993_2004.xlsx` | Ídem, 1993–2004 | DANE | https://www.dane.gov.co/files/censo2018/proyecciones-de-poblacion/Departamental/DCD-area-sexo-edad-proypoblacion-dep-1993-2004.xlsx |
| `pob_2005_2017.xlsx` | Ídem, 2005–2017 | DANE | https://www.dane.gov.co/files/censo2018/proyecciones-de-poblacion/Departamental/DCD-area-sexo-edad-proypoblacion-dep-2005-2017_VP.xlsx |
| `pob_2018_2050.xlsx` | Proyecciones de población departamental por área, sexo y edad simple, 2018–2050 (actualización post-COVID-19, 30 de julio de 2025) | DANE | https://www.dane.gov.co/files/censo2018/proyecciones-de-poblacion/Departamental/PPED-AreaSexoEdadDep-2018-2050_VP.xlsx |
| `fec_dep_1985_2017.xlsx` | Estimaciones de fecundidad: TGF y tasas específicas por edad simple (10–49), nacional y departamental, 1985–2017 | DANE, Estimaciones del cambio demográfico | https://www.dane.gov.co/files/censo2018/cambio-demografico/DCD-Fec-EstNal-Dep-1985-2017_VP.xlsx |
| `geih_departamentos_2007_2025.xls` | GEIH, mercado laboral por departamento, serie anual 2007–2025 (23 departamentos, valores retroproyectados con el marco 2018). Actualizado el 15 de abril de 2026 | DANE, GEIH | https://www.dane.gov.co/files/operaciones/GEIH/anex-GEIHDepartamentos-2025.xls |
| `informalidad_oct_dic2024.xlsx` | GEIH, empleo informal y seguridad social: proporción de informalidad por ciudad, trimestre móvil 2021–2024 | DANE, GEIH | https://www.dane.gov.co/files/operaciones/GEIH/anex-GEIHEISS-oct-dic2024.xlsx |
| `mapa_departamentos.geojson` | Límites departamentales del Marco Geoestadístico Nacional 2018 (DANE) en GeoJSON | Repositorio público `caticoa3/colombia_mapa` (GitHub) | https://raw.githubusercontent.com/caticoa3/colombia_mapa/master/co_2018_MGN_DPTO_POLITICO.geojson |

**Consulta en vivo (no se guarda copia):** API de Indicadores del Desarrollo Mundial del Banco Mundial, `https://api.worldbank.org/v2/`, indicadores SP.DYN.TFRT.IN, SP.DYN.CBRT.IN, SP.POP.1564.TO.ZS y NY.GDP.PCAP.KD.ZG (sección 9.5 del notebook).

**Dato citado del boletín:** TGF de estadísticas vitales para Nariño (1,4 en 2014; 0,9 en 2023) y Colombia (1,8 y 1,2), DANE, *Boletín técnico Estadísticas Vitales – Nacimientos 2024pr*: https://www.dane.gov.co/files/operaciones/EEVV/2024/19-dic-2024/bol-EEVV-Nacimientos-2024pr.pdf

**Nota sobre el empalme de 2018.** Las series de población 2005–2017 (retroproyección) y 2018–2050 (proyección actualizada) no empalman en la estructura por edades: en Nariño la proporción 15–64 pasa de 66,6 % (2017) a 63,7 % (2018). El notebook marca ese año en las figuras y excluye la variación 2017–2018 en la especificación con Δln(PET).
