"""Verificação de versão do Python (g4f exige 3.10+)."""
from __future__ import annotations

import sys

MIN = (3, 10)


def python_suportado() -> bool:
    return sys.version_info >= MIN


def mensagem_python_insuficiente() -> str:
    v = ".".join(map(str, sys.version_info[:3]))
    need = ".".join(map(str, MIN))
    return (
        f"Este demo exige **Python {need} ou superior** (detectado: **{v}**).\n\n"
        "No macOS, recrie o ambiente virtual:\n\n"
        "```bash\n"
        "brew install python@3.11\n"
        "python3.11 -m venv .venv\n"
        "source .venv/bin/activate\n"
        "pip install -r requirements.txt\n"
        "streamlit run app.py\n"
        "```"
    )


def exigir_python_minimo() -> None:
    if not python_suportado():
        print(mensagem_python_insuficiente().replace("**", ""), file=sys.stderr)
        raise SystemExit(1)
