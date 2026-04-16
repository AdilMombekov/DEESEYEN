# -*- coding: utf-8 -*-
"""Сборка index.html из эталона furnicraft-demo.html (родитель/нужное)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT.parent / "нужное" / "furnicraft-demo.html"
OUT = ROOT / "index.html"

def main():
    if not SRC.is_file():
        raise SystemExit(f"Не найден источник: {SRC}")
    text = SRC.read_text(encoding="utf-8")
    text = text.replace("FurniCraft", "DEESEYEN")
    text = text.replace('value="Мой проект"', 'value="DEESEYEN"')
    title = "<title>DEESEYEN — 3D Furniture Builder</title>"
    meta = (
        title
        + "\n<meta name=\"description\" content=\"DEESEYEN — 3D-конструктор мебели в браузере: каталог, корпус по размерам (см), материалы, RGB, оценка нагрузки полок, фурнитура (ручки), экспорт/импорт JSON.\">"
        + "\n<meta name=\"theme-color\" content=\"#080c14\">"
        + "\n<meta property=\"og:title\" content=\"DEESEYEN — 3D Furniture Builder\">"
        + "\n<meta property=\"og:description\" content=\"Каталог мебели и параметрический корпус в одном HTML.\">"
        + "\n<meta property=\"og:type\" content=\"website\">"
        + "\n<link rel=\"icon\" href=\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect fill='%236366f1' width='32' height='32' rx='8'/%3E%3Cpath fill='white' d='M6 22h8v4H6zm12 0h8v4h-8zM6 14h20v4H6z'/%3E%3C/svg%3E\">"
    )
    if title not in text:
        raise SystemExit("Ожидался заголовок после замены бренда")
    text = text.replace(title, meta, 1)
    OUT.write_text(text, encoding="utf-8")
    print("Written", OUT, "bytes", OUT.stat().st_size)

if __name__ == "__main__":
    main()
