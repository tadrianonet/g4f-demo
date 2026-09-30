"""Teste local sem rede: valida o fluxo de mensagens com cliente simulado."""
from __future__ import annotations

from types import SimpleNamespace
from unittest.mock import MagicMock, patch

import chat
from config import Settings


def test_enviar_mensagem_retorna_conteudo():
    fake = SimpleNamespace(
        choices=[SimpleNamespace(message=SimpleNamespace(content=" funcionou "))]
    )
    mock_client = MagicMock()
    mock_client.chat.completions.create.return_value = fake

    with patch.object(chat, "criar_cliente", return_value=mock_client):
        assert chat.enviar_mensagem("oi", settings=Settings(model="gpt-4o-mini")) == "funcionou"
    mock_client.chat.completions.create.assert_called_once()
