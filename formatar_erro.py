"""Resume erros longos do g4f (RetryProvider) para exibição em aula."""
from __future__ import annotations

import re
from dataclasses import dataclass, field


@dataclass
class FalhaProvedor:
    provedor: str
    tipo: str
    resumo: str


@dataclass
class ErroResumido:
    titulo: str
    mensagem: str
    falhas: list[FalhaProvedor] = field(default_factory=list)
    tecnico: str = ""
    sugerir_docker: bool = False


_LINHA_PROVEDOR = re.compile(
    r"^([A-Za-z][A-Za-z0-9]*):\s*((?:\w+Error)|RuntimeError|Error)\s*:\s*(.+)$",
    re.MULTILINE,
)


def _resumo_falha(tipo: str, detalhe: str) -> str:
    t = tipo.lower()
    d = detalhe.lower()
    if "missingauth" in t or "401" in detalhe or "api key" in d or "sign in" in d:
        return "exige login, cookie ou chave de API"
    if "paymentrequired" in t or "402" in detalhe or "subscription" in d:
        return "modelo pago ou saldo no provedor"
    if "verification" in d or "no reply" in d:
        return "bloqueio ou verificação no provedor"
    if "460" in detalhe or "invalid response status" in d:
        return "conexão recusada pelo serviço"
    if "timeout" in t or "timeout" in d:
        return "tempo esgotado"
    if "runtimeerror" in t:
        return "provedor indisponível no momento"
    curto = detalhe.replace("\n", " ").strip()
    return (curto[:120] + "…") if len(curto) > 120 else curto


def _extrair_falhas(texto: str) -> list[FalhaProvedor]:
    if "RetryProvider failed:" in texto:
        texto = texto.split("RetryProvider failed:", 1)[-1]
    falhas: list[FalhaProvedor] = []
    for m in _LINHA_PROVEDOR.finditer(texto):
        provedor, tipo, detalhe = m.group(1), m.group(2), m.group(3).strip()
        falhas.append(FalhaProvedor(provedor, tipo, _resumo_falha(tipo, detalhe)))
    return falhas


def resumir_erro(exc: BaseException, *, api_base: str = "") -> ErroResumido:
    tecnico = f"{type(exc).__name__}: {exc}".strip()
    falhas = _extrair_falhas(tecnico)
    retry = "RetryProvider" in type(exc).__name__ or "RetryProvider failed" in tecnico

    if falhas:
        titulo = "Nenhum provedor conseguiu responder"
        mensagem = (
            f"O g4f tentou **{len(falhas)}** provedor(es) e todos falharam. "
            "Provedores gratuitos mudam o tempo todo; isso não significa que seu código está errado."
        )
        sugerir = retry and not api_base
        return ErroResumido(titulo, mensagem, falhas, tecnico, sugerir)

    titulo = "Erro ao chamar o modelo"
    mensagem = "Não foi possível obter resposta. Veja os detalhes técnicos abaixo."
    return ErroResumido(titulo, mensagem, [], tecnico, not api_base)


def dica_docker_markdown() -> str:
    return (
        "**Recomendado na sala de aula:** use a API local do container oficial.\n\n"
        "1. Abra o Docker Desktop\n"
        "2. `docker compose up -d`\n"
        "3. No arquivo `.env`:\n\n"
        "```env\nG4F_API_BASE=http://127.0.0.1:8080/v1\n```\n\n"
        "4. Reinicie o Streamlit e teste de novo (GUI do g4f: http://localhost:8080)"
    )
