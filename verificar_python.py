"""Exige Python 3.10+ (necessário para o pacote g4f)."""
import sys

MIN = (3, 10)


def exigir_python_minimo() -> None:
    if sys.version_info < MIN:
        v = ".".join(map(str, sys.version_info[:3]))
        need = ".".join(map(str, MIN))
        print(f"Este demo exige Python {need} ou superior (atual: {v}).", file=sys.stderr)
        raise SystemExit(1)
