#!/usr/bin/env python3
"""Lista provedores registrados no g4f instalado (metadados estáticos)."""
from __future__ import annotations

import argparse
import json

from config import get_settings
from verificar_python import exigir_python_minimo


def main() -> int:
    exigir_python_minimo()
    from g4f.Provider import ProviderLoader

    settings = get_settings()
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default=settings.model, help="Destaca provedores que listam este modelo")
    args = parser.parse_args()

    try:
        from g4f.models import ModelUtils

        best = ModelUtils.convert.get(args.model)
        sugeridos = []
        if best and best.best_provider:
            bp = best.best_provider
            provs = getattr(bp, "providers", [bp])
            sugeridos = [p if isinstance(p, str) else getattr(p, "__name__", str(p)) for p in provs]
    except Exception:
        sugeridos = []

    print(f"Modelo: {args.model}")
    if sugeridos:
        print("Sugeridos pelo g4f para este modelo:", ", ".join(sugeridos))
    print(f"Total de provedores no pacote: {len(ProviderLoader.names)}\n")

    for name in ProviderLoader.names:
        row = {"name": name, "sugerido": name in sugeridos}
        try:
            cls = ProviderLoader.from_name(name)
            row["working"] = bool(getattr(cls, "working", False))
            row["needs_auth"] = bool(getattr(cls, "needs_auth", False))
            if args.model:
                models = getattr(cls, "models", ()) or ()
                aliases = getattr(cls, "model_aliases", {}) or {}
                row["suporta_modelo"] = args.model in models or args.model in aliases
        except Exception as exc:
            row["erro"] = str(exc)[:120]
        print(json.dumps(row, ensure_ascii=False))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
