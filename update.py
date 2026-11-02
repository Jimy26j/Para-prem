import json
import urllib.request

URL = "https://puntoplaytv.one/puntoplaytv/superadmin/paneltv/tv3.json"
ARCHIVO = "dato.json"

with urllib.request.urlopen(URL) as r:
    fuente = json.load(r)

# Índice de la fuente: (categoría, sample) -> url
urls = {
    (cat.get("name"), s.get("name")): s.get("url")
    for cat in fuente
    for s in cat.get("samples", [])
}

with open(ARCHIVO, encoding="utf-8") as f:
    mio = json.load(f)

for cat in mio:
    for s in cat.get("samples", []):
        nueva = urls.get((cat.get("name"), s.get("name")))
        if nueva:  # solo actualiza si existe en la fuente
            s["url"] = nueva

with open(ARCHIVO, "w", encoding="utf-8") as f:
    json.dump(mio, f, ensure_ascii=False, indent=2)
    f.write("\n")
