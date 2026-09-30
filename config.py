"""Configuração mínima via .env ou variáveis de ambiente."""
from __future__ import annotations

import os
from dataclasses import dataclass

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass


@dataclass
class Settings:
    model: str = os.getenv("G4F_MODEL", "gpt-4o-mini").strip()
    provider: str = os.getenv("G4F_PROVIDER", "").strip()
    api_base: str = os.getenv("G4F_API_BASE", "").strip()


def get_settings() -> Settings:
    return Settings()
