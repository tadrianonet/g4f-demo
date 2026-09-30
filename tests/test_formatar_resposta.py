from formatar_resposta import formatar_resposta, parece_html


def test_parece_html():
    assert parece_html("<strong>LLM</strong> é um modelo.")
    assert not parece_html("Texto simples sem tags.")


def test_html_vira_markdown_legivel():
    bruto = (
        '<strong class="x">LLM</strong> significa Large Language Model.<br />'
        "Exemplo: ChatGPT."
    )
    limpo = formatar_resposta(bruto)
    assert "LLM" in limpo
    assert "Large Language Model" in limpo
    assert "<strong" not in limpo
    assert "<br" not in limpo
