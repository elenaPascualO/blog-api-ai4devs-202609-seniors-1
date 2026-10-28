#!/usr/bin/env python3
"""Hook PostToolUse (Write|Edit): añade una línea a MARCADORES-blog-api.txt por cada archivo escrito.

Ruta absoluta para no depender del directorio de trabajo: registra también archivos fuera del repo.
Nunca bloquea: ante cualquier error sale con 0 sin escribir nada.
"""
import json
import sys
from datetime import datetime

MARCADORES = "/Users/elena.pascual.ext/Development/PERSONAL/LIDR/blog/blog-api/MARCADORES-blog-api.txt"

try:
    data = json.load(sys.stdin)
    herramienta = data.get("tool_name", "?")
    ruta = (data.get("tool_input") or {}).get("file_path", "?")
    with open(MARCADORES, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now().isoformat(timespec='seconds')}\t{herramienta}\t{ruta}\n")
except Exception:
    pass
sys.exit(0)
