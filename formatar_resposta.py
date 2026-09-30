"""Converte respostas HTML dos provedores em Markdown/texto legível."""
from __future__ import annotations

import html
import re


_TAG_HTML = re.compile(
    r"<\s*(br|p|div|span|strong|em|b|i|ul|ol|li|h[1-6]|a)\b",
    re.I,
)


def parece_html(texto: str) -> bool:
    return bool(_TAG_HTML.search(texto or ""))


def _html_para_texto(texto: str) -> str:
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(texto, "html.parser")
    for br in soup.find_all("br"):
        br.replace_with("\n")
    for p in soup.find_all("p"):
        p.insert_after("\n")
    out = soup.get_text("\n")
    out = html.unescape(out)
    return re.sub(r"\n{3,}", "\n\n", out).strip()


def formatar_resposta(texto: str) -> str:
    """Texto pronto para `st.markdown` ou impressão no terminal."""
    if not texto:
        return ""
    bruto = texto.strip()
    if not parece_html(bruto):
        return bruto
    try:
        from markdownify import markdownify

        md = markdownify(
            bruto,
            heading_style="ATX",
            bullets="-",
            strip=["script", "style", "iframe", "object", "embed"],
        ).strip()
        if md:
            return re.sub(r"\n{3,}", "\n\n", md)
    except Exception:
        pass
    return _html_para_texto(bruto)
