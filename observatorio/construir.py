"""Construye los datos del observatorio web (docs/datos.json) a partir de las salidas del notebook.
Uso: python observatorio/construir.py   (después de ejecutar natalidad_narino.ipynb)"""
import json, shutil
from datetime import datetime, timezone
from pathlib import Path
import pandas as pd

BASE = Path(__file__).resolve().parents[1]
S, DOCS = BASE / "salidas", BASE / "docs"
DOCS.mkdir(exist_ok=True)

def serie(df, cols):
    return {c: [None if pd.isna(v) else round(float(v), 3) for v in df[c]] for c in cols}

panel = pd.read_csv(S / "datos" / "panel_departamental.csv", dtype={"dp": str})
demo = pd.read_csv(S / "datos" / "demografia_1985_2050.csv", dtype={"dp": str})
VARS_P = ["ypc", "g", "tbn", "tgf", "pet_sh", "dep_juv", "dep_vej", "tgp", "to", "td", "agro_sh", "minas_sh"]
VARS_D = ["tbn", "tgf", "pet_sh", "dep_juv", "dep_vej"]
panel["ypc"] = panel.ypc / 1e6
deptos = (panel[["dp", "depto"]].drop_duplicates().sort_values("depto").to_dict("records"))
datos = {
    "meta": {"generado": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
             "repositorio": "https://github.com/santacruzdavid1201-web/natalidad-narino"},
    "deptos": deptos,
    "panel": {dp: {"anio": g.anio.tolist(), **serie(g, [v for v in VARS_P if v in g])} for dp, g in panel.groupby("dp")},
    "demografia": {dp: {"anio": g.anio.tolist(), **serie(g, VARS_D)} for dp, g in demo.groupby("dp")},
    "clave": json.loads((S / "resultados_clave.json").read_text()),
    "inf_media": pd.read_csv(S / "datos" / "informalidad_capitales.csv", dtype={"dp": str}).groupby("dp").inf.mean().round(2).to_dict(),
    "metodos": pd.read_csv(S / "tablas" / "Tabla_9_confrontacion.csv").round(3).to_dict("records"),
    "gmm": pd.read_csv(S / "tablas" / "Tabla_6c_gmm.csv", index_col=0, keep_default_na=False).reset_index().to_dict("records"),
}
(DOCS / "datos.json").write_text(json.dumps(datos, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
shutil.copy(BASE / "datos" / "raw" / "mapa_departamentos.geojson", DOCS / "mapa.geojson")
print("docs/datos.json:", round((DOCS / "datos.json").stat().st_size / 1024), "KB")
