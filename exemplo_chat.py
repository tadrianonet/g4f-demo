#!/usr/bin/env python3
"""Exemplo de linha de comando para aula — chama um modelo via g4f.

Uso:
    python exemplo_chat.py
    python exemplo_chat.py "Explique o que é uma API em duas frases."
    python exemplo_chat.py --model gpt-4o-mini "Olá"

Com Docker (API local do g4f na porta 8080):
    G4F_API_BASE=http://127.0.0.1:8080/v1 python exemplo_chat.py "Olá"
"""
from __future__ import annotations

import argparse
import sys

from verificar_python import exigir_python_minimo

exigir_python_minimo()

from chat import enviar_mensagem
from config import get_settings
from formatar_resposta import formatar_resposta


def main() -> int:
    settings = get_settings()
    parser = argparse.ArgumentParser(description="Demo GPT4Free (g4f) para aula")
    parser.add_argument("prompt", nargs="?", default="Diga apenas: funcionou")
    parser.add_argument("--model", default=settings.model)
    args = parser.parse_args()

    modo = "API local" if settings.api_base else (
        f"provedor {settings.provider}" if settings.provider else "provedor automático do g4f"
    )
    print(f"Modelo: {args.model} | Modo: {modo}", file=sys.stderr)

    try:
        texto = enviar_mensagem(args.prompt, model=args.model, settings=settings)
    except Exception as exc:
        print(f"Erro: {type(exc).__name__}: {exc}", file=sys.stderr)
        print(
            "\nDicas:\n"
            "  1) pip install -U 'g4f[all]'\n"
            "  2) docker compose up -d  e  G4F_API_BASE=http://127.0.0.1:8080/v1\n"
            "  3) python listar_provedores.py --model gpt-4o-mini\n"
            "Docs: https://github.com/xtekky/gpt4free",
            file=sys.stderr,
        )
        return 1

    print(formatar_resposta(texto))
    return 0 if texto else 2


if __name__ == "__main__":
    raise SystemExit(main())
