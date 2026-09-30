"""Cliente de chat usando o pacote oficial g4f (GPT4Free).

Documentação: https://g4f.dev/docs/client
Repositório: https://github.com/xtekky/gpt4free
"""
from __future__ import annotations

from typing import Optional

from config import Settings, get_settings


def criar_cliente(settings: Optional[Settings] = None):
    """Instancia Client ou Client apontando para a API local (Docker)."""
    from g4f.client import Client

    settings = settings or get_settings()
    if settings.api_base:
        return Client(base_url=settings.api_base.rstrip("/"))
    if settings.provider:
        from g4f.Provider import ProviderLoader

        provider = ProviderLoader.from_name(settings.provider)
        return Client(provider=provider)
    return Client()


def enviar_mensagem(
    prompt: str,
    *,
    model: Optional[str] = None,
    settings: Optional[Settings] = None,
) -> str:
    settings = settings or get_settings()
    model = (model or settings.model).strip()
    client = criar_cliente(settings)
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        web_search=False,
    )
    return (response.choices[0].message.content or "").strip()
